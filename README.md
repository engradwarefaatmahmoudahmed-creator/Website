# Website | Sharaf Eldin – AI & Software Engineering

A professional full-stack web platform built with **Python and Django** for presenting software engineering services, programming courses, and company information.

## 🚀 Project Overview

**Website** is a Django-based web application designed to provide a modern and professional online presence for **Sharaf Eldin – AI & Software Engineering**.

The platform presents:

* Software engineering services
* Programming courses
* Course details and information
* Company information
* Contact form
* Featured services and courses
* Statistics section
* Responsive modern UI

## 🛠️ Technologies Used

* Python
* Django 5.2
* Django Templates
* HTML5
* CSS3
* Bootstrap 5
* Bootstrap Icons
* JavaScript
* SQLite
* Python Dotenv
* WhiteNoise
* Git & GitHub

## ✨ Features

### 🏠 Home Page

A modern landing page introducing the company, services, courses, and key statistics.

### 💼 Services

Displays available software engineering and development services with detailed information.

### 🎓 Programming Courses

Provides information about available programming courses, including:

* Course levels
* Course hours
* Number of lectures
* Course details
* Featured courses

### 📩 Contact System

A contact form that allows visitors to send messages directly through the website.

### 📊 Statistics

Displays important project and business statistics in a clean and modern layout.

### 📱 Responsive Design

The website is designed to work across:

* Desktop
* Laptop
* Tablet
* Mobile devices

## 📁 Project Structure

```text
Website/
│
├── core/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── service_course/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── templates/
│   ├── includes/
│   ├── base.html
│   ├── home.html
│   ├── courses.html
│   ├── course_detail.html
│   ├── services.html
│   ├── service_detail.html
│   └── contact.html
│
├── media/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/engradwarefaatmahmoudahmed-creator/Website.git
cd Website
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root and add the required environment variables.

Example:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
```

### 6. Run Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## 🔐 Security

Sensitive configuration is stored using environment variables.

The following files and directories are excluded from Git:

* `.env`
* `venv/`
* `db.sqlite3`
* `__pycache__/`
* `staticfiles/`

## 🎯 Project Goals

The project was developed to provide:

* A professional company website
* A platform for presenting programming courses
* A clean Django backend architecture
* Responsive frontend design
* Practical experience with Django development
* A portfolio-ready software engineering project

## 👩‍💻 Developer

**Radwa Refaat Mahmoud Ahmed**

Backend Django Developer | Python & Django Instructor | Software Engineer

### 📌 Project

**Website – Sharaf Eldin | AI & Software Engineering**

Built with ❤️ using Python & Django.

## ⭐ Future Improvements

Planned improvements may include:

* User authentication
* Online course enrollment
* Payment integration
* Student dashboard
* REST API
* Django REST Framework integration
* Real-time notifications
* Deployment to a production server
