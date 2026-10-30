"""
Initial Seed Data for Cybersecurity Career Copilot
Contains curated career profiles, project definitions, certifications, and technical quiz questions.
"""

CAREERS_CATALOG = {
    "Ethical Hacker": {
        "title": "Ethical Hacker",
        "description": "Legally breaks into computers and networks to test an organization's overall defenses using authorized penetration methodologies, offensive security tooling, and exploit research.",
        "required_skills": ["Vulnerability Assessment", "Linux Administration", "Python/Bash Scripting", "Web Application Security", "Network Protocols & Sniffing", "Wireless Security"],
        "tools_tech": ["Kali Linux", "Burp Suite", "Nmap", "Metasploit", "Wireshark", "Hydra", "John the Ripper"],
        "beginner_resources": [
            {"title": "OverTheWire: Bandit (Linux Wargames)", "url": "https://overthewire.org/wargames/bandit/", "type": "Interactive Lab", "free": True},
            {"title": "TryHackMe Pre-Security Path", "url": "https://tryhackme.com/path/outline/pre-security", "type": "Guided Labs", "free": False},
            {"title": "PortSwigger Web Security Academy", "url": "https://portswigger.net/web-security", "type": "Web Security Labs", "free": True}
        ],
        "certifications": ["eJPT (eLearnSecurity Junior Penetration Tester)", "CompTIA Security+", "CEH (Certified Ethical Hacker)"],
        "practical_projects": [
            "Network Port Scanner in Python",
            "Vulnerability Report on VulnHub/HackTheBox machine",
            "Custom Brute-Force Authentication Auditor"
        ],
        "next_steps": [
            "Master command line Linux fundamentals & permissions",
            "Set up a local vulnerable lab using VirtualBox & Metasploitable",
            "Practice web exploits on PortSwigger Web Security Academy"
        ]
    },
    "SOC Analyst": {
        "title": "SOC Analyst",
        "description": "Monitors security infrastructure, triages automated SIEM alerts, detects suspicious network activities, analyzes potential cyber attacks, and conducts first-line incident response.",
        "required_skills": ["SIEM Operations", "Log Analysis", "Network Traffic Inspection", "Threat Intelligence", "MITRE ATT&CK Framework", "Incident Triage"],
        "tools_tech": ["Splunk", "Elastic Security (ELK)", "Wireshark", "Suricata/Snort", "VirusTotal", "AlienVault OTX", "CyberChef"],
        "beginner_resources": [
            {"title": "LetsDefend Blue Team Simulator", "url": "https://letsdefend.io/", "type": "SOC Simulator", "free": False},
            {"title": "Splunk Free Fundamentals Training", "url": "https://www.splunk.com/en_us/training/free-courses/splunk-fundamentals-1.html", "type": "Video Course", "free": True},
            {"title": "TryHackMe SOC Level 1 Path", "url": "https://tryhackme.com/path/outline/soclevel1", "type": "Guided Labs", "free": False}
        ],
        "certifications": ["CompTIA Security+", "Blue Team Level 1 (BTL1)", "CompTIA CySA+"],
        "practical_projects": [
            "Home Lab SIEM Deployment using Splunk or Elastic",
            "Brute Force Detection Rule & Alert Triage in Wazuh",
            "Phishing Email Header Analysis & IoC Extraction"
        ],
        "next_steps": [
            "Understand standard event IDs in Windows Event Viewer (4624, 4625, 4688)",
            "Deploy a free home instance of Splunk or Wazuh on Ubuntu Server",
            "Investigate sample PCAP packets using Wireshark filters"
        ]
    },
    "Penetration Tester": {
        "title": "Penetration Tester",
        "description": "Conducts authorized, structured simulated cyber attacks against computer systems, networks, APIs, and cloud environments to identify exploitable vulnerabilities and produce executive remediation reports.",
        "required_skills": ["Network Exploitation", "Web App Vulnerability Testing (OWASP Top 10)", "Privilege Escalation", "Scripting (Python/Bash/PowerShell)", "Reporting & Documentation"],
        "tools_tech": ["Kali Linux", "Burp Suite Pro", "Nmap", "ffuf/gobuster", "Impacket", "BloodHound", "SQLMap"],
        "beginner_resources": [
            {"title": "TCM Security - Practical Ethical Hacking", "url": "https://academy.tcm-sec.com/", "type": "Video Course", "free": False},
            {"title": "Hack The Box Starting Point", "url": "https://www.hackthebox.com/hacker/starting-point", "type": "Interactive Labs", "free": True},
            {"title": "OWASP Testing Guide (WSTG)", "url": "https://owasp.org/www-project-web-security-testing-guide/", "type": "Standard Guide", "free": True}
        ],
        "certifications": ["eJPT", "OSCP (Offensive Security Certified Professional)", "CompTIA PenTest+"],
        "practical_projects": [
            "Complete 10 HackTheBox Easy/Medium Boxes with structured write-ups",
            "Automated Subdomain Enumerator & Port Scanner Script",
            "SQL Injection Detection & Proof of Concept Test Tool"
        ],
        "next_steps": [
            "Master manual exploitation before relying on automated tools",
            "Learn Linux and Windows privilege escalation vectors",
            "Develop clear technical documentation and remediation writing skills"
        ]
    },
    "Cybersecurity Analyst": {
        "title": "Cybersecurity Analyst",
        "description": "Protects an organization's computer networks, cloud infrastructure, and endpoints by developing security policies, monitoring vulnerabilities, and conducting compliance assessments.",
        "required_skills": ["Risk Assessment", "Vulnerability Management", "Network Architecture", "Security Policies & Standards (NIST, ISO 27001)", "Security Controls"],
        "tools_tech": ["Nessus", "Qualys", "Wireshark", "Microsoft Defender", "NIST CSF Tools", "Nmap"],
        "beginner_resources": [
            {"title": "Professor Messer CompTIA Security+ Course", "url": "https://www.professormesser.com/", "type": "Video Series", "free": True},
            {"title": "NIST Cybersecurity Framework Official", "url": "https://www.nist.gov/cyberframework", "type": "Standard Documentation", "free": True},
            {"title": "Cybrary Introduction to IT & Cybersecurity", "url": "https://www.cybrary.it/", "type": "Online Course", "free": False}
        ],
        "certifications": ["CompTIA Security+", "CompTIA Network+", "SSCP (Systems Security Certified Practitioner)"],
        "practical_projects": [
            "Vulnerability Scan and Remediation Plan using Nessus Essentials",
            "Corporate Security Policy & Incident Response Playbook drafting",
            "Hardening Benchmark Audit on Windows and Linux Servers"
        ],
        "next_steps": [
            "Master the OSI model, TCP/IP, and firewall configurations",
            "Study NIST SP 800-53 security controls and risk scoring",
            "Install Nessus Essentials on a virtual machine to audit your network"
        ]
    },
    "Digital Forensics Analyst": {
        "title": "Digital Forensics Analyst",
        "description": "Recovers, investigates, and analyzes digital evidence from compromised hard drives, memory dumps, mobile devices, and server logs for incident investigation and legal proceedings.",
        "required_skills": ["Memory Forensics", "Disk Imaging & File Systems", "Chain of Custody Protocol", "Registry & Artifact Analysis", "Malware Triage"],
        "tools_tech": ["Autopsy", "Volatility 3", "FTK Imager", "Wireshark", "Eric Zimmerman Tools", "Sleuth Kit"],
        "beginner_resources": [
            {"title": "Cyber5W Digital Forensics Training", "url": "https://cyber5w.com/", "type": "Training Course", "free": False},
            {"title": "DFIR Training & Tools Portal", "url": "https://www.dfir.training/", "type": "Community Resource", "free": True},
            {"title": "TryHackMe Digital Forensics & Incident Response", "url": "https://tryhackme.com/", "type": "Hands-on Room", "free": False}
        ],
        "certifications": ["CHFI (Computer Hacking Forensic Investigator)", "GIAC Certified Forensic Analyst (GCFA)", "BTL1"],
        "practical_projects": [
            "Memory Dump Analysis of Ransomware Infection using Volatility",
            "Disk Forensics Evidence Extraction using Autopsy",
            "Windows Event Log & Registry Timeline Reconstruction"
        ],
        "next_steps": [
            "Understand FAT32, NTFS, and ext4 filesystem metadata structures",
            "Learn how to capture RAM and analyze processes with Volatility 3",
            "Practice artifact analysis on sample disk images from NIST CFTT"
        ]
    },
    "Cloud Security Engineer": {
        "title": "Cloud Security Engineer",
        "description": "Architects, implements, and maintains secure cloud environments across AWS, Azure, or GCP, enforcing identity management, infrastructure-as-code security, and cloud threat detection.",
        "required_skills": ["Cloud Architecture (AWS/Azure/GCP)", "IAM (Identity & Access Management)", "Infrastructure as Code (Terraform)", "Container Security (Docker/Kubernetes)", "Cloud Compliance"],
        "tools_tech": ["AWS GuardDuty/SecurityHub", "Azure Sentinel", "Terraform", "Trivy", "Prowler", "Docker", "ScoutSuite"],
        "beginner_resources": [
            {"title": "AWS Skill Builder Cloud Security Essentials", "url": "https://skillbuilder.aws/", "type": "Official Training", "free": True},
            {"title": "Microsoft Learn: SC-900 Fundamentals", "url": "https://learn.microsoft.com/", "type": "Learning Path", "free": True},
            {"title": "FreeCodeCamp AWS Certified Cloud Practitioner", "url": "https://www.freecodecamp.org/", "type": "Video Tutorial", "free": True}
        ],
        "certifications": ["AWS Certified Security - Specialty", "Microsoft Azure Security Technologies (AZ-500)", "CompTIA Security+"],
        "practical_projects": [
            "AWS Multi-Tier Architecture with Strict IAM and S3 Bucket Policies",
            "Automated Cloud Infrastructure Security Audit with Prowler",
            "Container Vulnerability Scanning Pipeline with Trivy and GitHub Actions"
        ],
        "next_steps": [
            "Master cloud shared responsibility model and IAM least privilege",
            "Create a free tier AWS or Azure account and configure MFA and CloudTrail",
            "Learn Docker containerization and image scanning tools"
        ]
    },
    "Application Security Engineer": {
        "title": "Application Security Engineer",
        "description": "Embeds security into the software development life cycle (DevSecOps), reviews source code for flaws, conducts dynamic security testing, and helps developers build resilient software.",
        "required_skills": ["SAST & DAST Tools", "Secure Software Development", "OWASP Top 10 / ASVS", "API Security", "CI/CD Pipeline Security Integration"],
        "tools_tech": ["SonarQube", "Snyk", "Burp Suite", "OWASP ZAP", "GitHub CodeQL", "Postman", "Semgrep"],
        "beginner_resources": [
            {"title": "PortSwigger Web Security Academy", "url": "https://portswigger.net/web-security", "type": "Hands-on Labs", "free": True},
            {"title": "OWASP Application Security Verification Standard", "url": "https://owasp.org/www-project-application-security-verification-standard/", "type": "Framework Guide", "free": True},
            {"title": "SecureFlag Secure Coding Labs", "url": "https://www.secureflag.com/", "type": "Interactive Platform", "free": False}
        ],
        "certifications": ["CSSLP (Certified Secure Software Lifecycle Professional)", "CASE (Certified Application Security Engineer)", "CompTIA Security+"],
        "practical_projects": [
            "DevSecOps CI/CD Pipeline with Semgrep and SonarQube in GitHub Actions",
            "API Security Vulnerability Scanner using Python and Postman",
            "Vulnerable Web Application Fix & Secure Code Remediation"
        ],
        "next_steps": [
            "Master OWASP Top 10 vulnerabilities (SQLi, XSS, SSRF, IDOR)",
            "Learn how to integrate automated SAST scanning tools into Git repositories",
            "Practice identifying flaws in source code (Python, JavaScript, Java)"
        ]
    },
    "Incident Response Analyst": {
        "title": "Incident Response Analyst",
        "description": "Leads investigations and mitigation efforts when active cyber breaches happen, isolating affected systems, containing ransomware, eliminating threats, and restoring operations.",
        "required_skills": ["Incident Handling (NIST SP 800-61)", "Network Containment", "Malware Behavior Analysis", "Root Cause Analysis", "Post-Incident Reporting"],
        "tools_tech": ["Velociraptor", "Wireshark", "YARA", "Cisco Talos", "Sysinternals Suite", "Ghidra"],
        "beginner_resources": [
            {"title": "NIST Computer Security Incident Handling Guide", "url": "https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final", "type": "Official Standard", "free": True},
            {"title": "TryHackMe Incident Response Module", "url": "https://tryhackme.com/", "type": "Hands-on Labs", "free": False},
            {"title": "SANS Reading Room: Incident Handling", "url": "https://www.sans.org/white-papers/", "type": "Whitepapers", "free": True}
        ],
        "certifications": ["GCIH (GIAC Certified Incident Handler)", "Blue Team Level 1 (BTL1)", "CompTIA CySA+"],
        "practical_projects": [
            "Incident Response Playbook for Ransomware Attack Scenario",
            "YARA Rule Development to Detect Malicious Binary Signatures",
            "Live Memory & Endpoint Triage with Velociraptor"
        ],
        "next_steps": [
            "Learn the 6 phases of incident response: Prep, Detection, Containment, Eradication, Recovery, Lessons Learned",
            "Master Windows Sysinternals tools (Process Explorer, Autoruns, Procmon)",
            "Write custom YARA rules to detect suspicious strings and file headers"
        ]
    }
}

