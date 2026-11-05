# AI Cybersecurity Career Copilot 🛡️

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-00FF9D?style=for-the-badge&logo=python&logoColor=0A0E0C)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask%203.1-00D67D?style=for-the-badge&logo=flask&logoColor=0A0E0C)](https://flask.palletsprojects.com/)
[![Database](https://img.shields.io/badge/Database-MySQL%20%7C%20SQLite-00FF9D?style=for-the-badge&logo=mysql&logoColor=0A0E0C)](https://www.mysql.com/)
[![Architecture](https://img.shields.io/badge/Architecture-Modular%20MVC-00D67D?style=for-the-badge)](#project-folder-structure)
[![Interface Theme](https://img.shields.io/badge/Theme-Matrix%20Obsidian%20%26%20Emerald-0A0E0C?style=for-the-badge&labelColor=00FF9D&color=0F1513)](#key-features)

> An intelligent, full-stack cybersecurity career mentorship and readiness platform engineered for college students and aspiring security analysts. Features dynamic career role matching, a 6-phase interactive milestone roadmap, 3-tier skill gap analysis, defensive hands-on projects, technical interview drills with instant feedback, and an integrated AI career mentor named **Cyber Copilot**.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Project Introduction](#2-project-introduction)
3. [Problem Statement](#3-problem-statement)
4. [Project Objectives](#4-project-objectives)
5. [Key Features](#5-key-features)
6. [AI Cybersecurity Career Guidance](#6-ai-cybersecurity-career-guidance)
7. [Technology Stack](#7-technology-stack)
8. [Project Folder Structure](#8-project-folder-structure)
9. [System Requirements](#9-system-requirements)
10. [Installation Instructions](#10-installation-instructions)
11. [Database Configuration (MySQL and SQLite fallback)](#11-database-configuration-mysql-and-sqlite-fallback)
12. [Environment Variables Setup](#12-environment-variables-setup)
13. [How to Run the Project](#13-how-to-run-the-project)
14. [Login and Registration Process](#14-login-and-registration-process)
15. [Application Modules](#15-application-modules)
16. [Screenshots Section](#16-screenshots-section)
17. [Future Enhancements](#17-future-enhancements)
18. [Conclusion](#18-conclusion)

---

## 1. Project Overview

**AI Cybersecurity Career Copilot** is a specialized web-based career navigation ecosystem tailored to computer science and cybersecurity students. The platform bridges the gap between academic classroom theory and industry-grade cybersecurity competencies. 

By analyzing an individual student's programming capabilities, networking foundations, operating system familiarity, and weekly availability, the platform calculates empirical readiness scores across **8 industry cybersecurity roles**. It produces personalized, phase-by-phase learning pathways, defensive hands-on project blueprints, multiple-choice technical interview simulations, and conversational AI guidance.

---

## 2. Project Introduction

Entering the cybersecurity domain is notoriously daunting for undergraduates. Unlike traditional software engineering, cybersecurity spans a vast spectrum ranging from low-level network packet analysis and binary exploitation to cloud governance, identity access management (IAM), and incident response triage.

Students frequently struggle with:
- Deciding which sub-discipline aligns with their technical strengths (e.g., Offensive Red Teaming vs. Defensive Blue Teaming vs. Cloud Security).
- Identifying their personal technical blind spots before applying for internships and entry-level positions.
- Finding structured, authorized, and defensive hands-on labs without inadvertently violating cyber ethics.

**AI Cybersecurity Career Copilot** serves as an always-available virtual mentor. It equips students with transparent role requirements, interactive task checklists, simulated technical interview questions with deep technical rationales, and an interactive conversational copilot that operates seamlessly in both online LLM inference mode and offline expert knowledge-base mode.

---

## 3. Problem Statement

1. **Information Overload and Fragmentation:** Aspiring students are bombarded with disjointed tutorials, expensive certification roadmaps, and fragmented forums without a cohesive, step-by-step curriculum tailored to their current knowledge level.
2. **Ambiguity Around Industry Roles:** Job descriptions for titles such as *SOC Analyst*, *Penetration Tester*, and *Application Security Engineer* often list overlapping or unrealistic requirements, leaving students confused about what skills are truly essential for entry-level hiring.
3. **Absence of Practical Readiness Benchmarks:** Students often learn theoretical concepts without knowing whether they can actually triage a security event, write an access control rule, or dissect a network packet stream.
4. **Safety & Ethical Boundaries:** Students often lack clear guidance on how to practice cybersecurity techniques legally and defensively using sandboxed environments, leading to uncertainty or improper testing practices.

---

## 4. Project Objectives

- **Demystify Cybersecurity Roles:** Provide concrete, transparent skill profiles, toolkits, and certification paths for 8 recognized cybersecurity specializations.
- **Empirically Measure Skill Gaps:** Categorize student competencies into *Possessed*, *Needs Improvement*, and *Missing Foundation* to compute an actionable **Role Readiness Index (%)**.
- **Deliver Adaptive Learning Roadmaps:** Generate a 6-phase modular syllabus with milestone tracking, allowing students to check off tasks in real-time.
- **Cultivate Defense-First Practical Skills:** Offer 9 defensive cybersecurity project blueprints across Beginner, Intermediate, and Advanced tiers with clear objectives, prerequisites, and milestone guides.
- **Sharpen Interview Acumen:** Provide category-filtered technical interview quizzes with real-time scoring, percentage metrics, and in-depth explanations for every option.
- **Ensure Academic Transparency in AI:** Deliver conversational mentorship through **Cyber Copilot**, offering dual-mode intelligence with explicit labeling between live generative AI and offline curated cybersecurity expert guidance.

---

## 5. Key Features

- **🔐 Cryptographically Secure Authentication:** User registration and login utilizing PBKDF2 with SHA-256 password hashing via Werkzeug, complete data isolation between student accounts, and multi-session persistence across browser refreshes.
- **🛡️ Secure Session & Back-Button Protection:** Hardened session lifecycle management featuring server-side anti-caching HTTP headers (`Cache-Control: no-cache, no-store, must-revalidate`), automatic Back-Forward Cache (bfcache) busting, and three prominent Logout access points.
- **👤 Dynamic Student Profile System:** Collects qualifications, departments, academic years, multi-select programming languages, networking protocols, operating systems, current cybersecurity experience tier, and weekly study time.
- **🎯 8-Track AI Career Matcher:** Compares student profiles against industry skill taxonomies to calculate dynamic match percentages and instant career recommendations.
- **📊 3-Tier Skill Gap Analyzer:** Dissects requirements into *Possessed Competencies*, *Needs Practical Improvement*, and *Missing Foundational Knowledge*, complete with ranked learning priorities and recommended hands-on exercises.
- **🗺️ Interactive 6-Phase Learning Roadmap:** Modular curriculum featuring real-time asynchronous (AJAX) task toggling that dynamically updates overall completion percentages without reloading the page.
- **🚀 9 Hands-on Defensive Projects:** Real-world portfolio projects categorized into Beginner, Intermediate, and Advanced tiers with project status tracking (*Not Started*, *In Progress*, *Completed*).
- **💡 Technical Interview Simulator:** Multi-category technical quizzes (*Networking*, *Linux & OS*, *SOC Analysis*, *Ethical Hacking*, *Python Security*, *Scenario Defense*) with score tracking and in-depth question explanations.
- **📜 Industry Certification & Lab Directory:** Curated catalog of recognized credentials (CompTIA Security+, BTL1, eJPT, CySA+, OSCP, AWS Security Specialty, PortSwigger) with difficulty levels, prerequisites, and free/paid filters.
- **🤖 Cyber Copilot AI Chatbot:** Dual-engine career advisor that utilizes Google Gemini 1.5 or OpenAI GPT-4o-mini when configured, with a built-in offline cybersecurity expert knowledge base in demo mode.
- **🎨 Matrix Obsidian & Electric Emerald Theme:** High-contrast cybersecurity command center aesthetic (`#0A0E0C` obsidian background, `#141C18` card surfaces, and `#00FF9D` electric emerald accents) designed for low eye strain and high readability.
- **⚡ Dual-Engine Database Architecture:** Native support for MySQL 8.0 with automatic zero-configuration fallback to local SQLite (`cyber_career_copilot.db`), ensuring immediate out-of-the-box evaluation.

---

## 6. AI Cybersecurity Career Guidance

The application evaluates student technical profiles against **8 distinct cybersecurity career trajectories**:

| Career Track | Focus Area | Key Tools & Technologies | Primary Certifications |
| :--- | :--- | :--- | :--- |
| **SOC Analyst** | Threat monitoring, SIEM alert triage, log auditing, incident detection | Splunk, Elastic Security, Wireshark, Suricata, Wazuh, VirusTotal | CompTIA Security+, BTL1, CySA+ |
| **Ethical Hacker** | Authorized offensive probing, vulnerability assessments, exploit research | Kali Linux, Burp Suite, Nmap, Metasploit, Wireshark, Hydra | eJPT, CompTIA Security+, CEH |
| **Penetration Tester** | Network exploitation, web application security (OWASP Top 10), privilege escalation | Kali Linux, Burp Suite Pro, Nmap, ffuf, Impacket, BloodHound | eJPT, OSCP, CompTIA PenTest+ |
| **Cybersecurity Analyst** | Risk assessment, compliance (NIST CSF, ISO 27001), vulnerability management | Nessus, Qualys, Wireshark, Microsoft Defender, Nmap | CompTIA Security+, Network+, SSCP |
| **Digital Forensics Analyst** | Memory acquisition, disk forensics, file system reconstruction, chain of custody | Autopsy, Volatility 3, FTK Imager, Eric Zimmerman Tools | CHFI, GCFA, BTL1 |
| **Cloud Security Engineer** | Cloud posture, IAM least privilege, container security, IaC audits | AWS GuardDuty, Terraform, Trivy, Prowler, Docker, ScoutSuite | AWS Security - Specialty, AZ-500, Security+ |
| **Application Security Engineer** | DevSecOps pipelines, SAST/DAST scanning, secure code review, API security | SonarQube, Snyk, Semgrep, OWASP ZAP, GitHub CodeQL | CSSLP, CASE, CompTIA Security+ |
| **Incident Response Analyst** | Host containment, malware triage, root-cause analysis, disaster recovery | Velociraptor, Wireshark, YARA, Sysinternals Suite, Ghidra | GCIH, BTL1, CompTIA CySA+ |

### Match Scoring Algorithm & Skill Taxonomy

The AI engine utilizes a multi-dimensional matching heuristic:
1. **Skill Taxonomy Normalization:** Normalizes language keywords (`Python`, `Bash`, `PowerShell`, `SQL`, `C`), networking keywords (`TCP/IP`, `Wireshark`, `DNS`, `Firewalls`), and operating system terms (`Linux`, `Windows Server`, `Kali Linux`).
2. **Weighted Alignment Scoring:** Cross-references the student's possessed profile terms against the career's mandatory skill profile.
3. **Experience Calibration:** Applies weight adjustments based on the student's declared experience level (*Beginner*, *Intermediate*, *Advanced*), providing an honest match percentage (25%–95%).
4. **Skill Gap Breakdown:**
   - **Possessed:** Direct matches between student skills and career prerequisites.
   - **Needs Improvement:** Foundational concepts known theoretically but requiring practical lab experience.
   - **Missing Foundation:** Prerequisite competencies not yet indicated in the student's profile.

---

## 7. Technology Stack

### Backend
- **Python 3.10+**: Core programming language.
- **Flask 3.1.3**: Micro-framework handling HTTP routing, session management, and template rendering.
- **Werkzeug 3.1.9**: Cryptographic hashing (`generate_password_hash`, `check_password_hash`) and WSGI helpers.
- **python-dotenv 1.2.4**: Secure environment configuration loader.
- **Requests 2.34.2**: Client for external AI API communication (Gemini / OpenAI).

### Frontend
- **HTML5**: Semantic web architecture with accessible ARIA landmarks.
- **Vanilla CSS3**: Custom design system featuring CSS variables, grid systems, responsive flexbox layouts, micro-animations, and the custom **Matrix Obsidian & Electric Emerald** palette.
- **JavaScript (ES6+)**: Asynchronous (Fetch/AJAX) task toggling, dynamic UI filtering, modal controllers, and Back-Forward Cache (bfcache) management.
- **Chart.js 4.4.1**: Interactive radial radar chart rendering competency breakdowns in the student command center.

### Database Layer
- **MySQL 8.0**: Production relational database engine using `PyMySQL 1.2.3`.
- **SQLite 3**: Automated embedded database fallback (`cyber_career_copilot.db`) for immediate local operation without external database server configuration.

---

## 8. Project Folder Structure

```
cyber-career-copilot/
├── app.py                      # Core Flask application, routing controllers & security middleware
├── config.py                   # Centralized application and session configuration
├── database.py                 # Dual-engine database abstraction (MySQL + SQLite fallback)
├── ai_engine.py                # AI career matching, skill gap analysis & dual-mode chatbot engine
├── data_seed.py                # Pre-seeded catalog of careers, 9 projects, certs & quiz questions
├── schema.sql                  # MySQL schema definition with relational constraints & indexes
├── requirements.txt            # Declared Python project dependencies
├── .env.example                # Template for environment variables
├── .env                        # Local active environment configuration (excluded from git)
├── cyber_career_copilot.db     # SQLite local database (generated on startup)
├── README.md                   # Comprehensive project documentation
├── static/
│   ├── css/
│   │   └── style.css           # Matrix Obsidian & Electric Emerald theme stylesheet
│   ├── js/
│   │   └── app.js              # Client-side DOM manipulation, AJAX handlers & bfcache buster
│   └── images/
│       └── logo.svg            # Vector Cyber Copilot emblem and typography
├── templates/
│   ├── base.html               # Base layout with sidebar navigation, header, and logout buttons
│   ├── login.html              # Cyber-themed student authentication portal
│   ├── register.html           # New student account registration portal
│   ├── dashboard.html          # Student command center with metrics, radar chart & action buttons
│   ├── profile.html            # Profile editor for skills, academic details & career goals
│   ├── careers.html            # AI Career Advisor catalog with match scores & blueprint modals
│   ├── skill_gap.html          # 3-tier competency gap analysis & lab exercise recommendations
│   ├── roadmap.html            # 6-phase learning roadmap with interactive milestone toggles
│   ├── projects.html           # 9 defensive cybersecurity project blueprints with status tracking
│   ├── interview.html          # Technical interview simulator with category-filtered questions
│   ├── interview_results.html  # Interactive test evaluation with in-depth question explanations
│   ├── certifications.html     # Industry certifications and verified lab directory
│   └── chatbot.html            # Cyber Copilot interactive conversational AI interface
└── tests/
    └── test_copilot.py         # Automated test suite covering auth, roadmap, quizzes, and session
```

---

## 9. System Requirements

- **Operating System:** Windows 10/11, macOS 12+, or modern Linux distribution (Ubuntu 20.04+, Debian 11+, Fedora 38+).
- **Python:** Version `3.10` or higher (`python --version`).
- **Memory (RAM):** Minimum 2 GB (4 GB recommended).
- **Disk Space:** 500 MB free space for repository, virtual environment, and database storage.
- **Web Browser:** Google Chrome, Microsoft Edge, Mozilla Firefox, Brave, or Safari with JavaScript enabled.
- **Database Server (Optional):** MySQL Server 8.0 (only required if not using the automated SQLite fallback).

---

## 10. Installation Instructions

### Step 1: Open the Project Directory
Open your terminal or PowerShell and navigate to the project directory:
```bash
cd cyber-career-copilot
```

### Step 2: Set Up Python Virtual Environment

#### On Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

> *Tip: If script execution is restricted on Windows, allow execution for the current session:*
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
> .\venv\Scripts\Activate.ps1
> ```

#### On Linux / macOS (Bash / Zsh):
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Dependencies
With the virtual environment active, install all required packages:
```bash
pip install -r requirements.txt
```

---

## 11. Database Configuration (MySQL and SQLite fallback)

The platform implements an automated dual-engine database layer in [`database.py`](file:///c:/Users/Admin/Desktop/cyber-career-copilot/database.py). You can choose either setup:

### Option A: Zero-Configuration SQLite Fallback (Default & Recommended for Evaluation)
No database server installation or setup is needed:
1. Ensure `USE_SQLITE_FALLBACK=True` is set in your `.env` file.
2. When the application boots, it automatically detects whether MySQL is reachable.
3. If MySQL is offline, it instantly creates and seeds the local SQLite database file (`cyber_career_copilot.db`).
4. All application features, relationships, and student data work identically.

### Option B: MySQL Database Server 8.0
If you prefer running against a dedicated MySQL instance:
1. Start your local MySQL service.
2. Initialize the database and table schemas using `schema.sql`:
   ```bash
   mysql -u root -p < schema.sql
   ```
3. Update `.env` with your local MySQL credentials:
   ```ini
   MYSQL_HOST=localhost
   MYSQL_PORT=3306
   MYSQL_USER=root
   MYSQL_PASSWORD=your_actual_mysql_password
   MYSQL_DB=cyber_career_copilot
   USE_SQLITE_FALLBACK=True
   ```
4. On startup, the application connects to MySQL, confirms the database schema, and seeds standard catalogs if empty.

---

## 12. Environment Variables Setup

Configuration settings are managed through a `.env` file located in the root directory. Copy the provided `.env.example` template:

```bash
# Windows PowerShell:
Copy-Item .env.example .env

# Linux / macOS:
cp .env.example .env
```

### Configuration Variables Guide

```ini
# Flask Core Configuration
SECRET_KEY=cyber_copilot_super_secret_dev_key_2026_secure
FLASK_ENV=development
PORT=5000

# Database Configuration (MySQL)
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=cyber_career_copilot
USE_SQLITE_FALLBACK=True

# AI API Key (Optional)
# If left empty, Cyber Copilot operates seamlessly in Intelligent Demo Mode
GEMINI_API_KEY=
OPENAI_API_KEY=
```

> **Security Note:** Never commit your production `.env` file containing sensitive credentials or live API keys to public repositories.

---

## 13. How to Run the Project

### 1. Launch the Application
Execute `app.py` within your activated virtual environment:

```powershell
# Windows:
.\venv\Scripts\python.exe app.py

# Linux / macOS:
python app.py
```

Upon launching, the console displays database initialization output:
```
[DB] Initializing database layer...
[DB Warning] Using local SQLite fallback database.
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### 2. Access the Application
Open your web browser and navigate to:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

### 3. Run Automated Unit Tests
To verify all authentication flows, session handling, database queries, and quiz calculations:

```powershell
# Windows:
.\venv\Scripts\python.exe -m unittest -v tests/test_copilot.py

# Linux / macOS:
python -m unittest -v tests/test_copilot.py
```

---

## 14. Login and Registration Process

### 1. Student Registration (`/register`)
- **Fields Required:** Full Name, University/Student Email Address, Password, and Password Confirmation.
- **Client & Server Validation:** Ensures passwords match and fields are non-empty.
- **Password Security:** Hashes passwords using `werkzeug.security.generate_password_hash` with PBKDF2:SHA-256 and unique salt iterations.
- **Automatic Profile Provisioning:** Generates an initial linked student profile and automatically starts a secure session, directing the student to the profile setup wizard.

### 2. Student Sign In (`/login`)
- Authenticates email and password against stored cryptographic hashes.
- Updates the `last_login` timestamp in the database.
- Marks `session.permanent = True` with a 7-day expiration lifetime (`PERMANENT_SESSION_LIFETIME = timedelta(days=7)`).
- Sets `session['user_id']` and `session['user_name']`.
- Redirects to the student's personalized Command Center Dashboard (`/dashboard`).

### 3. Session Persistence & Security
- **Browser Refresh Persistence:** Sessions remain active across page reloads and browser tab closures without prompting for re-login.
- **Back-Button Exposure Prevention:** Protected routes automatically send anti-caching HTTP response headers (`Cache-Control: no-cache, no-store, must-revalidate`). If a user logs out and clicks the browser's Back button, client-side lifecycle listeners (`pageshow` / bfcache detection) force an immediate reload that redirects to `/login`.
- **Visible Sign Out:** Logout buttons are clearly visible in the **Dashboard Hero Banner**, **Top App Bar**, and **Sidebar Footer**.
- **Complete Session Clearance (`/logout`):** Destroys all server-side session dictionaries via `session.clear()`, removes client-side session cookies via `delete_cookie`, and redirects to `/login`.

---

## 15. Application Modules

### 1. Dashboard & Command Center (`/dashboard`)
The central operations hub for the authenticated student:
- **Active Career Hero Banner:** Displays current role track, specialization ID, student academic details, and immediate action buttons (*Analyze Skill Gap*, *Change Career Goal*, *Logout*).
- **4 Key Performance Indicators (KPIs):** Real-time metrics for Roadmap Progress (%), Role Readiness Score (%), Completed Projects tally, and Practice Quiz Average (%).
- **Cyber Competency Radar Chart:** Interactive multi-axis visualization powered by Chart.js displaying comparative readiness across Network Defense, Linux/OS, Web Security, Python Automation, Threat Triage, and Cloud Security.
- **Active Milestone Action List:** Surfaces the next 4 pending tasks from the student's roadmap with direct toggle controls.
- **Recent Quiz History:** Shows recent scores, percentages, and performance badges (*Pass*, *Warning*, *Review*).

### 2. Student Profile Management (`/profile`)
Enables students to manage their academic context and technical foundation:
- Academic metadata: Degree qualification, academic department, and current year of study.
- Multi-select competency checkboxes for **Programming Languages** (Python, C, C++, Java, Bash, PowerShell, JavaScript, SQL, Go, Rust).
- Multi-select competency checkboxes for **Networking Skills** (TCP/IP, Wireshark, DNS/DHCP, Firewalls, Routing/Switching, VPNs).
- Multi-select competency checkboxes for **Operating Systems** (Linux, Windows Server, Kali Linux, macOS).
- Declared experience level (*Beginner*, *Intermediate*, *Advanced*) and preferred career target.
- Weekly available study time allocator (hours/week) to calibrate milestone timelines.

### 3. AI Career Advisor (`/careers`)
The discovery portal presenting all 8 cybersecurity roles:
- Individual role cards displaying calculated match percentage (0%–100%) based on the student's profile.
- Technical role summary, required skill sets, and industry toolkits.
- **"Set as My Career Target"** action button that recalibrates the student's roadmap and dashboard.
- **"View Career Blueprint" Modal:** Detailed modal breakdown showing recommended entry-level certifications, verified beginner resources, practical projects, and immediate next steps.

### 4. AI Skill Gap Analyzer (`/skill-gap`)
Provides a comprehensive technical readiness assessment for the selected career:
- **Role Readiness Index:** Percentage score benchmarked against industry role requirements.
- **3-Tier Categorization Cards:**
  1. *Possessed Competencies:* Skills already verified in the student's profile.
  2. *Needs Practical Improvement:* Areas where the student has foundational knowledge but requires hands-on lab practice.
  3. *Missing Foundational Knowledge:* Core prerequisites not yet demonstrated.
- **Ranked Learning Priorities:** Actionable, prioritized action items to close the technical gap.
- **Guided Lab Exercises:** Practical exercises with duration estimates and specific skills targeted.

### 5. Learning Roadmap Tracker (`/roadmap`)
A comprehensive 6-phase curriculum tailored to the student's career target:
- **Phase 1:** Networking and Computer Fundamentals
- **Phase 2:** Linux, Windows, and Python Basics
- **Phase 3:** Cybersecurity Fundamentals (CIA Triad, Threats, Cryptography)
- **Phase 4:** Specialized Tools & Technical Skills for the Chosen Career
- **Phase 5:** Hands-on Projects and Practical Labs
- **Phase 6:** Certifications and Interview Preparation
- **Real-Time Milestone Toggles:** Checkboxes make asynchronous `POST /api/toggle-task` requests, saving completion state and updating overall progress instantly without page reloads.

### 6. Hands-on Defensive Projects Portfolio (`/projects`)
A directory of 9 defense-oriented, authorized cybersecurity project specifications:
- Organized into **Beginner**, **Intermediate**, and **Advanced** difficulty tiers.
- Filterable navigation to view projects by specific difficulty level.
- Each project card details: Technical Objective, Prerequisites, Tech Stack, Step-by-Step Milestones, and Practical Learning Outcomes.
- Dynamic status tracking allowing students to mark projects as *Not Started*, *In Progress*, or *Completed*.

### 7. Technical Interview Simulator & Quizzes (`/interview`)
An interactive quiz system testing technical knowledge:
- Category filters: *Networking*, *Linux & OS*, *SOC Analysis*, *Ethical Hacking*, *Python Security*, and *Scenario Defense*.
- Multiple-choice questions with scenario contexts and technical options.
- **Immediate Evaluation (`/interview_results.html`):** Computes score, percentage, and provides comprehensive technical explanations for why the correct answer is right and why distractors are incorrect.
- Persistent attempt history tracked in the database.

### 8. Industry Certifications Directory (`/certifications`)
A reference guide to globally recognized cybersecurity credentials:
- Catalog covering CompTIA Security+, Network+, eJPT, BTL1, CySA+, OSCP, AWS Certified Security, and PortSwigger Web Security.
- Filterable by difficulty tier (*Beginner*, *Intermediate*, *Advanced*) and cost (*Free* vs. *Paid*).
- Outlines skills tested, target audience, recommended prerequisites, and direct links to official examination portals.

### 9. Cyber Copilot AI Chatbot (`/chatbot`)
An interactive chat interface for personalized cybersecurity guidance:
- **Live AI Mode:** Connects to Google Gemini 1.5 Flash or OpenAI GPT-4o-mini when an API key is provided in `.env`.
- **Intelligent Demo Mode:** Operates on an offline curated knowledge base when no API key is configured. Explicitly labeled with `[DEMO MODE: Predefined Expert Cybersecurity Guidance]` for academic honesty.
- Includes quick-prompt suggestion chips (*"How do I become a SOC Analyst?"*, *"Explain the TCP 3-way handshake"*, *"What projects should I put on my resume?"*, *"Top beginner certifications"*).
- Clear conversation history button (`POST /api/clear-chat`) to reset dialogue.

---

## 16. Screenshots Section

> *Place application screenshots in a `docs/screenshots/` directory for visual reference on GitHub.*

| Screen | Description | Expected Screenshot Path |
| :--- | :--- | :--- |
| **Authentication Portal** | Modern Matrix Obsidian & Electric Emerald login interface with security trust badge. | `docs/screenshots/01_login.png` |
| **Command Center Dashboard** | Main student overview with active career banner, KPI cards, radar chart, and action buttons. | `docs/screenshots/02_dashboard.png` |
| **Student Profile Editor** | Academic and technical skills configuration with multi-select checkboxes. | `docs/screenshots/03_profile.png` |
| **AI Career Advisor** | Grid of 8 cybersecurity role cards with dynamic match percentages and blueprint modals. | `docs/screenshots/04_careers.png` |
| **Skill Gap Analyzer** | 3-tier competency breakdown (*Possessed*, *Improvement*, *Missing*) and lab exercises. | `docs/screenshots/05_skill_gap.png` |
| **Learning Roadmap** | 6-phase curriculum with interactive AJAX task checkboxes and progress tracking. | `docs/screenshots/06_roadmap.png` |
| **Hands-on Projects** | 9 defensive cybersecurity project blueprints categorized by difficulty level. | `docs/screenshots/07_projects.png` |
| **Interview Simulator** | Category-filtered technical questions with scenario contexts and instant explanations. | `docs/screenshots/08_interview.png` |
| **Cyber Copilot Chatbot** | Conversational career advisor showing transparent dual-mode intelligence. | `docs/screenshots/09_chatbot.png` |
| **Certifications Directory** | Industry credentials catalog with difficulty and cost filters. | `docs/screenshots/10_certifications.png` |

---

## 17. Future Enhancements

The following roadmap outlines planned enhancements for upcoming iterations of the platform:

1. **Docker & Containerized Setup:** Provide a `Dockerfile` and `docker-compose.yml` to package Flask, MySQL, and Nginx into a single containerized setup.
2. **Automated Resume / CV Parser:** Enable students to upload PDF/DOCX resumes and automatically extract technical skills into their profile using NLP.
3. **Interactive Terminal Labs:** Embed in-browser sandboxed terminal exercises (via WebAssembly or xterm.js) for practicing basic Linux commands and network analysis.
4. **Study Streak & Discord/Slack Integrations:** Webhook notifications to celebrate milestone completions and maintain consistent study habits.
5. **University SSO Integration:** Support for Google Workspace for Education and Microsoft 365 OAuth2 for seamless institutional login.

---

## 18. Conclusion

**AI Cybersecurity Career Copilot** offers a structured, defense-first, and transparent platform to empower the next generation of cybersecurity defenders. By replacing fragmented learning with measurable skill benchmarks, guided project portfolios, structured roadmaps, and honest AI-driven mentorship, the platform equips college students with the practical skills and confidence needed to enter the cybersecurity workforce.

---

### 🛡️ Ethical Use & Defensive Learning Notice
*All project concepts, code samples, and lab exercises provided in this platform are designed strictly for authorized, defensive education in sandboxed environments (such as local VirtualBox networks, TryHackMe, PortSwigger Web Security Academy, and OverTheWire). Unauthorized penetration testing or scanning against external systems without prior written authorization is strictly prohibited by law.*
