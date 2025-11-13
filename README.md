🐍 Django Learning Journey — by Eswar Chandra Yadlapalli
📘 Overview

This repository documents my day-by-day learning progress of Django — a powerful Python web framework.
Each day’s code and notes reflect both theoretical understanding and practical implementation.

📅 Day 1 — Django Fundamentals

Understanding Software Types — System, Application, Standalone, Web, and Client-Server.

Introduction to Software Architectures — One-Tier, Two-Tier, N-Tier.

Framework Basics — Major vs. Micro frameworks.

Django Framework Introduction and MVC/MVT Design Patterns.

Installed Django and created the first project.

Studied the purpose of each file inside a Project Folder and App Folder.

Learned to run the Django server and view project output.

🔗 Topics Covered: Project creation, folder structure, command line usage, server start.
📂 Commit: Day-1 Django Learning

📅 Day 2 — URLs, Views, Templates & Static Files

Created multiple views with HttpResponse and render().

Learned URL Mapping — generic and specific.

Configured Template Directories (generic & app-level).

Created and connected HTML pages (base.html, home.html, about.html, contact.html).

Understood Jinja Tagging ({% block %}, {% extends %}, {% static %}).

Created and registered static files (CSS, JS, Images) in settings.py.

🔗 Topics Covered: Template Inheritance, Static files setup, URL flow understanding.
📂 Commit: Day-2 Django Learning

📅 Day 3 — Models, ORM & Admin Panel

Created a new Django App (students) and registered it in the project.

Defined Models and explored how Django interacts with databases.

Applied migrations (makemigrations & migrate).

Registered models in admin.py for admin panel management.

Displayed model data dynamically on HTML templates using views and ORM queries.

Deep dive into Django’s Request-Response Flow.

🔗 Topics Covered: Models, Database ORM, Admin Panel, Template Rendering.
📂 Commit: Day-3 Django Learning

⚙️ Tech Stack

Language: Python (v3.12)

Framework: Django (v5.2.8)

Frontend: HTML5, CSS3 (Static files)

Tools: VS Code, Git, PowerShell

Version Control: Git & GitHub

🚀 How to Run the Project
# Clone the repository
git clone https://github.com/ESWAR-CHANDRA-YADLAPALLI-2003/django_learning.git

# Navigate into the project
cd django_learning/myproject

# Activate virtual environment
.\venv\Scripts\activate

# Run the development server
python manage.py runserver
