#ABBAS MUHAMMAD YUSUF
#MAAUN/24/CSC/0052

# 🏢 BizConnect NG — Local Business & Startup Directory

A Flask web application for CSC 202 Continuous Assessment.  
Discover, list, and manage local businesses and startups in your community.

---

## 📌 What the App Does

**BizConnect NG** is a community-facing web app where users can:

- 📋 **View all businesses** listed in the directory, with category filtering
- ➕ **Add a new business** by filling out a form (name, category, description, location, contact)
- 🕐 **See recently added businesses** — powered by a LIFO Stack data structure
- ↩ **Undo the last addition** using Stack Pop
- 🔍 **View full details** of any listed business

### Tech Stack
- **Backend:** Python 3, Flask
- **Frontend:** HTML5, CSS3 (Jinja2 templates)
- **Data:** In-memory (Python classes, no database needed)

---

## 🚀 How to Run the Flask App Locally

Follow these steps carefully — beginner friendly!

### Step 1: Make sure Python is installed
Open your terminal (Command Prompt on Windows, Terminal on Mac/Linux) and type:
```bash
python --version
```
You should see something like `Python 3.10.x`. If not, download Python from [python.org](https://www.python.org/downloads/).

---

### Step 2: Download or clone the project
If you have Git installed:
```bash
git clone https://github.com/YOUR_USERNAME/bizconnect-ng.git
cd bizconnect-ng
```
Or just download the ZIP from GitHub and extract it.

---

### Step 3: Install Flask
In the project folder, run:
```bash
pip install Flask
```
Or use the requirements file:
```bash
pip install -r requirements.txt
```

---

### Step 4: Run the app
```bash
python app.py
```
You should see:
```
 * Running on http://127.0.0.1:5000
```

---

### Step 5: Open in your browser
Go to: **http://127.0.0.1:5000**

That's it! 🎉 The app will be running locally on your computer.

---

## 📁 Project Structure

```
bizconnect-ng/
├── app.py              # Flask routes and app logic
├── models.py           # OOP classes: Business, BusinessDirectory
├── requirements.txt    # Python dependencies
├── README.md           # This file
├── templates/          # HTML pages (Jinja2)
│   ├── base.html       # Shared layout (navbar, footer)
│   ├── index.html      # Home page — all businesses
│   ├── add.html        # Add business form
│   ├── recent.html     # Recently added (LIFO stack)
│   └── detail.html     # Business detail page
└── static/
    └── css/
        └── style.css   # App styles
```

---

## 📚 Core Requirements Met

| Requirement | How It's Implemented |
|---|---|
| OOP (Class + `__init__` + methods) | `Business` class in `models.py` with `get_summary()`, `is_recently_added()`, `to_dict()` |
| Data Structure (Stack LIFO) | `_recently_added_stack` in `BusinessDirectory` with push/pop/peek operations |
| Standard API (datetime) | `datetime.now()` used to timestamp every new business entry |
| Flask Web UI (2+ routes) | 5 routes: `/`, `/add`, `/recent`, `/business/<id>`, `/undo` |
| GitHub (20+ commits) | Committed incrementally with clear messages |

---

## 👤 Author
**[Your Name]** — CSC 202, [Your University]