PROJECTS_CATALOG = [
    # Beginner Projects
    {
        "title": "Password Strength Checker",
        "difficulty_level": "Beginner",
        "objective": "Design an interactive, defense-oriented password entropy calculator that tests candidate passwords against length, complexity, dictionary attacks, and known leaked hashes.",
        "prerequisites": "Basic Python or JavaScript, understanding of strings, regular expressions, and hashing fundamentals.",
        "tech_stack": "Python, zxcvbn / hashlib, Flask or CLI, HTML/CSS for UI",
        "milestones": "1. Implement regex checking for length, uppercase, lowercase, numbers, and symbols.\n2. Compute Shannon entropy in bits for password strength.\n3. Integrate local dictionary check to detect common leaked passwords.\n4. Build clean web UI with dynamic color-coded feedback and meter.",
        "learning_outcomes": "Mastery of hashing basics, password entropy theory, credential stuffing defense, and client/server validation."
    },
    {
        "title": "File Integrity Monitoring Tool",
        "difficulty_level": "Beginner",
        "objective": "Build a host-based security utility that scans monitored directories, calculates cryptographic SHA-256 baseline hashes, and alerts on unauthorized file modifications, additions, or deletions.",
        "prerequisites": "Python file I/O, os/pathlib modules, cryptographic hash functions (SHA-256).",
        "tech_stack": "Python, hashlib, watchdog / time scheduling, JSON/SQLite storage",
        "milestones": "1. Scan target directory and generate cryptographic baseline JSON.\n2. Create periodic file auditor comparing current hashes with baseline.\n3. Generate instant alert logs when files are tampered or deleted.\n4. Support recursive directory monitoring and exclusion patterns.",
        "learning_outcomes": "Understanding integrity verification in security architectures, baseline change detection, and defensive logging."
    },
    {
        "title": "Basic Network Traffic Analyzer",
        "difficulty_level": "Beginner",
        "objective": "Develop a lightweight network packet sniffer that captures local Ethernet/IP packets, decodes TCP/UDP/ICMP headers, and displays traffic statistics in real time.",
        "prerequisites": "TCP/IP OSI model knowledge, IP addressing, basic socket programming.",
        "tech_stack": "Python, Scapy or raw sockets, Matplotlib/Chart.js or terminal curses",
        "milestones": "1. Set up socket capture or Scapy sniffing with root/admin privileges.\n2. Extract source/destination IP, ports, protocol type, and payload size.\n3. Categorize common protocols (HTTP, DNS, SSH, HTTPS, ICMP).\n4. Output real-time statistics of top communicating IP addresses.",
        "learning_outcomes": "Hands-on packet dissection, understanding headers and frames, and foundational network defense skills."
    },

    # Intermediate Projects
    {
        "title": "Personal Firewall",
        "difficulty_level": "Intermediate",
        "objective": "Construct an application-level firewall rule engine that filters incoming and outgoing connections based on customizable port, IP, and protocol access control lists (ACLs).",
        "prerequisites": "Intermediate Python/C, networking concepts (stateful vs stateless filtering), OS network stack (iptables/Windows Filtering Platform).",
        "tech_stack": "Python / scapy / netfilterqueue (Linux) or Windows firewall API, JSON rule engine",
        "milestones": "1. Define access control list (ACL) schema (ALLOW/DENY by IP, Port, Direction).\n2. Intercept packets before routing or application delivery.\n3. Match packet metadata against stateful rules and log decisions.\n4. Build CLI or Web dashboard to view blocked connection attempts.",
        "learning_outcomes": "Deep understanding of firewall rule evaluation, stateful connection tracking, and packet dropping mechanics."
    },
    {
        "title": "Intrusion Detection System (IDS)",
        "difficulty_level": "Intermediate",
        "objective": "Build a signature and heuristic-based Network Intrusion Detection System (NIDS) that detects port scans (SYN/FIN), suspicious HTTP payloads, and DoS flood patterns.",
        "prerequisites": "Packet sniffing, regular expressions, signature-matching algorithms, threat detection concepts.",
        "tech_stack": "Python, Scapy, Snort rule syntax parsing, SQLite for security events",
        "milestones": "1. Ingest real-time packet stream or PCAP replay files.\n2. Implement detection logic for TCP SYN stealth scans and ICMP sweeps.\n3. Add HTTP payload regex inspection for SQLi (OR 1=1) and XSS (<script>).\n4. Dispatch structured security alerts with severity ratings (Low/Med/High).",
        "learning_outcomes": "Signature vs anomaly detection techniques, threat rule crafting, and automated security event triage."
    },
    {
        "title": "Phishing URL Detection Tool",
        "difficulty_level": "Intermediate",
        "objective": "Develop a multi-feature machine-learning and heuristic scanner that assesses candidate URLs for phishing indicators, typosquatting, suspicious redirect chains, and domain reputation.",
        "prerequisites": "Python, WHOIS lookup libraries, URL parsing, basic machine learning (scikit-learn) or heuristic feature engineering.",
        "tech_stack": "Python, Flask, scikit-learn, WHOIS, requests, BeautifulSoup",
        "milestones": "1. Extract lexical features (URL length, entropy, @ symbol, IP-in-domain, subdomains count).\n2. Query domain age via WHOIS and check HTTPS certificate validity.\n3. Train Random Forest / Logistic Regression classifier on phishing dataset.\n4. Create interactive web scanner with detailed threat score breakdown.",
        "learning_outcomes": "Phishing attack vectors, typosquatting mechanics, domain reputation analysis, and applied AI in threat detection."
    },

    # Advanced Projects
    {
        "title": "Security Log Analysis Dashboard",
        "difficulty_level": "Advanced",
        "objective": "Build a high-performance Security Information and Event Management (SIEM) dashboard that ingests authentication logs, normalizes heterogeneous events, and correlates attacks.",
        "prerequisites": "Data pipelines, regular expressions, database indexing, Chart.js/visualizations, MITRE ATT&CK mapping.",
        "tech_stack": "Python (Flask/FastAPI), SQLite/MySQL, Chart.js, Tailwind/Vanilla CSS, Logstash/Regex parser",
        "milestones": "1. Parse Apache, Nginx, Linux auth.log, and Windows Event logs into structured JSON.\n2. Build correlation rules for distributed brute-force attacks and privilege escalations.\n3. Map identified alerts to MITRE ATT&CK tactics and techniques.\n4. Design modern interactive SOC dashboard with real-time incident metrics.",
        "learning_outcomes": "Log parsing at scale, SIEM correlation rule engineering, MITRE ATT&CK mapping, and enterprise security visibility."
    },
    {
        "title": "Cloud Security Monitoring Tool",
        "difficulty_level": "Advanced",
        "objective": "Create an automated cloud posture and compliance auditing agent that evaluates AWS/Azure configurations against CIS Benchmarks for misconfigured buckets, permissive IAM roles, and unencrypted volumes.",
        "prerequisites": "Cloud architecture, IAM least privilege principles, boto3 / Azure SDK, compliance frameworks.",
        "tech_stack": "Python, Boto3 (AWS SDK), JSON/YAML policy parser, HTML report generator",
        "milestones": "1. Authenticate to cloud environment securely via IAM assume-role credentials.\n2. Audit S3 bucket public permissions, ACLs, and bucket policies.\n3. Check IAM user MFA enforcement and inactive access key rotation.\n4. Inspect Security Group ingress rules (detecting 0.0.0.0/0 on ports 22 & 3389).\n5. Generate executive PDF/HTML compliance score and remediation guide.",
        "learning_outcomes": "Cloud Security Posture Management (CSPM), identity auditing, automated cloud policy remediation, and CIS benchmarks."
    },
    {
        "title": "Machine Learning-Based Anomaly Detection System",
        "difficulty_level": "Advanced",
        "objective": "Develop an unsupervised machine learning model that establishes a baseline of normal network behavior and flags anomalous zero-day traffic spikes, data exfiltration, or botnet beacons.",
        "prerequisites": "Unsupervised ML algorithms (Isolation Forest, One-Class SVM, Autoencoders), network metric extraction, statistical modeling.",
        "tech_stack": "Python, scikit-learn / PyTorch, Pandas, Scapy, Flask UI with real-time charts",
        "milestones": "1. Extract temporal network features: packet rate, byte ratios, inter-arrival time, port diversity.\n2. Train Isolation Forest algorithm on clean baseline traffic.\n3. Stream test traffic (including simulated beaconing) and compute anomaly scores.\n4. Visualize anomalous spikes with confidence intervals and alert logs.",
        "learning_outcomes": "Zero-day detection principles, time-series anomaly detection, feature engineering for network security, and AI model evaluation."
    }
]

