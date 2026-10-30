import unittest
import json
from app import app
import database as db

class CyberCareerCopilotTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()

        # Clean test user if exists
        db.execute("DELETE FROM users WHERE email = 'cadet@test.edu'")

    def tearDown(self):
        db.execute("DELETE FROM users WHERE email = 'cadet@test.edu'")

    def test_01_registration_and_login(self):
        """Test student registration and login flow"""
        # Register new student
        resp = self.client.post('/register', data={
            'full_name': 'Test Cadet',
            'email': 'cadet@test.edu',
            'password': 'StrongPassword123!',
            'confirm_password': 'StrongPassword123!'
        }, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Student Cybersecurity Profile', resp.data)

        # Verify user in database
        user = db.query_one("SELECT * FROM users WHERE email = 'cadet@test.edu'")
        self.assertIsNotNone(user)
        self.assertEqual(user['full_name'], 'Test Cadet')

        # Logout
        resp = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Sign In to Cyber Copilot', resp.data)

        # Login
        resp = self.client.post('/login', data={
            'email': 'cadet@test.edu',
            'password': 'StrongPassword123!'
        }, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Cyber Career Command Center', resp.data)

    def test_02_profile_update_and_skill_gap(self):
        """Test profile updating and skill gap calculation"""
        # Register and login
        self.client.post('/register', data={
            'full_name': 'Alex Hunter',
            'email': 'cadet@test.edu',
            'password': 'StrongPassword123!',
            'confirm_password': 'StrongPassword123!'
        }, follow_redirects=True)

        # Update profile
        resp = self.client.post('/profile', data={
            'full_name': 'Alex Hunter',
            'qualification': 'B.Tech / B.E.',
            'department': 'Cyber Security',
            'year_of_study': '3rd Year',
            'programming_languages': ['Python', 'Bash', 'SQL'],
            'networking_skills': ['TCP/IP', 'Wireshark'],
            'os_skills': ['Linux (Ubuntu/Debian)', 'Kali Linux'],
            'cyber_level': 'Intermediate',
            'areas_of_interest': ['SOC Analysis', 'Incident Response'],
            'preferred_career': 'SOC Analyst',
            'weekly_study_hours': '15'
        }, follow_redirects=True)
        self.assertEqual(resp.status_code, 200)

        # Check skill gap analyzer
        resp = self.client.get('/skill-gap?career=SOC+Analyst')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Possessed Competencies', resp.data)
        self.assertIn(b'Role Readiness Index', resp.data)

    def test_03_roadmap_and_task_toggle(self):
        """Test roadmap generation and task toggle API"""
        self.client.post('/register', data={
            'full_name': 'Cadet Jordan',
            'email': 'cadet@test.edu',
            'password': 'StrongPassword123!',
            'confirm_password': 'StrongPassword123!'
        }, follow_redirects=True)

        resp = self.client.get('/roadmap')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Phase 1: Networking and Computer Fundamentals', resp.data)

        # Fetch first task
        user = db.query_one("SELECT id FROM users WHERE email = 'cadet@test.edu'")
        task = db.query_one("SELECT id, is_completed FROM roadmap_tasks WHERE user_id = %s LIMIT 1", (user['id'],))
        self.assertIsNotNone(task)
        self.assertEqual(task['is_completed'], 0)

        # Toggle task to completed
        resp = self.client.post('/api/toggle-task', 
            data=json.dumps({'task_id': task['id']}),
            content_type='application/json'
        )
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertTrue(data['success'])
        self.assertTrue(data['is_completed'])
        self.assertGreater(data['overall_progress'], 0)

    def test_04_interview_quiz_submission(self):
        """Test quiz question display and submission"""
        self.client.post('/register', data={
            'full_name': 'Quiz Taker',
            'email': 'cadet@test.edu',
            'password': 'StrongPassword123!',
            'confirm_password': 'StrongPassword123!'
        }, follow_redirects=True)

        resp = self.client.get('/interview')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Technical Cybersecurity Interview Practice', resp.data)

        # Fetch a quiz question
        question = db.query_one("SELECT * FROM quiz_questions LIMIT 1")
        self.assertIsNotNone(question)

        # Submit answer
        resp = self.client.post('/interview', data={
            'category': 'Networking',
            'question_ids': [str(question['id'])],
            f"question_{question['id']}": question['correct_option']
        })
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Score: 1 out of 1 Questions Correct', resp.data)
        self.assertIn(b'Technical Explanation', resp.data)

    def test_05_cyber_copilot_chatbot_api(self):
        """Test Cyber Copilot Chatbot API and demo mode transparency"""
        self.client.post('/register', data={
            'full_name': 'Chat Student',
            'email': 'cadet@test.edu',
            'password': 'StrongPassword123!',
            'confirm_password': 'StrongPassword123!'
        }, follow_redirects=True)

        resp = self.client.post('/api/chat',
            data=json.dumps({'message': 'How do I become a SOC Analyst?'}),
            content_type='application/json'
        )
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertTrue(data['success'])
        self.assertIn('SOC', data['response'])
        self.assertIn('mode', data)
        self.assertIn('DEMO MODE', data['response'])

if __name__ == '__main__':
    unittest.main()
