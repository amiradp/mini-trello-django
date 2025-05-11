# 🧩 Mini Trello – Django-based Task Management App

Mini Trello is a simplified Trello clone built with Django. It allows users to organize their work using Boards, Lists, and Cards, collaborate with others, and manage tasks visually.

---

## 📸 Demo

👉 [Live Demo](https://your-deployed-url.com)

> 🔐 Demo credentials:  
> Username: `demo_user`  
> Password: `demopassword`

---

## 🎯 Features

- ✅ User registration, login, logout, password reset
- ✅ Create and manage Boards, Lists, and Cards
- ✅ Invite members to boards with role-based access (owner, editor, viewer)
- ✅ Drag & Drop cards between lists
- ✅ Card details: description, checklist, deadline, labels, comments
- ✅ Responsive UI with clean custom CSS
- ✅ REST API for Boards and Cards (WIP)
- ✅ Real-time updates with WebSockets (optional)

---

## 🏗️ Tech Stack

| Layer         | Tech                              |
|---------------|-----------------------------------|
| Backend       | Django, Django REST Framework     |
| Frontend      | Django Templates / (React optional) |
| Database      | PostgreSQL / SQLite (dev)         |
| Auth          | Django built-in auth system       |
| Realtime (opt)| Django Channels                   |
| Deployment    | Render / Railway / Heroku         |

---

## ⚙️ Installation

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/mini-trello.git
cd mini-trello


2.Create virtual environment & install dependencies

python -m venv env
source env/bin/activate   # or env\Scripts\activate on Windows
pip install -r requirements.txt

3.Run migrations & start the server

python manage.py migrate
python manage.py runserver

4.Access app

http://127.0.0.1:8000/



📁 Project Structure

mini-trello/
├── core/           # User auth & profiles
├── boards/         # Boards, Lists, Cards models & logic
├── templates/      # HTML templates
├── static/         # Custom CSS & JS
├── api/ (opt)      # DRF APIs
├── requirements.txt
└── README.md


🚀 Upcoming Features
 REST API for full frontend integration

 WebSocket-based live sync (Django Channels)

 Google OAuth login

 Email notifications for board activity

🧠 Author
Made with ❤️ by Your Name

📜 License
This project is licensed under the MIT License.