CERTIFICATIONS_CATALOG = [
    {
        "name": "CompTIA Security+",
        "difficulty": "Beginner to Intermediate",
        "skills_covered": "Security controls, threat identification, cryptographic concepts, network architecture, risk management",
        "intended_audience": "Entry-level cybersecurity professionals, IT specialists, students starting security careers",
        "official_url": "https://www.comptia.org/certifications/security",
        "is_free": False,
        "prerequisites": "CompTIA Network+ or 2 years IT administration experience recommended"
    },
    {
        "name": "CompTIA Network+",
        "difficulty": "Beginner",
        "skills_covered": "TCP/IP, subnetting, routing protocols, network topologies, DNS/DHCP, switch configurations",
        "intended_audience": "Students and IT technicians seeking solid networking fundamentals",
        "official_url": "https://www.comptia.org/certifications/network",
        "is_free": False,
        "prerequisites": "Basic computer literacy"
    },
    {
        "name": "eJPT (eLearnSecurity Junior Penetration Tester)",
        "difficulty": "Beginner to Intermediate",
        "skills_covered": "Hands-on penetration testing, host/network enumeration, vulnerability assessment, manual exploitation, pivoting",
        "intended_audience": "Aspiring penetration testers, ethical hackers, and defensive analysts wanting offensive insight",
        "official_url": "https://ine.com/certifications/ejpt-certification",
        "is_free": False,
        "prerequisites": "Basic networking and Linux command line familiarity"
    },
    {
        "name": "Blue Team Level 1 (BTL1)",
        "difficulty": "Intermediate",
        "skills_covered": "Security Information and Event Management (SIEM), Phishing Analysis, Digital Forensics, Threat Intelligence, Incident Response",
        "intended_audience": "Aspiring and junior SOC Analysts, Incident Responders, Blue Team defenders",
        "official_url": "https://securityblue.team/why-btl1/",
        "is_free": False,
        "prerequisites": "Basic networking and security concepts"
    },
    {
        "name": "CompTIA CySA+ (Cybersecurity Analyst)",
        "difficulty": "Intermediate",
        "skills_covered": "Threat intelligence, vulnerability management, security operations, compliance, automated incident response",
        "intended_audience": "SOC Analysts, security analysts with 2-4 years of experience or Security+ holders",
        "official_url": "https://www.comptia.org/certifications/cybersecurity-analyst",
        "is_free": False,
        "prerequisites": "CompTIA Security+ or equivalent knowledge recommended"
    },
    {
        "name": "OSCP (Offensive Security Certified Professional)",
        "difficulty": "Advanced",
        "skills_covered": "Practical penetration testing, exploit modification, privilege escalation, Active Directory exploitation, reporting",
        "intended_audience": "Intermediate to advanced penetration testers and security engineers",
        "official_url": "https://www.offsec.com/courses/pen-200/",
        "is_free": False,
        "prerequisites": "Solid Linux/Windows networking, scripting, and prior penetration testing lab experience"
    },
    {
        "name": "AWS Certified Security - Specialty",
        "difficulty": "Intermediate to Advanced",
        "skills_covered": "AWS Identity & Access Management (IAM), data protection, encryption, infrastructure security, incident response in the cloud",
        "intended_audience": "Cloud security engineers, cloud architects, DevSecOps professionals",
        "official_url": "https://aws.amazon.com/certification/certified-security-specialty/",
        "is_free": False,
        "prerequisites": "5 years of IT security experience with at least 2 years hands-on securing AWS workloads"
    },
    {
        "name": "PortSwigger Web Security Practitioner",
        "difficulty": "Intermediate",
        "skills_covered": "Web application security, SQL injection, Cross-Site Scripting (XSS), CSRF, Server-Side Request Forgery (SSRF), OAuth vulnerabilities",
        "intended_audience": "Application security engineers, web penetration testers, full-stack developers",
        "official_url": "https://portswigger.net/web-security/certification",
        "is_free": False,
        "prerequisites": "Web application development concepts (HTTP, cookies, sessions, APIs)"
    }
]

