# 🎓 UCU Chapters Registration System

A modern web-based registration platform for **Uganda Christian University (UCU)** student chapters, enabling students to register, verify, and track their membership status in various academic and tech-related societies.

---

## 🚀 Features

✅ Student registration with validation  
✅ Select from multiple chapters:
- Cyber Security
- AI & Robotics
- Software Engineering
- Gaming & Innovation  

✅ Track your registration status in real time  
✅ Verifies Student IDs and course information  
✅ Beautiful responsive UI built with Bootstrap 5  
✅ Admin panel for managing registrations  

---

## 🛠 Tech Stack

| Tool         | Description                     |
|--------------|---------------------------------|
| **Django**   | Backend framework (v4.x)        |
| **SQLite**   | Lightweight local DB            |
| **Bootstrap**| Frontend styling (v5.3.2)       |
| **FontAwesome** | Icon library (v6.0.0)        |
| **HTML/CSS** | Templating and UI styling       |

---

## 📁 Project Structure


---

## ⚙️ Installation & Setup

1. **Clone the Repository**

```bash
git clone <your-repo-url>
cd UCUChapters


Create a Virtual Environment

bash
Copy code
python -m venv venv
# For Windows
venv\Scripts\activate
# For Mac/Linux
source venv/bin/activate


Install Dependencies

bash
Copy code
pip install -r requirements.txt


Run Migrations

bash
Copy code
python manage.py migrate

Start the Development Server

bash
Copy code
python manage.py runserver


Visit the App

Open your browser and go to:
👉 http://127.0.0.1:8000/