# Portfolio Site

A Django-based portfolio website where you can showcase your projects, display contact information, and integrate with your GitHub/LinkedIn profile.

---

## Features
- List all your projects with images, descriptions, and links.
- Contact form for visitors.
- Admin panel to manage projects.
- Bootstrap styling for clean UI.
- Django REST Framework API.
- Neon DB

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/E-Nincy/PortfolioSite.git
cd PortfolioSite

#Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Rum migrations
python manage.py makemigrations
python manage.py migrate

#Create superuser
python manage.py createsuperuser

# Run locally
python manage.py runserver

# Deployment

You can deploy on:

Render (simple PaaS hosting)

Azure VM (manual setup with Gunicorn + Nginx)

# Tests

Run:

python manage.py test

# License
MIT License
```
