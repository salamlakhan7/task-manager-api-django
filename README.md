# Task Manager API (Django + DRF)

A production-ready Task Management REST API built with Django and Django REST Framework.

## Features
- JWT Authentication (Login / Refresh)
- User Signup
- Secure CRUD for Tasks
- User-based ownership
- Protected endpoints

## Tech Stack
- Django
- Django REST Framework
- SimpleJWT

## Endpoints
- POST /api/auth/signup/
- POST /api/auth/login/
- POST /api/auth/refresh/
- GET /api/tasks/
- POST /api/tasks/
- PATCH /api/tasks/{id}/
- DELETE /api/tasks/{id}/

## How to Run
```bash
pip install -r requirements.txt
python manage.py runserver
