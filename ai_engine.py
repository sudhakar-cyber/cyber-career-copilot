"""
AI Engine for Cybersecurity Career Copilot
Provides:
1. Intelligent Career Matching & Scoring
2. Skill Gap Analysis (Possessed, Needs Improvement, Missing, Priorities, Exercises)
3. 6-Phase Personalized Learning Roadmap Generator
4. Cyber Copilot Chatbot (Live AI with Gemini / OpenAI fallback to Labeled Intelligent Demo Mode)
"""

import os
import re
import json
import requests
from config import Config
from data_seed import CAREERS_CATALOG, PROJECTS_CATALOG, CERTIFICATIONS_CATALOG

# Common cybersecurity skill taxonomy for matching
SKILL_TAXONOMY = {
    "languages": {
        "python": ["Python", "Scripting", "Automation", "Security Tooling"],
        "c": ["C", "Low-level Systems", "Memory Analysis", "Exploit Development"],
        "c++": ["C++", "Reverse Engineering", "Systems Security"],
        "bash": ["Bash", "Linux Scripting", "Command Line", "Automation"],
        "powershell": ["PowerShell", "Windows Administration", "Active Directory"],
        "javascript": ["JavaScript", "Web Security", "XSS", "DOM Security"],
        "sql": ["SQL", "Database Security", "SQL Injection"],
        "go": ["Go", "Cloud Security Tooling", "Microservices Security"],
        "java": ["Java", "Enterprise AppSec", "Android Security"]
    },
    "networking": {
        "tcp/ip": ["TCP/IP", "Protocols", "Network Architecture"],
        "wireshark": ["Wireshark", "Packet Analysis", "Traffic Inspection"],
        "dns/dhcp": ["DNS", "DHCP", "Network Services"],
        "firewalls": ["Firewalls", "Network Defense", "Access Control Lists"],
        "routing/switching": ["Routing & Switching", "Subnetting", "VLANs"],
        "vpn": ["VPNs", "IPsec", "Network Cryptography"]
    },
    "os": {
        "linux": ["Linux Administration", "Command Line", "File Permissions", "Shell Navigation"],
        "windows": ["Windows Administration", "Active Directory", "Registry", "Event Viewer"],
        "kali linux": ["Kali Linux", "Offensive Tooling", "Penetration Testing"],
        "macos": ["macOS Forensics", "Unix Shell"]
    }
}

