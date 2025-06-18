# 📝 Django To-Do App

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-4.x-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Fly.io-blueviolet)
[![Deploy on Fly.io](https://img.shields.io/badge/Deployed-Fly.io-orange)](https://django-to-do-app.fly.dev)

A simple yet functional task management web application built with Django and deployed using [Fly.io](https://fly.io).

## 🚀 Live Demo

👉 [django-to-do-app.fly.dev](https://django-to-do-app.fly.dev)

## 📦 Features

- User authentication (login/logout/register)
- Create, view, edit, and delete tasks
- Task scheduling with due dates, comments and CRUD functionality too.
- Admin dashboard for managing users and tasks
- Responsive layout using TailwindCSS

## 💻 Tech Stack
- **Backend:** Django (Python)
- **Database:** PostgreSQL (via Fly.io)
- **Deployment:** Fly.io
- **Tools:** Docker, Git


## ⚙️ Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/pablo727/to_do_app.git
   cd to_do_app

2. Create a virtual environment and activate it:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Windows: venv\Scripts\activate
  ```
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
4. Run migrations and start the server:
  ```bash
  python manage.py migrate
  python manage.py runserver
  ```
5. Visit http://127.0.0.1:8000/ in your browser.

## 📄 License
MIT License. Use freely, credit appreciated.
