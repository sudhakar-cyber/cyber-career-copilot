-- AI Cybersecurity Career Copilot - Database Schema
-- Database Name: cyber_career_copilot

CREATE DATABASE IF NOT EXISTS cyber_career_copilot CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE cyber_career_copilot;

-- 1. Users Table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(191) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(120) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. Student Profiles Table
CREATE TABLE IF NOT EXISTS student_profiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL UNIQUE,
    qualification VARCHAR(100) DEFAULT '',
    department VARCHAR(100) DEFAULT '',
    year_of_study VARCHAR(50) DEFAULT '',
    programming_languages TEXT,
    networking_skills TEXT,
    os_skills TEXT,
    cyber_level VARCHAR(50) DEFAULT 'Beginner',
    areas_of_interest TEXT,
    preferred_career VARCHAR(120) DEFAULT 'SOC Analyst',
    weekly_study_hours INT DEFAULT 10,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_profiles_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. Career Recommendations Table
CREATE TABLE IF NOT EXISTS career_recommendations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    career_title VARCHAR(120) NOT NULL,
    match_percentage INT DEFAULT 0,
    description TEXT,
    required_skills TEXT,
    tools_tech TEXT,
    beginner_resources TEXT,
    certifications TEXT,
    practical_projects TEXT,
    next_steps TEXT,
    is_ai_generated BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_career_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 4. Skill Assessments Table
CREATE TABLE IF NOT EXISTS skill_assessments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    career_title VARCHAR(120) NOT NULL,
    possessed_skills TEXT,
    improvement_skills TEXT,
    missing_foundation TEXT,
    priority_learning TEXT,
    practical_exercises TEXT,
    readiness_score INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_skill_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 5. Learning Roadmaps Table
CREATE TABLE IF NOT EXISTS learning_roadmaps (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    career_title VARCHAR(120) NOT NULL,
    overall_progress INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_roadmap_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 6. Roadmap Tasks Table
CREATE TABLE IF NOT EXISTS roadmap_tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roadmap_id INT NOT NULL,
    user_id INT NOT NULL,
    phase_number INT NOT NULL,
    phase_title VARCHAR(150) NOT NULL,
    task_title VARCHAR(200) NOT NULL,
    description TEXT,
    resource_url VARCHAR(255) DEFAULT '',
    is_completed BOOLEAN DEFAULT FALSE,
    completed_at TIMESTAMP NULL,
    sort_order INT DEFAULT 0,
    CONSTRAINT fk_task_roadmap FOREIGN KEY (roadmap_id) REFERENCES learning_roadmaps(id) ON DELETE CASCADE,
    CONSTRAINT fk_task_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 7. Projects Table
CREATE TABLE IF NOT EXISTS projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NULL,
    title VARCHAR(150) NOT NULL,
    difficulty_level VARCHAR(50) NOT NULL, -- Beginner, Intermediate, Advanced
    objective TEXT NOT NULL,
    prerequisites TEXT,
    tech_stack TEXT,
    milestones TEXT,
    learning_outcomes TEXT,
    status VARCHAR(50) DEFAULT 'Not Started', -- Not Started, In Progress, Completed
    is_custom BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_projects_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 8. Quiz Questions Table
CREATE TABLE IF NOT EXISTS quiz_questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(80) NOT NULL, -- Networking, Linux & OS, SOC Analysis, Ethical Hacking, Python Security, Scenario Defense
    career_tag VARCHAR(100) DEFAULT 'All',
    difficulty VARCHAR(50) DEFAULT 'Intermediate', -- Beginner, Intermediate, Advanced
    question_text TEXT NOT NULL,
    option_a VARCHAR(255) NOT NULL,
    option_b VARCHAR(255) NOT NULL,
    option_c VARCHAR(255) NOT NULL,
    option_d VARCHAR(255) NOT NULL,
    correct_option CHAR(1) NOT NULL, -- 'A', 'B', 'C', 'D'
    explanation TEXT NOT NULL,
    scenario_context TEXT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 9. Quiz Attempts Table
CREATE TABLE IF NOT EXISTS quiz_attempts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    category VARCHAR(80) NOT NULL,
    score INT NOT NULL,
    total_questions INT NOT NULL,
    percentage DECIMAL(5,2) NOT NULL,
    details_json MEDIUMTEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_quiz_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 10. Chat History Table
CREATE TABLE IF NOT EXISTS chat_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    sender VARCHAR(20) NOT NULL, -- 'user' or 'copilot'
    message TEXT NOT NULL,
    is_ai BOOLEAN DEFAULT FALSE,
    mode VARCHAR(50) DEFAULT 'demo', -- 'live_ai' or 'demo'
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_chat_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Indexes for performance
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_profiles_user ON student_profiles(user_id);
CREATE INDEX idx_roadmap_user ON learning_roadmaps(user_id);
CREATE INDEX idx_tasks_roadmap ON roadmap_tasks(roadmap_id);
CREATE INDEX idx_quiz_category ON quiz_questions(category);
CREATE INDEX idx_quiz_attempts_user ON quiz_attempts(user_id);
CREATE INDEX idx_chat_user ON chat_history(user_id);