# Fallback AI Knowledge Base for Demo Mode
CYBER_KNOWLEDGE_BASE = [
    {
        "keywords": ["soc", "soc analyst", "blue team", "siem", "splunk"],
        "response": (
            "### 🛡️ How to Become a SOC (Security Operations Center) Analyst\n\n"
            "A **SOC Analyst** monitors security alerts, detects anomalies, and performs first-line incident triage.\n\n"
            "**Key Steps to Get Started:**\n"
            "1. **Core Fundamentals:** Master the OSI model, TCP/IP 3-way handshake, common ports (53, 80, 443, 22), and subnetting.\n"
            "2. **Operating System Logs:** Learn Windows Event IDs (e.g., 4624 for logon, 4625 for failed login, 4688 for process creation) and Linux `/var/log/auth.log`.\n"
            "3. **SIEM Tooling:** Build a free home lab with **Splunk Free** or **Wazuh EDR/SIEM** on Ubuntu.\n"
            "4. **Packet Analysis:** Practice investigating malicious PCAPs using **Wireshark** (filter by `http.request.method == 'POST'` or `dns.flags.response == 1`).\n"
            "5. **Recommended Certifications:** CompTIA Security+, Blue Team Level 1 (BTL1), or CySA+.\n\n"
            "💡 *Pro-Tip:* Try free practice rooms on **LetsDefend.io** and TryHackMe's **SOC Level 1** path."
        )
    },
    {
        "keywords": ["ethical hacker", "pentest", "penetration tester", "offensive", "red team", "kali"],
        "response": (
            "### ⚔️ Ethical Hacker & Penetration Tester Guide\n\n"
            "Ethical Hackers identify and exploit vulnerabilities legally to help organizations secure their assets before attackers strike.\n\n"
            "**Actionable Learning Path:**\n"
            "1. **Linux Command Line:** Complete the **OverTheWire: Bandit** wargame to master Bash, file permissions, and piping.\n"
            "2. **Web Application Security:** Practice the **OWASP Top 10** (SQLi, XSS, CSRF, IDOR) on PortSwigger Web Security Academy (100% free).\n"
            "3. **Network Scanning:** Learn **Nmap** (`-sS`, `-sV`, `-sC`, `-p-`) and **Wireshark** to understand how exploits look on the wire.\n"
            "4. **Hands-on Labs:** Solve the free 'Starting Point' machines on **Hack The Box** and rooms on **TryHackMe**.\n"
            "5. **Recommended Certifications:** eJPT (eLearnSecurity Junior Penetration Tester) -> CompTIA PenTest+ -> OSCP."
        )
    },
    {
        "keywords": ["cert", "certification", "certifications", "security+", "ceh", "ejpt", "oscp", "comptia"],
        "response": (
            "### 📜 Top Cybersecurity Certifications for College Students\n\n"
            "Choosing the right certification depends on your career track:\n\n"
            "- **Foundational (Must-have for all roles):**\n"
            "  - **CompTIA Security+**: Industry gold standard entry cert. Covers cryptography, network defense, threats, and risk management.\n"
            "  - **CompTIA Network+**: Highly recommended if you lack strong networking fundamentals.\n\n"
            "- **Defensive / SOC Analyst:**\n"
            "  - **Blue Team Level 1 (BTL1)**: 24-hour hands-on incident investigation exam with real SIEM, forensics, and phishing triage.\n"
            "  - **CompTIA CySA+**: Recognized intermediate certification for security analytics and threat detection.\n\n"
            "- **Offensive / Ethical Hacking:**\n"
            "  - **eJPT (eLearnSecurity Junior Pen Tester)**: 100% hands-on practical exam, ideal first offensive cert before OSCP.\n"
            "  - **OSCP (OffSec)**: Rigorous 24-hour exam, recognized worldwide for senior penetration testing roles.\n\n"
            "- **Cloud Security:**\n"
            "  - **AWS Certified Security - Specialty** or **Azure SC-900 / AZ-500**."
        )
    },
    {
        "keywords": ["project", "projects", "ideas", "resume project", "portfolio"],
        "response": (
            "### 🚀 High-Impact Cybersecurity Projects for Your Resume\n\n"
            "Employers love candidates with hands-on GitHub projects. Here are 3 top recommendations by difficulty:\n\n"
            "1. **Beginner: Python File Integrity Monitor (FIM)**\n"
            "   - Computes baseline SHA-256 hashes of critical files and alerts when unexpected edits, deletions, or new files occur.\n\n"
            "2. **Intermediate: Snort / Suricata Intrusion Detection System (IDS)**\n"
            "   - Set up an IDS on a local VM, craft custom rules to detect SYN port scans and SQL injection attempts, and log alerts.\n\n"
            "3. **Advanced: Automated Security Log Analysis Dashboard (SIEM)**\n"
            "   - Parse web server and authentication logs with Python, correlate brute-force attempts, and display metrics with interactive charts.\n\n"
            "👉 *Tip:* Document your architecture with a clean README, test cases, and a network topology diagram on GitHub!"
        )
    },
    {
        "keywords": ["resume", "internship", "job", "career", "interview", "college"],
        "response": (
            "### 💼 Securing a Cybersecurity Internship as a Student\n\n"
            "Cybersecurity is notoriously hands-on, but college students can stand out with this blueprint:\n\n"
            "1. **Show Evidence of Practical Work:** Replace generic course descriptions with GitHub repositories, TryHackMe / HackTheBox public profile links, and CTF rankings.\n"
            "2. **Build a Virtual Home Lab:** Put a dedicated 'Home Lab Environment' section on your resume (e.g., 'Configured pfSense firewall, Active Directory domain controller with 2 client VMs, and Splunk forwarder').\n"
            "3. **Prepare for Technical Interviews:**\n"
            "   - Explain the TCP 3-way handshake in detail.\n"
            "   - Distinguish between symmetric vs asymmetric encryption with real examples (AES vs RSA).\n"
            "   - Explain how you would contain a suspected ransomware infection on a corporate host."
        )
    },
    {
        "keywords": ["tcp", "handshake", "osi", "networking", "ports"],
        "response": (
            "### 🌐 Networking Fundamentals for Cybersecurity\n\n"
            "Solid networking knowledge is non-negotiable in cybersecurity:\n\n"
            "- **TCP 3-Way Handshake:**\n"
            "  1. **SYN**: Client sends initial sequence number requesting a connection.\n"
            "  2. **SYN-ACK**: Server acknowledges client's sequence and sends its own sequence.\n"
            "  3. **ACK**: Client acknowledges server's sequence. Connection is now ESTABLISHED.\n\n"
            "- **Critical Ports to Memorize:**\n"
            "  - `21`: FTP | `22`: SSH | `25`: SMTP | `53`: DNS\n"
            "  - `80`: HTTP | `443`: HTTPS | `445`: SMB | `3389`: RDP\n\n"
            "- **OSI Layers (1 to 7):** Physical -> Data Link -> Network -> Transport -> Session -> Presentation -> Application."
        )
    }
]