QUIZ_QUESTIONS_SEED = [
    # 1. Networking Questions
    {
        "category": "Networking",
        "career_tag": "All",
        "difficulty": "Beginner",
        "question_text": "During the TCP 3-way handshake, what is the exact sequence of flag packets sent between client and server to establish a reliable connection?",
        "option_a": "SYN -> ACK -> SYN-ACK",
        "option_b": "SYN -> SYN-ACK -> ACK",
        "option_c": "ACK -> SYN -> SYN-ACK",
        "option_d": "SYN -> FIN -> ACK",
        "correct_option": "B",
        "explanation": "The standard TCP 3-way handshake starts with the client sending a SYN (Synchronize), the server responding with SYN-ACK (Synchronize-Acknowledge), and the client finalizing with an ACK (Acknowledge).",
        "scenario_context": "A network security monitor is inspecting packet captures to verify connection establishment between an endpoint and a web server."
    },
    {
        "category": "Networking",
        "career_tag": "All",
        "difficulty": "Intermediate",
        "question_text": "Which network attack involves an adversary sending falsified ARP replies across a local area network to bind their MAC address with the default gateway's IP address?",
        "option_a": "DNS Poisoning",
        "option_b": "ARP Cache Poisoning (Spoofing)",
        "option_c": "BGP Hijacking",
        "option_d": "DHCP Starvation",
        "correct_option": "B",
        "explanation": "ARP Spoofing exploits the stateless nature of ARP by sending unsolicited ARP reply packets, tricking devices on the local subnet into sending traffic to the attacker's MAC address instead of the legitimate gateway.",
        "scenario_context": "A technician detects intermittent network latency and unencrypted session hijacking happening on a university computer lab switch."
    },
    {
        "category": "Networking",
        "career_tag": "All",
        "difficulty": "Beginner",
        "question_text": "What is the default port and underlying transport protocol utilized by DNS (Domain Name System) queries during standard name resolution?",
        "option_a": "Port 53 over UDP",
        "option_b": "Port 80 over TCP",
        "option_c": "Port 443 over UDP",
        "option_d": "Port 22 over TCP",
        "correct_option": "A",
        "explanation": "Standard DNS resolution queries use Port 53 over UDP because it is fast and low-overhead. TCP port 53 is used for zone transfers or responses exceeding 512 bytes.",
        "scenario_context": "A firewall engineer is configuring outbound egress filtering rules for an enterprise branch office."
    },
    {
        "category": "Networking",
        "career_tag": "Penetration Tester",
        "difficulty": "Intermediate",
        "question_text": "When running an Nmap scan with the '-sS' parameter, what mechanism makes this scan 'stealthy' compared to a normal connect scan (-sT)?",
        "option_a": "It encrypts packet payloads using TLS",
        "option_b": "It sends a FIN packet to terminate existing connections",
        "option_c": "It sends a SYN packet and resets (RST) upon receiving SYN-ACK without completing the handshake",
        "option_d": "It routes traffic through the Tor onion routing network",
        "correct_option": "C",
        "explanation": "Nmap's SYN Stealth Scan (-sS) never completes the 3-way handshake. When the target responds with SYN-ACK, Nmap immediately sends a RST packet, preventing application-layer connection logs on older systems.",
        "scenario_context": "An authorized ethical hacker is mapping open listening services on a client's perimeter without establishing full TCP sessions."
    },

    # 2. Linux & OS Questions
    {
        "category": "Linux & OS",
        "career_tag": "Ethical Hacker",
        "difficulty": "Beginner",
        "question_text": "In Linux systems, which file contains the hashed user passwords and account expiration details, accessible only by the root superuser?",
        "option_a": "/etc/passwd",
        "option_b": "/etc/shadow",
        "option_c": "/etc/group",
        "option_d": "/var/log/auth.log",
        "correct_option": "B",
        "explanation": "/etc/shadow stores salted password hashes and account expiration flags and has strict permissions (read-only for root, 0640 or 0600), whereas /etc/passwd is world-readable for system processes.",
        "scenario_context": "A security auditor is checking file permissions on an Ubuntu production database server."
    },
    {
        "category": "Linux & OS",
        "career_tag": "All",
        "difficulty": "Intermediate",
        "question_text": "What does a special SUID (Set User ID) permission bit on an executable binary in Linux allow an unprivileged user to do?",
        "option_a": "Execute the binary with the privileges of the file's owner (often root)",
        "option_b": "Modify the binary's source code in place",
        "option_c": "Prevent the binary from being terminated by kill -9",
        "option_d": "Automatically run the binary at boot time",
        "correct_option": "A",
        "explanation": "When an executable has the SUID bit set (e.g., chmod u+s /usr/bin/passwd), any user executing the program temporarily inherits the privileges of the binary's file owner (commonly root). Misconfigured SUID binaries are common privilege escalation targets.",
        "scenario_context": "A student conducting a Linux privilege escalation audit runs 'find / -perm -u=s -type f 2>/dev/null'."
    },
    {
        "category": "Linux & OS",
        "career_tag": "Incident Response Analyst",
        "difficulty": "Intermediate",
        "question_text": "Which Windows Event ID indicates a successful user logon to a local or domain workstation?",
        "option_a": "Event ID 4624",
        "option_b": "Event ID 4625",
        "option_c": "Event ID 4688",
        "option_d": "Event ID 7045",
        "correct_option": "A",
        "explanation": "In Windows Security Event Logs, Event ID 4624 represents a successful account logon (with logon types such as 2 for interactive, 3 for network, 10 for RDP). Event ID 4625 records failed logons.",
        "scenario_context": "An incident investigator is correlating logon timestamps following suspected credential theft."
    },

    # 3. SOC Analysis Questions
    {
        "category": "SOC Analysis",
        "career_tag": "SOC Analyst",
        "difficulty": "Beginner",
        "question_text": "What is the primary difference between a False Positive and a True Positive alert in a Security Operations Center (SOC)?",
        "option_a": "False Positive is a real breach ignored; True Positive is a test alert",
        "option_b": "False Positive is an alert triggered by benign activity; True Positive is an alert triggered by genuine malicious or unauthorized activity",
        "option_c": "False Positive only occurs on Linux; True Positive occurs on Windows",
        "option_d": "False Positive has High severity; True Positive has Low severity",
        "correct_option": "B",
        "explanation": "A False Positive occurs when benign operational behavior triggers a security rule. A True Positive correctly identifies actual adversarial, malicious, or non-compliant actions.",
        "scenario_context": "A Tier 1 SOC Analyst receives 15 SIEM alerts after a developer deployed a new automated backup script."
    },
    {
        "category": "SOC Analysis",
        "career_tag": "SOC Analyst",
        "difficulty": "Intermediate",
        "question_text": "In the MITRE ATT&CK framework, what is the distinction between a 'Tactic' and a 'Technique'?",
        "option_a": "Tactics describe the adversary's technical goal ('Why'); Techniques describe the specific method used ('How')",
        "option_b": "Tactics are hardware tools; Techniques are software packages",
        "option_c": "Tactics apply only to malware; Techniques apply to social engineering",
        "option_d": "Tactics are defensive measures; Techniques are offensive exploits",
        "correct_option": "A",
        "explanation": "Tactics represent the high-level tactical objective (e.g., Initial Access, Persistence, Privilege Escalation), while Techniques represent the specific actions and mechanisms an attacker uses to achieve that goal.",
        "scenario_context": "A blue team is mapping a ransomware intrusion report to the enterprise MITRE ATT&CK matrix."
    },
    {
        "category": "SOC Analysis",
        "career_tag": "SOC Analyst",
        "difficulty": "Intermediate",
        "question_text": "What type of artifact is an IP address, domain name, or MD5/SHA256 file hash categorized as in threat intelligence terminology?",
        "option_a": "TTP (Tactics, Techniques, and Procedures)",
        "option_b": "IoC (Indicator of Compromise)",
        "option_c": "SLA (Service Level Agreement)",
        "option_d": "CVE (Common Vulnerabilities and Exposures)",
        "correct_option": "B",
        "explanation": "An Indicator of Compromise (IoC) is forensic evidence of potential intrusion or malicious activity on a host or network, such as known bad IP addresses, malicious URLs, or malware file hashes.",
        "scenario_context": "A threat intelligence team distributes a daily threat bulletin containing hashes associated with a new spear-phishing campaign."
    },

    # 4. Ethical Hacking & Web Security
    {
        "category": "Ethical Hacking",
        "career_tag": "Ethical Hacker",
        "difficulty": "Beginner",
        "question_text": "Which vulnerability occurs when user-supplied input is directly concatenated into a database query without parameterized statements or escaping?",
        "option_a": "Cross-Site Request Forgery (CSRF)",
        "option_b": "SQL Injection (SQLi)",
        "option_c": "Insecure Direct Object Reference (IDOR)",
        "option_d": "Cross-Site Scripting (XSS)",
        "correct_option": "B",
        "explanation": "SQL Injection happens when untrusted user input is directly concatenated into an SQL statement, allowing the attacker to manipulate the query logic, bypass authentication, or exfiltrate database records.",
        "scenario_context": "A tester inputs `' OR '1'='1' -- ` into a login username field and successfully bypasses authentication."
    },
    {
        "category": "Ethical Hacking",
        "career_tag": "Application Security Engineer",
        "difficulty": "Intermediate",
        "question_text": "What is the most secure and reliable defense against SQL Injection vulnerabilities in modern web applications?",
        "option_a": "Client-side JavaScript input length checks",
        "option_b": "Blacklisting the single quote (') and double dash (--) characters",
        "option_c": "Parameterized queries (prepared statements) and ORM query binding",
        "option_d": "Base64 encoding all URL parameters",
        "correct_option": "C",
        "explanation": "Parameterized queries (prepared statements) treat user input strictly as literal data rather than executable SQL syntax, completely neutralising injection attempts regardless of input content.",
        "scenario_context": "A software engineer is refactoring an e-commerce backend to eliminate critical OWASP vulnerabilities."
    },
    {
        "category": "Ethical Hacking",
        "career_tag": "Ethical Hacker",
        "difficulty": "Intermediate",
        "question_text": "Which HTTP cookie flag instructs web browsers that the cookie must NOT be accessed via client-side JavaScript (e.g. document.cookie), mitigating session theft via XSS?",
        "option_a": "Secure",
        "option_b": "SameSite=Strict",
        "option_c": "HttpOnly",
        "option_d": "Path=/",
        "correct_option": "C",
        "explanation": "The 'HttpOnly' flag prevents client-side scripts from reading session cookies via JavaScript, substantially reducing the risk of session hijacking in the event of a Cross-Site Scripting (XSS) attack.",
        "scenario_context": "An application security specialist is auditing response headers for a banking portal's session management."
    },

    # 5. Python & Scripting Security
    {
        "category": "Python Security",
        "career_tag": "All",
        "difficulty": "Beginner",
        "question_text": "Why should password verification in security applications use 'hmac.compare_digest()' or 'secrets.compare_digest()' instead of standard '==' comparison?",
        "option_a": "Standard '==' comparison crashes on binary strings",
        "option_b": "Standard '==' comparison is vulnerable to side-channel timing attacks because it returns early upon first mismatch",
        "option_c": "Standard '==' comparison requires root privileges",
        "option_d": "Standard '==' only works with numbers",
        "correct_option": "B",
        "explanation": "Standard string equality comparison terminates as soon as the first non-matching character is found, leaking timing differences that adversaries can measure. 'compare_digest' runs in constant time.",
        "scenario_context": "A security engineer is reviewing an authentication webhook handler verifying HMAC signatures."
    },
    {
        "category": "Python Security",
        "career_tag": "Ethical Hacker",
        "difficulty": "Intermediate",
        "question_text": "In Python, which popular library allows developers to craft, send, sniff, and dissect custom raw network packets across layers 2, 3, and 4?",
        "option_a": "Requests",
        "option_b": "Scapy",
        "option_c": "Urllib3",
        "option_d": "BeautifulSoup",
        "correct_option": "B",
        "explanation": "Scapy is the premier Python interactive packet manipulation tool and library capable of forging and decoding packets of a vast number of protocols, handling pings, traceroutes, probes, and attacks.",
        "scenario_context": "A student is writing an automated ARP monitor and custom TCP SYN scanner for their cyber capstone project."
    },

    # 6. Scenario-Based Defensive Security
    {
        "category": "Scenario Defense",
        "career_tag": "Incident Response Analyst",
        "difficulty": "Intermediate",
        "question_text": "A workstation on your corporate VLAN is actively encrypting network share files and displaying a ransomware note. What should be your FIRST immediate action?",
        "option_a": "Pay the cryptocurrency ransom immediately to retrieve keys",
        "option_b": "Isolate the infected workstation from the physical and wireless network (unplug Ethernet / disable Wi-Fi)",
        "option_c": "Reboot the workstation immediately",
        "option_d": "Delete all log files on the workstation to free disk space",
        "correct_option": "B",
        "explanation": "The immediate containment priority during an active ransomware attack is isolating the infected machine from the network to prevent lateral movement and stop encryption of connected network shares.",
        "scenario_context": "An emergency ticket arrives at 02:00 AM from the accounting department reporting encrypted file extensions."
    },
    {
        "category": "Scenario Defense",
        "career_tag": "Cybersecurity Analyst",
        "difficulty": "Beginner",
        "question_text": "An employee receives an email appearing to come from the CEO demanding an urgent wire transfer to an unknown vendor with an external sender domain. What type of social engineering attack is this?",
        "option_a": "Business Email Compromise (BEC) / CEO Fraud",
        "option_b": "Watering Hole Attack",
        "option_c": "Cross-Site Scripting",
        "option_d": "Distributed Denial of Service",
        "correct_option": "A",
        "explanation": "Business Email Compromise (BEC) is a targeted spear-phishing attack where criminals impersonate executives or trusted partners to trick employees into transferring funds or sensitive information.",
        "scenario_context": "A human resources officer forwards a suspicious email regarding an 'Urgent Executive Payroll Update'."
    },
    {
        "category": "Scenario Defense",
        "career_tag": "Cloud Security Engineer",
        "difficulty": "Advanced",
        "question_text": "In AWS cloud security, what is the best practice policy for securing storage buckets containing sensitive customer data?",
        "option_a": "Enable S3 Block Public Access, enable KMS server-side encryption, and enforce least-privilege IAM bucket policies",
        "option_b": "Make the bucket public so customer browsers do not get HTTP 403 errors",
        "option_c": "Store root account credentials directly inside the bucket",
        "option_d": "Disable CloudTrail logging to reduce storage cost",
        "correct_option": "A",
        "explanation": "AWS S3 security best practices require enabling Block Public Access at the bucket and account level, mandating server-side encryption (SSE-KMS), enforcing strict IAM/bucket policies, and logging access via CloudTrail.",
        "scenario_context": "A financial technology startup is preparing its cloud infrastructure for a SOC 2 compliance audit."
    }
]
