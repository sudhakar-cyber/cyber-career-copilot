# AI Cybersecurity Career Copilot 🛡️

**AI Cybersecurity Career Copilot** is a modern, full-stack web application designed for college students aspiring to build careers in cybersecurity. It features a dark navy and electric blue high-tech cybersecurity interface, personalized AI guidance, a 6-phase learning roadmap, a skill gap analyzer, defensive hands-on projects, technical interview preparation with instant explanations, and an AI career mentor named **Cyber Copilot**.

---

## 🌟 Key Features

### 1. 🔐 Secure Student Authentication & Isolation
- Student registration, secure login, and session termination.
- Passwords cryptographically hashed using PBKDF2 with SHA-256 via Werkzeug.
- Strict data isolation: students only access their personal profile, progress, quiz history, and chat logs.

### 2. 👤 Comprehensive Student Profile
- Academic details: qualification, department, year of study.
- Known programming languages (Python, C, C++, Java, Bash, PowerShell, JavaScript, SQL, Go, Rust).
- Networking competencies (TCP/IP, Wireshark, DNS/DHCP, Firewalls, Routing/Switching, VPNs).
- Operating system skills (Linux, Windows Server, Kali Linux, macOS).
- Experience levels (Beginner, Intermediate, Advanced) and specific cybersecurity interests.
- Weekly available study time calibration.

### 3. 🎯 AI Cybersecurity Career Advisor
Evaluates student background against 8 specialized cybersecurity career paths:
1. **Ethical Hacker**
2. **SOC Analyst**
3. **Penetration Tester**
4. **Cybersecurity Analyst**
5. **Digital Forensics Analyst**
6. **Cloud Security Engineer**
7. **Application Security Engineer (AppSec)**
8. **Incident Response Analyst**

Each recommendation includes dynamic match scoring (0-100%), required technical skills, important tools, verified beginner-friendly resources, recognized certifications, practical projects, and immediate next steps.

### 4. 📊 AI Skill Gap Analyzer
- Evaluates competencies against the chosen target career.
- 3-tier categorization:
  - **Possessed Competencies** (verified skills matching the career)
  - **Needs Practical Improvement** (intermediate/theoretical knowledge requiring labs)
  - **Missing Foundational Knowledge** (unaddressed requirements)
- Generates a **Role Readiness Index (%)**, ranked learning priorities, and guided hands-on lab exercises with estimated completion hours.

### 5. 🗺️ Personalized 6-Phase Learning Roadmap
Structured modular syllabus customized to the student's career track:
- **Phase 1:** Networking and Computer Fundamentals
- **Phase 2:** Linux, Windows, and Python Basics
- **Phase 3:** Cybersecurity Fundamentals (CIA Triad, Threats, Cryptography)
- **Phase 4:** Specialized Tools & Technical Skills for the Chosen Career
- **Phase 5:** Hands-on Projects and Practical Labs
- **Phase 6:** Certifications and Technical Interview Preparation

Interactive AJAX checkboxes allow students to mark milestones completed in real-time, recalculating overall progress without page refreshes.

### 6. 🚀 Hands-on Projects Portfolio (3 Difficulty Tiers)
All practical exercises adhere to authorized and defensive learning ethics:
- **Beginner:** Password Strength Checker, File Integrity Monitoring Tool, Basic Network Traffic Analyzer.
- **Intermediate:** Personal Firewall, Intrusion Detection System (IDS), Phishing URL Detection Tool.
- **Advanced:** Security Log Analysis Dashboard (SIEM), Cloud Security Monitoring Tool, ML-Based Anomaly Detection System.
- Tracks project progress status (*Not Started*, *In Progress*, *Completed*).

### 7. 💡 Technical Interview Simulator & Quizzes
- Category filters: *Networking*, *Linux & OS*, *SOC Analysis*, *Ethical Hacking*, *Python Security*, *Scenario Defense*.
- Interactive multiple-choice quizzes with real-time scoring.
- Comprehensive technical explanations for every question and option.
- Persistent attempt history with percentage tracking and historical progression.

### 8. 🤖 Cyber Copilot AI Chatbot (Dual-Mode)
- Integrated via Flask backend with secure credentials.
- **Live AI Mode:** Integrates Google Gemini or OpenAI API when configured in `.env`.
- **Intelligent Demo Mode:** When no API key is set, operates on an offline curated cybersecurity knowledge base. Features an explicit label: `[DEMO MODE: Predefined Expert Cybersecurity Guidance]` ensuring academic transparency.
- Quick suggestion chips for common queries (*SOC Analyst roadmap*, *TCP 3-way handshake*, *Resume projects*, *Top certifications*).