def calculate_career_match(student_profile, career_data):
    """
    Computes a realistic, dynamic match percentage (0-100%) between a student's profile and a career.
    """
    score = 30  # Baseline interest
    profile_langs = [l.strip().lower() for l in (student_profile.get('programming_languages') or '').split(',') if l.strip()]
    profile_net = [n.strip().lower() for n in (student_profile.get('networking_skills') or '').split(',') if n.strip()]
    profile_os = [o.strip().lower() for o in (student_profile.get('os_skills') or '').split(',') if o.strip()]
    profile_interests = [i.strip().lower() for i in (student_profile.get('areas_of_interest') or '').split(',') if i.strip()]
    cyber_level = (student_profile.get('cyber_level') or 'Beginner').lower()
    preferred_career = (student_profile.get('preferred_career') or '').lower()

    # Bonus if explicitly preferred
    if preferred_career and preferred_career in career_data['title'].lower():
        score += 20

    # Knowledge level weighting
    if cyber_level == 'intermediate':
        score += 15
    elif cyber_level == 'advanced':
        score += 25
    else:
        score += 5

    # Check skills against required skills and tech stack
    req_skills_str = " ".join(career_data['required_skills']).lower()
    tech_str = " ".join(career_data['tools_tech']).lower()

    # Programming alignment
    for lang in profile_langs:
        if lang in req_skills_str or lang in tech_str or lang == 'python':
            score += 5

    # Networking alignment
    for net in profile_net:
        if any(term in req_skills_str or term in tech_str for term in [net, 'network', 'traffic', 'sniffing', 'wireshark']):
            score += 5

    # OS alignment
    for os_item in profile_os:
        if 'linux' in os_item and ('linux' in req_skills_str or 'kali' in tech_str):
            score += 6
        elif 'windows' in os_item and ('windows' in req_skills_str or 'active directory' in req_skills_str):
            score += 4

    # Interests alignment
    for interest in profile_interests:
        if interest in career_data['title'].lower() or interest in req_skills_str:
            score += 10

    # Cap score cleanly between 25% and 98%
    match_percentage = max(25, min(98, score))
    return match_percentage

