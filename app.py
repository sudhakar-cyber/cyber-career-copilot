import os
import json
from functools import wraps
from datetime import datetime, timezone
from flask import (
    Flask, render_template, request, redirect, url_for, 
    flash, session, jsonify, g, make_response
)
from werkzeug.security import generate_password_hash, check_password_hash

from config import Config
import database as db
import ai_engine
from data_seed import CAREERS_CATALOG, CERTIFICATIONS_CATALOG, PROJECTS_CATALOG

app = Flask(__name__)
app.config.from_object(Config)

# Ensure database is initialized on startup
with app.app_context():
    try:
        db.init_db()
    except Exception as e:
        print(f"[Error] Initializing DB: {e}")

# Keep sessions permanent across browser refreshes
@app.before_request
def ensure_session_persistence():
    session.permanent = True

# Prevent browser caching of authenticated views to defeat Back button exposure after logout
@app.after_request
def add_security_and_cache_control_headers(response):
    if response.content_type and 'text/html' in response.content_type:
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate, max-age=0, private'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
    return response

# Authentication decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please sign in to access your Cyber Copilot workspace.", "info")
            return redirect(url_for('login', next=request.url))
        
        # Verify active account still exists in database
        user = db.query_one("SELECT id FROM users WHERE id = %s", (session['user_id'],))
        if not user:
            session.clear()
            flash("Session expired or user account not found. Please log in again.", "warning")
            return redirect(url_for('login'))

        session.permanent = True
        return f(*args, **kwargs)
    return decorated_function

# Context processor for templates
@app.context_processor
def inject_global_data():
    current_user = None
    profile = None
    if 'user_id' in session:
        current_user = db.query_one("SELECT id, email, full_name, created_at FROM users WHERE id = %s", (session['user_id'],))
        profile = db.query_one("SELECT * FROM student_profiles WHERE user_id = %s", (session['user_id'],))
    
    return {
        'current_user': current_user,
        'student_profile': profile,
        'active_db_engine': db.ACTIVE_DB_ENGINE,
        'db_status_message': db.DB_STATUS_MESSAGE,
        'now': datetime.now(timezone.utc)
    }