### 9. 📜 Certifications & Verified Learning Directory
- Database of industry credentials (CompTIA Security+, Network+, eJPT, BTL1, CySA+, OSCP, AWS Security Specialty, PortSwigger Certified Practitioner).
- Filters for difficulty level and free vs. paid resources with direct links to official examination portals.

### 10. 📈 Command Center Progress Dashboard
- Career target summary and profile status.
- Real-time metrics calculated from live database records.
- **Cyber Competency Radar Chart** powered by Chart.js.
- Upcoming milestone launcher and recommended next steps.

---

## 🛠️ Technology Stack

- **Frontend:** HTML5, Vanilla CSS3 (Custom Dark Navy Theme, Glassmorphism, Micro-animations), JavaScript (ES6+), Chart.js
- **Backend:** Python 3.10+ / Flask
- **Database:** MySQL 8.0 (primary) with PyMySQL, automated fallback to SQLite (`cyber_career_copilot.db`) for immediate out-of-the-box local testing.
- **Security:** Werkzeug password hashing, parameter-bound SQL queries, session encryption.

---

## 📁 Project Structure

```
cyber-career-copilot/
├── app.py                  # Main Flask application and REST routes
├── config.py               # Environment configuration loader
├── database.py             # Database abstraction layer (MySQL + SQLite fallback)
├── ai_engine.py            # AI matching, skill gap analysis & chatbot logic
├── data_seed.py            # Pre-seeded catalog of careers, questions, projects & certs
├── schema.sql              # MySQL schema creation script
├── requirements.txt        # Python dependency declarations
├── .env.example            # Environment template
├── .env                    # Local environment settings
├── static/
│   ├── css/
│   │   └── style.css       # Cybersecurity dark theme design system
│   ├── js/
│   │   └── app.js          # Interactive client logic and AJAX handlers
│   └── images/
│       └── logo.svg        # Cyber Copilot SVG emblem & typography
├── templates/
│   ├── base.html           # Base layout with sidebar navigation
│   ├── login.html          # Secure login portal
│   ├── register.html       # Student registration
│   ├── dashboard.html      # Command center with Chart.js radar
│   ├── profile.html        # Academic & skills profile editor
│   ├── careers.html        # AI career advisor cards & blueprint modals
│   ├── skill_gap.html      # 3-tier gap breakdown & readiness score
│   ├── roadmap.html        # 6-phase interactive milestone tracker
│   ├── projects.html       # 9 defensive cybersecurity projects
│   ├── interview.html      # Practice quiz simulator
│   ├── interview_results.html # Detailed technical feedback & review
│   ├── certifications.html # Verified certs directory
│   └── chatbot.html        # Cyber Copilot AI conversation interface
└── tests/
    └── test_copilot.py     # Automated unit test suite
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10 or higher
- MySQL Server 8.0 (Optional — application automatically initializes SQLite if MySQL is offline or credentials differ)

### 2. Installation
Clone the repository or open the project folder:
```bash
cd cyber-career-copilot
```

Create and activate a Python virtual environment:
```powershell
# Windows PowerShell:
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Database Configuration

#### Option A: Using MySQL (Recommended for evaluation)
1. Ensure your MySQL server is running (e.g. MySQL 8.0 service).
2. Create the database and tables using `schema.sql`:
```bash
mysql -u root -p < schema.sql
```
3. Update `.env` with your MySQL credentials:
```ini
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=cyber_career_copilot
USE_SQLITE_FALLBACK=True
```

#### Option B: Zero-Config SQLite Fallback
If MySQL is not installed or the password is unknown, the application will automatically initialize a local SQLite database (`cyber_career_copilot.db`) on startup. All features function identically!

### 4. Optional AI API Configuration
In `.env`:
- To run with live Google Gemini:
  ```ini
  GEMINI_API_KEY=your_gemini_api_key_here
  ```
- To run with live OpenAI GPT:
  ```ini
  OPENAI_API_KEY=your_openai_api_key_here
  ```
- If left empty, Cyber Copilot operates seamlessly in **Intelligent Demo Mode** with its built-in cybersecurity knowledge base.

### 5. Running the Application
Start the Flask development server:
```bash
python app.py
```

Access the application in your browser:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🧪 Running the Automated Test Suite

Run the unit test suite to verify authentication, database queries, roadmap toggling, and quiz scoring:
```bash
python -m unittest tests/test_copilot.py
```

---

## 🛡️ Defensive Learning Notice

All project concepts and practical exercises in this platform are designed strictly for authorized, defensive learning environments (local home labs, VirtualBox, TryHackMe, PortSwigger, and OverTheWire). Unauthorized penetration testing or scanning against external networks without written authorization is illegal.