def get_career_recommendations(student_profile):
    """
    Returns ranked career recommendations for the student.
    """
    recommendations = []
    for key, cdata in CAREERS_CATALOG.items():
        match_pct = calculate_career_match(student_profile, cdata)
        rec = {
            "career_title": cdata['title'],
            "match_percentage": match_pct,
            "description": cdata['description'],
            "required_skills": cdata['required_skills'],
            "tools_tech": cdata['tools_tech'],
            "beginner_resources": cdata['beginner_resources'],
            "certifications": cdata['certifications'],
            "practical_projects": cdata['practical_projects'],
            "next_steps": cdata['next_steps'],
            "is_ai_generated": False
        }
        recommendations.append(rec)

    # Sort descending by match percentage
    recommendations.sort(key=lambda x: x['match_percentage'], reverse=True)
    return recommendations

def analyze_skill_gap(student_profile, target_career_title=None):
    """
    Compares student's current profile skills against the target career requirements.
    Categorizes skills into Possessed, Needs Improvement, and Missing Foundation.
    """
    if not target_career_title or target_career_title not in CAREERS_CATALOG:
        target_career_title = student_profile.get('preferred_career') or "SOC Analyst"
        if target_career_title not in CAREERS_CATALOG:
            target_career_title = "SOC Analyst"

    career = CAREERS_CATALOG[target_career_title]
    required_skills = career['required_skills']
    cyber_level = (student_profile.get('cyber_level') or 'Beginner').lower()

    # Collect student skills into a search text
    student_langs = [s.strip().lower() for s in (student_profile.get('programming_languages') or '').split(',') if s.strip()]
    student_net = [s.strip().lower() for s in (student_profile.get('networking_skills') or '').split(',') if s.strip()]
    student_os = [s.strip().lower() for s in (student_profile.get('os_skills') or '').split(',') if s.strip()]
    all_student_terms = set(student_langs + student_net + student_os)

    possessed = []
    improvement = []
    missing = []

    for req in required_skills:
        req_lower = req.lower()
        matched = False
        # Check direct or synonym match
        for term in all_student_terms:
            if term in req_lower or any(word in req_lower for word in term.split()):
                matched = True
                break
        
        if matched:
            if cyber_level == 'beginner':
                # Possessed in concept, but needs practical improvement
                improvement.append(req)
            else:
                possessed.append(req)
        else:
            missing.append(req)

    # Ensure possessed has at least some elements if student has any foundational inputs
    if not possessed and not improvement and all_student_terms:
        # Transfer common skills
        if 'python' in all_student_terms:
            possessed.append("Python Scripting & Automation Basics")
        if 'linux' in all_student_terms:
            possessed.append("Linux Command Line Navigation")

    # Calculate realistic readiness score
    total_reqs = len(required_skills)
    readiness_score = int(((len(possessed) * 1.0 + len(improvement) * 0.5) / max(total_reqs, 1)) * 100)
    readiness_score = max(15, min(95, readiness_score))

    # Priority learning steps
    priorities = []
    for idx, skill in enumerate(missing[:3], 1):
        priorities.append(f"Priority #{idx}: Master foundational {skill} through structured labs.")
    if improvement:
        priorities.append(f"Priority #{len(priorities)+1}: Advance existing knowledge in {improvement[0]} to practical project level.")

    # Practical hands-on exercises tailored to gaps
    exercises = [
        {
            "title": f"{target_career_title} Lab Environment Setup",
            "description": "Configure an isolated virtual network in VirtualBox or VMware with an attacker/analyst VM and a vulnerable target machine.",
            "duration": "4-6 Hours",
            "skill_targeted": "System & Network Architecture"
        },
        {
            "title": "Packet Capture & Protocol Dissection",
            "description": "Inspect sample PCAPs from Malware-Traffic-Analysis.net using Wireshark display filters to isolate suspicious streams.",
            "duration": "3 Hours",
            "skill_targeted": "Traffic Inspection & Protocol Analysis"
        },
        {
            "title": "Hands-on Attack/Defense Simulation",
            "description": f"Complete 3 guided rooms on TryHackMe or PortSwigger related to {career['required_skills'][0]}.",
            "duration": "5 Hours",
            "skill_targeted": career['required_skills'][0]
        }
    ]

    return {
        "career_title": target_career_title,
        "readiness_score": readiness_score,
        "possessed_skills": possessed,
        "improvement_skills": improvement,
        "missing_foundation": missing,
        "priority_learning": priorities,
        "practical_exercises": exercises
    }