# -------------------------------------------------------------
# Authentication Routes
# -------------------------------------------------------------

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        full_name = request.form.get('full_name', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        # Validations
        if not full_name or not email or not password:
            flash("All required fields must be filled.", "danger")
            return render_template('register.html', full_name=full_name, email=email)

        if len(password) < 6:
            flash("Password must be at least 6 characters long.", "danger")
            return render_template('register.html', full_name=full_name, email=email)

        if password != confirm_password:
            flash("Passwords do not match.", "danger")
            return render_template('register.html', full_name=full_name, email=email)

        # Check existing user
        existing_user = db.query_one("SELECT id FROM users WHERE email = %s", (email,))
        if existing_user:
            flash("An account with this email address already exists. Please log in.", "warning")
            return redirect(url_for('login'))

        # Secure password hashing
        password_hash = generate_password_hash(password)
        user_id = db.execute(
            "INSERT INTO users (email, password_hash, full_name) VALUES (%s, %s, %s)",
            (email, password_hash, full_name)
        )

        # Initialize blank student profile
        db.execute(
            """INSERT INTO student_profiles 
               (user_id, qualification, department, year_of_study, programming_languages, networking_skills, os_skills, cyber_level, areas_of_interest, preferred_career, weekly_study_hours)
               VALUES (%s, 'B.Tech / B.E.', 'Computer Science & Engineering', '3rd Year', 'Python, C', 'TCP/IP, Wireshark', 'Linux, Windows', 'Beginner', 'SOC Analysis, Ethical Hacking', 'SOC Analyst', 10)""",
            (user_id,)
        )

        session.permanent = True
        session['user_id'] = user_id
        session['user_name'] = full_name
        session.modified = True
        flash(f"Welcome aboard, {full_name}! Complete your cybersecurity profile to customize your roadmap.", "success")
        return redirect(url_for('profile'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        if not email or not password:
            flash("Please enter both email and password.", "danger")
            return render_template('login.html', email=email)

        user = db.query_one("SELECT id, email, password_hash, full_name FROM users WHERE email = %s", (email,))
        if not user or not check_password_hash(user['password_hash'], password):
            flash("Invalid email or password. Please verify credentials.", "danger")
            return render_template('login.html', email=email)

        # Update last login timestamp
        db.execute("UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = %s", (user['id'],))

        session.permanent = True
        session['user_id'] = user['id']
        session['user_name'] = user['full_name']
        session.modified = True
        flash(f"Welcome back, {user['full_name']}! System ready.", "success")

        next_page = request.args.get('next')
        if next_page and next_page.startswith('/'):
            return redirect(next_page)
        return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    cookie_name = app.config.get('SESSION_COOKIE_NAME', 'cyber_copilot_session')
    response = make_response(redirect(url_for('login')))
    response.delete_cookie(cookie_name, path='/')
    response.delete_cookie('session', path='/')
    flash("You have been successfully logged out. Secure session terminated.", "info")
    return response

# -------------------------------------------------------------
# Student Profile Routes
# -------------------------------------------------------------

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user_id = session['user_id']

    if request.method == 'POST':
        full_name = request.form.get('full_name', '').strip()
        qualification = request.form.get('qualification', '').strip()
        department = request.form.get('department', '').strip()
        year_of_study = request.form.get('year_of_study', '').strip()
        
        # Handle comma-separated or checkbox arrays
        prog_langs = request.form.getlist('programming_languages')
        prog_langs_str = ", ".join(prog_langs) if prog_langs else request.form.get('programming_languages_text', '')
        
        net_skills = request.form.getlist('networking_skills')
        net_skills_str = ", ".join(net_skills) if net_skills else request.form.get('networking_skills_text', '')

        os_skills = request.form.getlist('os_skills')
        os_skills_str = ", ".join(os_skills) if os_skills else request.form.get('os_skills_text', '')

        cyber_level = request.form.get('cyber_level', 'Beginner')
        
        interests = request.form.getlist('areas_of_interest')
        interests_str = ", ".join(interests) if interests else request.form.get('areas_of_interest_text', '')

        preferred_career = request.form.get('preferred_career', 'SOC Analyst')
        try:
            weekly_study_hours = int(request.form.get('weekly_study_hours', 10))
        except ValueError:
            weekly_study_hours = 10

        # Update full name in users table
        if full_name:
            db.execute("UPDATE users SET full_name = %s WHERE id = %s", (full_name, user_id))
            session['user_name'] = full_name

        # Update or insert student profile
        db.execute("""
            UPDATE student_profiles SET
                qualification = %s,
                department = %s,
                year_of_study = %s,
                programming_languages = %s,
                networking_skills = %s,
                os_skills = %s,
                cyber_level = %s,
                areas_of_interest = %s,
                preferred_career = %s,
                weekly_study_hours = %s
            WHERE user_id = %s
        """, (
            qualification, department, year_of_study, prog_langs_str,
            net_skills_str, os_skills_str, cyber_level, interests_str,
            preferred_career, weekly_study_hours, user_id
        ))

        flash("Profile updated successfully! AI recommendations updated.", "success")
        return redirect(url_for('profile'))

    prof = db.query_one("SELECT * FROM student_profiles WHERE user_id = %s", (user_id,))
    user = db.query_one("SELECT full_name, email FROM users WHERE id = %s", (user_id,))

    # Parse stored string fields into lists for convenient checkbox checking in HTML
    selected_langs = [x.strip() for x in (prof.get('programming_languages') or '').split(',') if x.strip()]
    selected_net = [x.strip() for x in (prof.get('networking_skills') or '').split(',') if x.strip()]
    selected_os = [x.strip() for x in (prof.get('os_skills') or '').split(',') if x.strip()]
    selected_interests = [x.strip() for x in (prof.get('areas_of_interest') or '').split(',') if x.strip()]

    return render_template(
        'profile.html',
        profile=prof,
        user=user,
        selected_langs=selected_langs,
        selected_net=selected_net,
        selected_os=selected_os,
        selected_interests=selected_interests,
        careers=list(CAREERS_CATALOG.keys())
    )

# -------------------------------------------------------------
# Dashboard Route
# -------------------------------------------------------------

@app.route('/dashboard')
@login_required
def dashboard():
    user_id = session['user_id']
    profile = db.query_one("SELECT * FROM student_profiles WHERE user_id = %s", (user_id,))
    if not profile:
        return redirect(url_for('profile'))

    preferred_career = profile.get('preferred_career') or "SOC Analyst"

    # 1. Learning Roadmap progress
    roadmap = db.query_one("SELECT * FROM learning_roadmaps WHERE user_id = %s AND career_title = %s", (user_id, preferred_career))
    if not roadmap:
        # Generate default roadmap for preferred career
        roadmap_data = ai_engine.generate_personalized_roadmap(profile, preferred_career)
        roadmap_id = db.execute(
            "INSERT INTO learning_roadmaps (user_id, career_title, overall_progress) VALUES (%s, %s, 0)",
            (user_id, preferred_career)
        )
        sort_idx = 0
        for ph in roadmap_data['phases']:
            for t in ph['tasks']:
                sort_idx += 1
                db.execute("""
                    INSERT INTO roadmap_tasks 
                    (roadmap_id, user_id, phase_number, phase_title, task_title, description, resource_url, is_completed, sort_order)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, 0, %s)
                """, (roadmap_id, user_id, ph['phase_number'], ph['phase_title'], t['title'], t['description'], t['resource_url'], sort_idx))
        roadmap = db.query_one("SELECT * FROM learning_roadmaps WHERE id = %s", (roadmap_id,))

    # Task completion stats
    task_stats = db.query_one("""
        SELECT 
            COUNT(*) as total_tasks,
            SUM(CASE WHEN is_completed = 1 THEN 1 ELSE 0 END) as completed_tasks
        FROM roadmap_tasks WHERE user_id = %s AND roadmap_id = %s
    """, (user_id, roadmap['id']))
    total_tasks = task_stats['total_tasks'] or 0
    completed_tasks = task_stats['completed_tasks'] or 0
    progress_percentage = int((completed_tasks / total_tasks * 100)) if total_tasks > 0 else 0

    # Upcoming tasks (next 3 uncompleted)
    upcoming_tasks = db.query_all("""
        SELECT * FROM roadmap_tasks 
        WHERE user_id = %s AND roadmap_id = %s AND is_completed = 0 
        ORDER BY phase_number ASC, sort_order ASC LIMIT 4
    """, (user_id, roadmap['id']))

    # 2. Skill Gap Readiness Score
    skill_analysis = ai_engine.analyze_skill_gap(profile, preferred_career)

    # 3. Project stats
    # Check if student has projects created; if none, copy catalog to user-specific records
    user_projects_count = db.query_one("SELECT COUNT(*) as c FROM projects WHERE user_id = %s", (user_id,))
    if not user_projects_count or user_projects_count['c'] == 0:
        for p in PROJECTS_CATALOG:
            db.execute("""
                INSERT INTO projects (user_id, title, difficulty_level, objective, prerequisites, tech_stack, milestones, learning_outcomes, status, is_custom)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 'Not Started', 0)
            """, (user_id, p['title'], p['difficulty_level'], p['objective'], p['prerequisites'], p['tech_stack'], p['milestones'], p['learning_outcomes']))

    project_stats = db.query_one("""
        SELECT 
            COUNT(*) as total_projects,
            SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) as completed_projects,
            SUM(CASE WHEN status = 'In Progress' THEN 1 ELSE 0 END) as in_progress_projects
        FROM projects WHERE user_id = %s
    """, (user_id,))

    # 4. Quiz attempt stats
    quiz_stats = db.query_one("""
        SELECT 
            COUNT(*) as attempts_count,
            AVG(percentage) as avg_score,
            MAX(percentage) as best_score
        FROM quiz_attempts WHERE user_id = %s
    """, (user_id,))

    recent_quizzes = db.query_all("""
        SELECT category, score, total_questions, percentage, created_at 
        FROM quiz_attempts WHERE user_id = %s 
        ORDER BY created_at DESC LIMIT 5
    """, (user_id,))

    # 5. Career match recommendations
    career_recs = ai_engine.get_career_recommendations(profile)
    top_career = career_recs[0] if career_recs else None

    # Chart data: skills categories breakdown for radar/doughnut chart
    skills_radar = {
        "labels": ["Network Defense", "Linux/OS", "Web Security", "Python Automation", "Threat Triage", "Cloud Security"],
        "student_scores": [
            60 if 'TCP/IP' in (profile.get('networking_skills') or '') else 30,
            75 if 'Linux' in (profile.get('os_skills') or '') else 35,
            50 if 'Ethical Hacking' in (profile.get('areas_of_interest') or '') else 25,
            70 if 'Python' in (profile.get('programming_languages') or '') else 20,
            65 if 'SOC' in (profile.get('areas_of_interest') or '') else 30,
            40 if 'Cloud Security' in (profile.get('areas_of_interest') or '') else 20
        ]
    }

    return render_template(
        'dashboard.html',
        profile=profile,
        preferred_career=preferred_career,
        roadmap=roadmap,
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        progress_percentage=progress_percentage,
        upcoming_tasks=upcoming_tasks,
        skill_analysis=skill_analysis,
        project_stats=project_stats,
        quiz_stats=quiz_stats,
        recent_quizzes=recent_quizzes,
        top_career=top_career,
        skills_radar=skills_radar
    )

# -------------------------------------------------------------
# Career Advisor Routes
# -------------------------------------------------------------

@app.route('/careers')
@login_required
def careers():
    user_id = session['user_id']
    profile = db.query_one("SELECT * FROM student_profiles WHERE user_id = %s", (user_id,))
    if not profile:
        return redirect(url_for('profile'))

    recommendations = ai_engine.get_career_recommendations(profile)
    return render_template(
        'careers.html',
        recommendations=recommendations,
        profile=profile,
        catalog=CAREERS_CATALOG
    )

@app.route('/careers/set-preferred', methods=['POST'])
@login_required
def set_preferred_career():
    user_id = session['user_id']
    chosen_career = request.form.get('career_title', '').strip()
    if chosen_career in CAREERS_CATALOG:
        db.execute("UPDATE student_profiles SET preferred_career = %s WHERE user_id = %s", (chosen_career, user_id))
        flash(f"Preferred career successfully updated to {chosen_career}! Your roadmap has been calibrated.", "success")
    return redirect(url_for('roadmap'))

# -------------------------------------------------------------
# Skill Gap Analysis Route
# -------------------------------------------------------------

@app.route('/skill-gap')
@login_required
def skill_gap():
    user_id = session['user_id']
    profile = db.query_one("SELECT * FROM student_profiles WHERE user_id = %s", (user_id,))
    if not profile:
        return redirect(url_for('profile'))

    selected_career = request.args.get('career', profile.get('preferred_career') or "SOC Analyst")
    if selected_career not in CAREERS_CATALOG:
        selected_career = "SOC Analyst"

    gap_data = ai_engine.analyze_skill_gap(profile, selected_career)
    career_info = CAREERS_CATALOG[selected_career]

    return render_template(
        'skill_gap.html',
        gap=gap_data,
        selected_career=selected_career,
        career_info=career_info,
        all_careers=list(CAREERS_CATALOG.keys()),
        profile=profile
    )

# -------------------------------------------------------------
# Learning Roadmap Routes
# -------------------------------------------------------------

@app.route('/roadmap')
@login_required
def roadmap():
    user_id = session['user_id']
    profile = db.query_one("SELECT * FROM student_profiles WHERE user_id = %s", (user_id,))
    if not profile:
        return redirect(url_for('profile'))

    preferred_career = profile.get('preferred_career') or "SOC Analyst"

    # Check or generate roadmap
    rm = db.query_one("SELECT * FROM learning_roadmaps WHERE user_id = %s AND career_title = %s", (user_id, preferred_career))
    if not rm:
        data = ai_engine.generate_personalized_roadmap(profile, preferred_career)
        rm_id = db.execute(
            "INSERT INTO learning_roadmaps (user_id, career_title, overall_progress) VALUES (%s, %s, 0)",
            (user_id, preferred_career)
        )
        sort_order = 0
        for ph in data['phases']:
            for t in ph['tasks']:
                sort_order += 1
                db.execute("""
                    INSERT INTO roadmap_tasks 
                    (roadmap_id, user_id, phase_number, phase_title, task_title, description, resource_url, is_completed, sort_order)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, 0, %s)
                """, (rm_id, user_id, ph['phase_number'], ph['phase_title'], t['title'], t['description'], t['resource_url'], sort_order))
        rm = db.query_one("SELECT * FROM learning_roadmaps WHERE id = %s", (rm_id,))

    tasks = db.query_all("""
        SELECT * FROM roadmap_tasks 
        WHERE roadmap_id = %s AND user_id = %s 
        ORDER BY phase_number ASC, sort_order ASC
    """, (rm['id'], user_id))

    # Organize tasks into 6 phases
    phases_map = {}
    total_tasks = len(tasks)
    completed_tasks = 0

    for t in tasks:
        pnum = t['phase_number']
        if pnum not in phases_map:
            phases_map[pnum] = {
                'phase_number': pnum,
                'phase_title': t['phase_title'],
                'tasks': []
            }
        phases_map[pnum]['tasks'].append(t)
        if t['is_completed']:
            completed_tasks += 1

    overall_progress = int((completed_tasks / total_tasks * 100)) if total_tasks > 0 else 0

    return render_template(
        'roadmap.html',
        roadmap=rm,
        phases=phases_map.values(),
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        overall_progress=overall_progress,
        preferred_career=preferred_career,
        all_careers=list(CAREERS_CATALOG.keys())
    )

@app.route('/api/toggle-task', methods=['POST'])
@login_required
def toggle_task():
    user_id = session['user_id']
    data = request.get_json() or {}
    task_id = data.get('task_id')
    
    if not task_id:
        return jsonify({"success": False, "error": "Missing task_id"}), 400

    task = db.query_one("SELECT * FROM roadmap_tasks WHERE id = %s AND user_id = %s", (task_id, user_id))
    if not task:
        return jsonify({"success": False, "error": "Task not found"}), 404

    new_status = 0 if task['is_completed'] else 1
    completed_time = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S') if new_status else None

    db.execute("""
        UPDATE roadmap_tasks 
        SET is_completed = %s, completed_at = %s 
        WHERE id = %s AND user_id = %s
    """, (new_status, completed_time, task_id, user_id))

    # Recalculate roadmap progress
    roadmap_id = task['roadmap_id']
    stats = db.query_one("""
        SELECT 
            COUNT(*) as total, 
            SUM(CASE WHEN is_completed = 1 THEN 1 ELSE 0 END) as done 
        FROM roadmap_tasks WHERE roadmap_id = %s
    """, (roadmap_id,))
    total = stats['total'] or 0
    done = stats['done'] or 0
    progress = int((done / total * 100)) if total > 0 else 0

    db.execute("UPDATE learning_roadmaps SET overall_progress = %s WHERE id = %s", (progress, roadmap_id))

    return jsonify({
        "success": True,
        "task_id": task_id,
        "is_completed": bool(new_status),
        "total_tasks": total,
        "completed_tasks": done,
        "overall_progress": progress
    })

# -------------------------------------------------------------
# Projects Routes
# -------------------------------------------------------------

@app.route('/projects')
@login_required
def projects():
    user_id = session['user_id']
    # Ensure user has projects
    user_projects = db.query_all("SELECT * FROM projects WHERE user_id = %s ORDER BY id ASC", (user_id,))
    if not user_projects:
        for p in PROJECTS_CATALOG:
            db.execute("""
                INSERT INTO projects (user_id, title, difficulty_level, objective, prerequisites, tech_stack, milestones, learning_outcomes, status, is_custom)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 'Not Started', 0)
            """, (user_id, p['title'], p['difficulty_level'], p['objective'], p['prerequisites'], p['tech_stack'], p['milestones'], p['learning_outcomes']))
        user_projects = db.query_all("SELECT * FROM projects WHERE user_id = %s ORDER BY id ASC", (user_id,))

    # Filter by difficulty
    difficulty_filter = request.args.get('difficulty', 'All')
    if difficulty_filter != 'All':
        displayed_projects = [p for p in user_projects if p['difficulty_level'].lower() == difficulty_filter.lower()]
    else:
        displayed_projects = user_projects

    return render_template(
        'projects.html',
        projects=displayed_projects,
        active_filter=difficulty_filter
    )

@app.route('/api/update-project-status', methods=['POST'])
@login_required
def update_project_status():
    user_id = session['user_id']
    data = request.get_json() or {}
    project_id = data.get('project_id')
    new_status = data.get('status')

    if not project_id or new_status not in ('Not Started', 'In Progress', 'Completed'):
        return jsonify({"success": False, "error": "Invalid input"}), 400

    db.execute(
        "UPDATE projects SET status = %s WHERE id = %s AND user_id = %s",
        (new_status, project_id, user_id)
    )
    return jsonify({"success": True, "project_id": project_id, "status": new_status})

# -------------------------------------------------------------
# Interview Preparation & Quiz Routes
# -------------------------------------------------------------

@app.route('/interview', methods=['GET', 'POST'])
@login_required
def interview():
    user_id = session['user_id']
    categories = ["Networking", "Linux & OS", "SOC Analysis", "Ethical Hacking", "Python Security", "Scenario Defense"]

    if request.method == 'POST':
        # Process quiz submission
        category = request.form.get('category', 'All')
        question_ids = request.form.getlist('question_ids')
        
        score = 0
        total = len(question_ids)
        details = []

        for q_id in question_ids:
            q = db.query_one("SELECT * FROM quiz_questions WHERE id = %s", (q_id,))
            if not q:
                continue
            selected_option = request.form.get(f"question_{q_id}", '').upper()
            is_correct = (selected_option == q['correct_option'])
            if is_correct:
                score += 1

            details.append({
                "id": q['id'],
                "question": q['question_text'],
                "selected": selected_option,
                "correct": q['correct_option'],
                "is_correct": is_correct,
                "explanation": q['explanation'],
                "options": {
                    "A": q['option_a'],
                    "B": q['option_b'],
                    "C": q['option_c'],
                    "D": q['option_d']
                }
            })

        percentage = round((score / total * 100), 2) if total > 0 else 0.0

        # Save attempt in DB
        db.execute("""
            INSERT INTO quiz_attempts (user_id, category, score, total_questions, percentage, details_json)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (user_id, category, score, total, percentage, json.dumps(details)))

        return render_template(
            'interview_results.html',
            category=category,
            score=score,
            total=total,
            percentage=percentage,
            details=details
        )

    # GET request - load quiz interface
    selected_category = request.args.get('category', 'All')
    if selected_category == 'All':
        questions = db.query_all("SELECT * FROM quiz_questions ORDER BY id ASC")
    else:
        questions = db.query_all("SELECT * FROM quiz_questions WHERE category = %s ORDER BY id ASC", (selected_category,))

    # Previous attempts
    attempts = db.query_all("""
        SELECT * FROM quiz_attempts 
        WHERE user_id = %s 
        ORDER BY created_at DESC LIMIT 10
    """, (user_id,))

    return render_template(
        'interview.html',
        categories=categories,
        selected_category=selected_category,
        questions=questions,
        attempts=attempts
    )

# -------------------------------------------------------------
# Certifications & Learning Resources
# -------------------------------------------------------------

@app.route('/certifications')
@login_required
def certifications():
    cost_filter = request.args.get('cost', 'all')
    diff_filter = request.args.get('difficulty', 'all')

    certs = CERTIFICATIONS_CATALOG
    if cost_filter == 'free':
        certs = [c for c in certs if c['is_free']]
    elif cost_filter == 'paid':
        certs = [c for c in certs if not c['is_free']]

    if diff_filter != 'all':
        certs = [c for c in certs if diff_filter.lower() in c['difficulty'].lower()]

    return render_template(
        'certifications.html',
        certifications=certs,
        cost_filter=cost_filter,
        diff_filter=diff_filter
    )

# -------------------------------------------------------------
# Cyber Copilot Chatbot Routes
# -------------------------------------------------------------

@app.route('/chatbot')
@login_required
def chatbot():
    user_id = session['user_id']
    profile = db.query_one("SELECT * FROM student_profiles WHERE user_id = %s", (user_id,))
    history = db.query_all("SELECT * FROM chat_history WHERE user_id = %s ORDER BY created_at ASC LIMIT 50", (user_id,))

    # Identify whether live AI or Demo mode is active
    ai_status = {
        "is_live_ai": bool(Config.GEMINI_API_KEY or Config.OPENAI_API_KEY),
        "engine": "Gemini 1.5 / OpenAI" if (Config.GEMINI_API_KEY or Config.OPENAI_API_KEY) else "Cyber Copilot Knowledge Base (Demo Mode)"
    }

    return render_template('chatbot.html', profile=profile, chat_history=history, ai_status=ai_status)

@app.route('/api/chat', methods=['POST'])
@login_required
def api_chat():
    user_id = session['user_id']
    data = request.get_json() or {}
    message = data.get('message', '').strip()

    if not message:
        return jsonify({"error": "Empty message"}), 400

    profile = db.query_one("SELECT * FROM student_profiles WHERE user_id = %s", (user_id,))

    # Save user message
    db.execute(
        "INSERT INTO chat_history (user_id, sender, message, is_ai, mode) VALUES (%s, 'user', %s, 0, 'user')",
        (user_id, message)
    )

    # Get response from AI Engine (Live AI or clearly labeled Demo Mode)
    ai_result = ai_engine.ask_cyber_copilot(message, profile)

    # Save copilot response
    db.execute(
        "INSERT INTO chat_history (user_id, sender, message, is_ai, mode) VALUES (%s, 'copilot', %s, %s, %s)",
        (user_id, ai_result['response'], 1 if ai_result['is_ai'] else 0, ai_result['mode'])
    )

    return jsonify({
        "success": True,
        "response": ai_result['response'],
        "mode": ai_result['mode'],
        "is_ai": ai_result['is_ai'],
        "model": ai_result['model']
    })

@app.route('/api/clear-chat', methods=['POST'])
@login_required
def clear_chat():
    user_id = session['user_id']
    db.execute("DELETE FROM chat_history WHERE user_id = %s", (user_id,))
    return jsonify({"success": True, "message": "Chat history cleared."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Config.PORT, debug=Config.DEBUG)
