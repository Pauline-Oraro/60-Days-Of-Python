# 60 Days of Python — Flask Web App 🐍

A simple web application built with **Python (Flask)** and **Jinja2 templating** as part of the **60 Days of Python Challenge**. The app includes a home page and an about page.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Pages](#pages)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Template Breakdown](#template-breakdown)
- [Getting Started](#getting-started)
- [Jinja2 Templating Reference](#jinja2-templating-reference)
- [Important Notes](#important-notes)

---

## Overview

This is a simple Flask web application that demonstrates:

- Multi-page routing with Flask
- Jinja2 template inheritance using a shared base layout
- Dynamic page titles
- Passing variables from Flask into templates

---

## 📄 Pages

| Page | Route | Description |
|------|-------|-------------|
| **Home** | `/` | A simple home page |
| **About** | `/about` | Displays information about the 60 Days of Python challenge |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core programming language |
| **Flask** | Web framework for routing and backend logic |
| **Jinja2** | Templating engine for rendering dynamic HTML |
| **HTML/CSS** | Frontend structure and styling |
| **Google Fonts** | Typography — Lato, Nunito, Raleway |

---

## 📁 Project Structure

```
project/
│
├── templates/
│   ├── layout.html       # Base template — shared navbar, head, and structure
│   ├── home.html         # Home page — text form (extends layout.html)
│   └── about.html        # About page (extends layout.html)
│
├── static/
│   └── main.css          # Stylesheet
│
├── app.py                # Flask application, routes and logic
└── README.md             # Project documentation
```

---

## 🧩 Template Breakdown

### `layout.html` — Base Template

The base template is the **shared skeleton** of the entire app. All other pages extend it.

```html
{% if title %}
<title>60 Days of Python - {{ title }}</title>
{% else %}
<title>60 Days of Python</title>
{% endif %}
```

- If a page passes a `title` variable from Flask, it is included in the page title
- Otherwise a default title is used
- This makes each page have a unique, meaningful browser tab title

```html
<a class="brand-name nav-link" href="/">60DaysOfPython</a>
```

- The brand name in the navbar links back to the home page

```html
<a href="{{ url_for('home') }}">Home</a>
<a href="{{ url_for('about') }}">About</a>
```

- `url_for()` generates URLs dynamically from Flask function names
- This is safer than hardcoding URLs — if a route changes, the links update automatically

```html
{% block content %} {% endblock %}
```

- This is the **content placeholder** — each child template fills this in with its own unique content

---

### `home.html` — Home Page

```html
{% extends 'layout.html' %}
{% block content %}
  ...
{% endblock %}
```

- Inherits the full layout from `layout.html`
- Only defines the content unique to the home page

---

### `about.html` — About Page

```html
<h1>About {{name}}</h1>
```

- `{{ name }}` is a **Jinja2 variable** — the value is passed in from Flask when the route is called
- For example, in `app.py`: `return render_template('about.html', name='Pauline')`

```html
<p>
  This is a 60 days of python programming challenge. If you have been coding
  this far, you are awesome. Congratulations for the job well done!
</p>
```

> **Note:** The `{% extends %}` and `{% block %}` tags in `about.html` must be at the top level of the file, not nested inside `<body>` tags — Jinja2 processes templates before the HTML is rendered.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/60-days-python-flask.git
cd 60-days-python-flask
```

2. **Create and activate a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
python app.py
```

5. **Open in your browser**

```
http://127.0.0.1:5000
```

---

## 🧠 Jinja2 Templating Reference

| Syntax | Purpose | Example |
|--------|---------|---------|
| `{{ }}` | Output a variable | `{{ name }}` |
| `{% %}` | Logic/control statement | `{% if title %}` |
| `{# #}` | Comment (not rendered in HTML) | `{# TODO: fix this #}` |
| `{% extends %}` | Inherit from a parent template | `{% extends 'layout.html' %}` |
| `{% block %}` | Define a replaceable section | `{% block content %}{% endblock %}` |
| `url_for()` | Generate a URL from a Flask function name | `{{ url_for('home') }}` |

### Why Use Template Inheritance?

- **DRY** (Don't Repeat Yourself) — write the navbar and footer only once
- **Consistency** — every page shares the same structure automatically
- **Maintainability** — update the layout in one file and all pages update
- **Scalability** — adding new pages is as simple as creating a new file that extends the layout

---

## 📌 Important Notes

- `{% extends %}` must always be the **very first line** of a child template — placing it inside `<body>` tags will break the template.
- `url_for('home')` references the **Flask function name**, not the route path — make sure function names match exactly.
- The `{{ url_for('static', filename='main.css') }}` in `layout.html` is the correct Flask way to reference static files — never hardcode paths to static assets
- Variables like `{{ name }}` and `{{ title }}` must be passed explicitly from the Flask route using `render_template()` — they are not available automatically

---

## 👩‍💻 Author

**Pauline Oraro**
60 Days of Python Challenge

---