def generate_personalized_roadmap(student_profile, target_career_title=None):
    """
    Generates a structured 6-phase learning roadmap customized to the student's career target.
    """
    if not target_career_title or target_career_title not in CAREERS_CATALOG:
        target_career_title = student_profile.get('preferred_career') or "SOC Analyst"
        if target_career_title not in CAREERS_CATALOG:
            target_career_title = "SOC Analyst"

    career = CAREERS_CATALOG[target_career_title]
    weekly_hours = student_profile.get('weekly_study_hours', 10)

    phases = [
        {
            "phase_number": 1,
            "phase_title": "Phase 1: Networking and Computer Fundamentals",
            "tasks": [
                {
                    "title": "Understand the OSI Model & TCP/IP Protocol Suite",
                    "description": "Learn the 7 layers of OSI, TCP vs UDP, standard ports, and packet encapsulation.",
                    "resource_url": "https://www.professormesser.com/network-plus/n10-008/n10-008-video/n10-008-training-course/"
                },
                {
                    "title": "Master IP Addressing, Subnetting, and DNS/DHCP",
                    "description": "Practice IPv4 CIDR notation, subnet masks, default gateways, and DNS query resolution flows.",
                    "resource_url": "https://www.youtube.com/playlist?list=PLDQaRcbiSnqF5U8ffMgZzS7fqkwU-SZQv"
                },
                {
                    "title": "Hands-on Wireshark Packet Analysis",
                    "description": "Capture local network traffic and write filters for HTTP, DNS, TCP handshakes, and ICMP.",
                    "resource_url": "https://www.wireshark.org/docs/"
                }
            ]
        },
        {
            "phase_number": 2,
            "phase_title": "Phase 2: Linux, Windows, and Python Basics",
            "tasks": [
                {
                    "title": "Linux Command Line & Permissions Mastery",
                    "description": "Complete Bandit levels 0-20 on OverTheWire to learn grep, permissions, pipes, and SSH keys.",
                    "resource_url": "https://overthewire.org/wargames/bandit/"
                },
                {
                    "title": "Windows Architecture & Event Log Auditing",
                    "description": "Inspect Windows Event Viewer, Sysinternals Process Explorer, and core Registry keys.",
                    "resource_url": "https://learn.microsoft.com/en-us/sysinternals/"
                },
                {
                    "title": "Python Scripting for Security Tasks",
                    "description": "Write Python scripts for automating port scanning, parsing log files, and sending HTTP requests.",
                    "resource_url": "https://docs.python.org/3/tutorial/"
                }
            ]
        },
        {
            "phase_number": 3,
            "phase_title": "Phase 3: Cybersecurity Fundamentals",
            "tasks": [
                {
                    "title": "Core Security Principles: CIA Triad, AAA, and Least Privilege",
                    "description": "Understand Confidentiality, Integrity, Availability, authentication mechanisms, and access control models.",
                    "resource_url": "https://csrc.nist.gov/glossary"
                },
                {
                    "title": "Threat Landscape & Common Attack Vectors",
                    "description": "Study phishing, malware variants, MITM attacks, DoS/DDoS, and social engineering methods.",
                    "resource_url": "https://www.cisa.gov/cybersecurity-best-practices"
                },
                {
                    "title": "Cryptographic Essentials: Symmetric, Asymmetric, and Hashing",
                    "description": "Understand AES, RSA, SHA-256, digital certificates, TLS handshakes, and Public Key Infrastructure (PKI).",
                    "resource_url": "https://en.wikipedia.org/wiki/Public-key_cryptography"
                }
            ]
        },
        {
            "phase_number": 4,
            "phase_title": f"Phase 4: Specialized Tools & Technical Skills for {target_career_title}",
            "tasks": [
                {
                    "title": f"Master Core Toolset: {career['tools_tech'][0]} and {career['tools_tech'][1]}",
                    "description": f"Install and operate {career['tools_tech'][0]} and {career['tools_tech'][1]} in a virtualized lab environment.",
                    "resource_url": career['beginner_resources'][0]['url']
                },
                {
                    "title": f"Implement Practical Workflows in {career['required_skills'][0]}",
                    "description": f"Learn industry standard workflows and playbooks for {career['required_skills'][0]}.",
                    "resource_url": career['beginner_resources'][1]['url'] if len(career['beginner_resources']) > 1 else "https://tryhackme.com"
                },
                {
                    "title": "Framework Integration: MITRE ATT&CK & Defense Mapping",
                    "description": "Map techniques and procedures to the MITRE ATT&CK enterprise matrix.",
                    "resource_url": "https://attack.mitre.org/"
                }
            ]
        },
        {
            "phase_number": 5,
            "phase_title": "Phase 5: Hands-on Projects and Practical Labs",
            "tasks": [
                {
                    "title": f"Build Practical Capstone: {career['practical_projects'][0]}",
                    "description": f"Develop, test, and document the project '{career['practical_projects'][0]}' in an authorized environment.",
                    "resource_url": "https://github.com"
                },
                {
                    "title": "Publish Technical Write-ups & GitHub Repository",
                    "description": "Document your design choices, architecture diagrams, and lessons learned to showcase to recruiters.",
                    "resource_url": "https://medium.com"
                },
                {
                    "title": "Complete 5 Hands-on CTF / Lab Challenges",
                    "description": "Solve intermediate challenge labs on TryHackMe, HackTheBox, or PortSwigger.",
                    "resource_url": "https://portswigger.net/web-security"
                }
            ]
        },
        {
            "phase_number": 6,
            "phase_title": "Phase 6: Certifications and Interview Preparation",
            "tasks": [
                {
                    "title": f"Target Certification Prep: {career['certifications'][0]}",
                    "description": f"Review official exam objectives and take practice assessments for {career['certifications'][0]}.",
                    "resource_url": "https://www.comptia.org"
                },
                {
                    "title": "Technical Cyber Mock Interviews & Scenario Drills",
                    "description": "Practice answering scenario-based questions: ransomware mitigation, packet dissection, and log analysis.",
                    "resource_url": "#interview"
                },
                {
                    "title": "Resume & LinkedIn Optimization with Practical Proof",
                    "description": "Format your resume highlighting completed projects, lab setups, and verified certifications.",
                    "resource_url": "https://www.linkedin.com"
                }
            ]
        }
    ]

    return {
        "career_title": target_career_title,
        "weekly_hours": weekly_hours,
        "phases": phases
    }

