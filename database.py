import sqlite3
import pymysql
import os
import re
import json
from config import Config
from data_seed import QUIZ_QUESTIONS_SEED, PROJECTS_CATALOG

ACTIVE_DB_ENGINE = "SQLite"
DB_STATUS_MESSAGE = "Initializing database..."

def get_mysql_connection(include_db=True):
    return pymysql.connect(
        host=Config.MYSQL_HOST,
        port=Config.MYSQL_PORT,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB if include_db else None,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
        connect_timeout=2
    )

def get_sqlite_connection():
    conn = sqlite3.connect(Config.SQLITE_DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn

def test_mysql_available():
    try:
        conn = get_mysql_connection(include_db=False)
        conn.close()
        return True
    except Exception as e:
        return False

def init_db():
    global ACTIVE_DB_ENGINE, DB_STATUS_MESSAGE
    print("[DB] Initializing database layer...")

    # Attempt MySQL first
    if test_mysql_available():
        try:
            print("[DB] Connecting to MySQL server...")
            server_conn = get_mysql_connection(include_db=False)
            with server_conn.cursor() as cur:
                cur.execute(f"CREATE DATABASE IF NOT EXISTS `{Config.MYSQL_DB}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
            server_conn.close()

            # Now run schema in the database
            db_conn = get_mysql_connection(include_db=True)
            schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
            if os.path.exists(schema_path):
                with open(schema_path, 'r', encoding='utf-8') as f:
                    schema_sql = f.read()
                
                # Split and execute statements
                statements = [s.strip() for s in schema_sql.split(';') if s.strip() and not s.strip().startswith('--')]
                with db_conn.cursor() as cur:
                    for stmt in statements:
                        if stmt.upper().startswith("CREATE DATABASE") or stmt.upper().startswith("USE "):
                            continue
                        cur.execute(stmt)

            ACTIVE_DB_ENGINE = "MySQL"
            DB_STATUS_MESSAGE = f"Connected to MySQL 8.0 (`{Config.MYSQL_DB}`)"
            print(f"[DB] {DB_STATUS_MESSAGE}")
            db_conn.close()
            seed_initial_data()
            return
        except Exception as e:
            print(f"[DB] MySQL initialization error: {e}")
            if not Config.USE_SQLITE_FALLBACK:
                raise e

    # Fallback to SQLite if MySQL fails or fallback is enabled
    print("[DB Warning] Using local SQLite fallback database.")
    ACTIVE_DB_ENGINE = "SQLite"
    DB_STATUS_MESSAGE = "Running on local SQLite engine (MySQL fallback active)"
    init_sqlite()
    seed_initial_data()

def init_sqlite():
    conn = get_sqlite_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        full_name TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_login TIMESTAMP NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS student_profiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL UNIQUE,
        qualification TEXT DEFAULT '',
        department TEXT DEFAULT '',
        year_of_study TEXT DEFAULT '',
        programming_languages TEXT DEFAULT '',
        networking_skills TEXT DEFAULT '',
        os_skills TEXT DEFAULT '',
        cyber_level TEXT DEFAULT 'Beginner',
        areas_of_interest TEXT DEFAULT '',
        preferred_career TEXT DEFAULT 'SOC Analyst',
        weekly_study_hours INTEGER DEFAULT 10,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS career_recommendations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        career_title TEXT NOT NULL,
        match_percentage INTEGER DEFAULT 0,
        description TEXT,
        required_skills TEXT,
        tools_tech TEXT,
        beginner_resources TEXT,
        certifications TEXT,
        practical_projects TEXT,
        next_steps TEXT,
        is_ai_generated INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS skill_assessments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        career_title TEXT NOT NULL,
        possessed_skills TEXT,
        improvement_skills TEXT,
        missing_foundation TEXT,
        priority_learning TEXT,
        practical_exercises TEXT,
        readiness_score INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS learning_roadmaps (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        career_title TEXT NOT NULL,
        overall_progress INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS roadmap_tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roadmap_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        phase_number INTEGER NOT NULL,
        phase_title TEXT NOT NULL,
        task_title TEXT NOT NULL,
        description TEXT,
        resource_url TEXT DEFAULT '',
        is_completed INTEGER DEFAULT 0,
        completed_at TIMESTAMP NULL,
        sort_order INTEGER DEFAULT 0,
        FOREIGN KEY (roadmap_id) REFERENCES learning_roadmaps(id) ON DELETE CASCADE,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NULL,
        title TEXT NOT NULL,
        difficulty_level TEXT NOT NULL,
        objective TEXT NOT NULL,
        prerequisites TEXT,
        tech_stack TEXT,
        milestones TEXT,
        learning_outcomes TEXT,
        status TEXT DEFAULT 'Not Started',
        is_custom INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS quiz_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        career_tag TEXT DEFAULT 'All',
        difficulty TEXT DEFAULT 'Intermediate',
        question_text TEXT NOT NULL,
        option_a TEXT NOT NULL,
        option_b TEXT NOT NULL,
        option_c TEXT NOT NULL,
        option_d TEXT NOT NULL,
        correct_option TEXT NOT NULL,
        explanation TEXT NOT NULL,
        scenario_context TEXT
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS quiz_attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        category TEXT NOT NULL,
        score INTEGER NOT NULL,
        total_questions INTEGER NOT NULL,
        percentage REAL NOT NULL,
        details_json TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        sender TEXT NOT NULL,
        message TEXT NOT NULL,
        is_ai INTEGER DEFAULT 0,
        mode TEXT DEFAULT 'demo',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    conn.commit()
    conn.close()

def seed_initial_data():
    # Seed quiz questions if empty
    questions_count = query_one("SELECT COUNT(*) as count FROM quiz_questions")
    if not questions_count or questions_count.get('count', 0) == 0:
        print(f"[DB] Seeding {len(QUIZ_QUESTIONS_SEED)} quiz questions...")
        for q in QUIZ_QUESTIONS_SEED:
            execute("""
                INSERT INTO quiz_questions 
                (category, career_tag, difficulty, question_text, option_a, option_b, option_c, option_d, correct_option, explanation, scenario_context)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                q['category'], q['career_tag'], q['difficulty'], q['question_text'],
                q['option_a'], q['option_b'], q['option_c'], q['option_d'],
                q['correct_option'], q['explanation'], q['scenario_context']
            ))

    # Seed public project catalog templates if empty
    projects_count = query_one("SELECT COUNT(*) as count FROM projects WHERE user_id IS NULL")
    if not projects_count or projects_count.get('count', 0) == 0:
        print(f"[DB] Seeding {len(PROJECTS_CATALOG)} project templates...")
        for p in PROJECTS_CATALOG:
            execute("""
                INSERT INTO projects 
                (user_id, title, difficulty_level, objective, prerequisites, tech_stack, milestones, learning_outcomes, status, is_custom)
                VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, 'Not Started', 0)
            """, (
                p['title'], p['difficulty_level'], p['objective'], p['prerequisites'],
                p['tech_stack'], p['milestones'], p['learning_outcomes']
            ))

def format_query(sql):
    """Translate %s to ? if using SQLite engine."""
    if ACTIVE_DB_ENGINE == "SQLite":
        return sql.replace('%s', '?')
    return sql

def query_all(sql, params=()):
    sql = format_query(sql)
    if ACTIVE_DB_ENGINE == "MySQL":
        conn = get_mysql_connection(include_db=True)
        try:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                return cur.fetchall()
        finally:
            conn.close()
    else:
        conn = get_sqlite_connection()
        try:
            cur = conn.cursor()
            cur.execute(sql, params)
            rows = cur.fetchall()
            return [dict(r) for r in rows]
        finally:
            conn.close()

def query_one(sql, params=()):
    sql = format_query(sql)
    if ACTIVE_DB_ENGINE == "MySQL":
        conn = get_mysql_connection(include_db=True)
        try:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                return cur.fetchone()
        finally:
            conn.close()
    else:
        conn = get_sqlite_connection()
        try:
            cur = conn.cursor()
            cur.execute(sql, params)
            row = cur.fetchone()
            return dict(row) if row else None
        finally:
            conn.close()

def execute(sql, params=()):
    sql = format_query(sql)
    if ACTIVE_DB_ENGINE == "MySQL":
        conn = get_mysql_connection(include_db=True)
        try:
            with conn.cursor() as cur:
                cur.execute(sql, params)
                conn.commit()
                return cur.lastrowid
        finally:
            conn.close()
    else:
        conn = get_sqlite_connection()
        try:
            cur = conn.cursor()
            cur.execute(sql, params)
            conn.commit()
            return cur.lastrowid
        finally:
            conn.close()