def ask_cyber_copilot(query, student_profile=None):
    """
    Handles student questions to Cyber Copilot.
    Tries live AI (Gemini or OpenAI) if API key is present in environment variables.
    Falls back cleanly and transparently to the intelligent curated cybersecurity knowledge base.
    """
    clean_query = query.strip()
    preferred_career = (student_profile.get('preferred_career') if student_profile else '') or "Cybersecurity Analyst"
    cyber_level = (student_profile.get('cyber_level') if student_profile else '') or "Beginner"

    # 1. Attempt Google Gemini API if configured
    if Config.GEMINI_API_KEY:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={Config.GEMINI_API_KEY}"
            prompt = (
                f"You are Cyber Copilot, an expert, encouraging cybersecurity mentor for college students.\n"
                f"Student Profile: Preferred Career: {preferred_career}, Experience Level: {cyber_level}.\n"
                f"Question: {clean_query}\n\n"
                f"Provide a clear, beginner-friendly, structured answer with technical accuracy and authorized/defensive security ethics."
            )
            payload = {
                "contents": [{"parts": [{"text": prompt}]}]
            }
            resp = requests.post(url, json=payload, timeout=8)
            if resp.status_code == 200:
                data = resp.json()
                text = data['candidates'][0]['content']['parts'][0]['text']
                return {
                    "response": text,
                    "mode": "live_ai",
                    "is_ai": True,
                    "model": "Gemini 1.5 Flash"
                }
        except Exception as e:
            print(f"[AI Copilot] Gemini API error, falling back to demo mode: {e}")

    # 2. Attempt OpenAI API if configured
    if Config.OPENAI_API_KEY:
        try:
            url = "https://api.openai.com/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {Config.OPENAI_API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "gpt-4o-mini",
                "messages": [
                    {
                        "role": "system",
                        "content": f"You are Cyber Copilot, an encouraging mentor for college cybersecurity students. The student is aiming for {preferred_career} at a {cyber_level} level. Focus on defensive, authorized security practices."
                    },
                    {"role": "user", "content": clean_query}
                ]
            }
            resp = requests.post(url, headers=headers, json=payload, timeout=8)
            if resp.status_code == 200:
                data = resp.json()
                text = data['choices'][0]['message']['content']
                return {
                    "response": text,
                    "mode": "live_ai",
                    "is_ai": True,
                    "model": "OpenAI GPT-4o Mini"
                }
        except Exception as e:
            print(f"[AI Copilot] OpenAI API error, falling back to demo mode: {e}")

    # 3. Transparent, Clearly-Labeled Demo Fallback Mode
    q_lower = clean_query.lower()

    # Search knowledge base matches
    matched_response = None
    for item in CYBER_KNOWLEDGE_BASE:
        for kw in item['keywords']:
            if kw in q_lower:
                matched_response = item['response']
                break
        if matched_response:
            break

    if not matched_response:
        # Check specific career mentions
        for career_name, cinfo in CAREERS_CATALOG.items():
            if career_name.lower() in q_lower:
                matched_response = (
                    f"### 🎯 Career Overview: {career_name}\n\n"
                    f"{cinfo['description']}\n\n"
                    f"**Core Technical Skills:** {', '.join(cinfo['required_skills'])}\n\n"
                    f"**Essential Tools:** {', '.join(cinfo['tools_tech'])}\n\n"
                    f"**Top Certifications:** {', '.join(cinfo['certifications'])}\n\n"
                    f"**Recommended First Project:** {cinfo['practical_projects'][0]}"
                )
                break

    if not matched_response:
        # High quality generic cyber mentor response
        matched_response = (
            f"Hello! As your **Cyber Copilot**, I'm here to help guide your journey towards becoming a **{preferred_career}**.\n\n"
            f"Regarding your question on: *\"{clean_query}\"*\n\n"
            f"**Key Recommendations for your {cyber_level} stage:**\n"
            f"1. **Foundations First:** Ensure you are comfortable with computer networking (TCP/IP, DNS, Subnets) and basic Linux shell navigation.\n"
            f"2. **Hands-on Practice:** Practical labs on platforms like TryHackMe, PortSwigger, and local VirtualBox labs are worth 10x more than passive reading.\n"
            f"3. **Build Tangible Artifacts:** Code a security tool in Python (like a port scanner or log analyzer) and push it to GitHub with a detailed README.\n"
            f"4. **Certifications:** Work toward **CompTIA Security+** to validate your foundational knowledge for college placements.\n\n"
            f"Feel free to ask me about specific topics like **'SOC Analyst path'**, **'Top Certifications'**, **'Project Ideas'**, or **'TCP Handshake'**!"
        )

    # Prefix with clear, prominent demo mode notification
    demo_badge = (
        "> ℹ️ **[DEMO MODE: Predefined Expert Cybersecurity Guidance]**\n"
        "> *Running on local offline cybersecurity knowledge base. To activate real-time LLM inference, configure `GEMINI_API_KEY` or `OPENAI_API_KEY` in `.env`.*\n\n"
    )

    return {
        "response": demo_badge + matched_response,
        "mode": "demo",
        "is_ai": False,
        "model": "Cyber Copilot Knowledge Base (Demo Mode)"
    }
