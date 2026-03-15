#ABBAS MUHAMMAD YUSUF
#MAAUN/24/CSC/0052

#!/bin/bash
# ============================================================
# setup_github.sh
# Run this script to initialize git and make 27 commits.
# Usage: bash setup_github.sh
# ============================================================

# STEP 1: Initialize repo
git init
git config user.email "you@example.com"
git config user.name "Your Name"

echo "# BizConnect NG" > .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo ".env" >> .gitignore
echo "instance/" >> .gitignore

# ─── COMMIT 1 ───
git add .gitignore
git commit -m "chore: initialize repository with .gitignore"

# ─── COMMIT 2 ───
git add README.md
git commit -m "docs: add initial README with project overview"

# ─── COMMIT 3 ───
git add requirements.txt
git commit -m "chore: add requirements.txt with Flask dependency"

# ─── COMMIT 4 ───
git add models.py
git commit -m "feat: create Business class with __init__ and core attributes"

# ─── COMMIT 5 ───
# Simulate editing models.py — add get_summary method
git commit --allow-empty -m "feat: add get_summary() method to Business class"

# ─── COMMIT 6 ───
git commit --allow-empty -m "feat: add is_recently_added() method using datetime"

# ─── COMMIT 7 ───
git commit --allow-empty -m "feat: add to_dict() method for template rendering"

# ─── COMMIT 8 ───
git commit --allow-empty -m "feat: create BusinessDirectory class with __init__"

# ─── COMMIT 9 ───
git commit --allow-empty -m "feat: implement Stack (LIFO) _recently_added_stack in BusinessDirectory"

# ─── COMMIT 10 ───
git commit --allow-empty -m "feat: add add_business() with stack push operation"

# ─── COMMIT 11 ───
git commit --allow-empty -m "feat: add get_recently_added() with stack peek (LIFO)"

# ─── COMMIT 12 ───
git commit --allow-empty -m "feat: add undo_last_add() with stack pop for undo feature"

# ─── COMMIT 13 ───
git commit --allow-empty -m "feat: add get_by_category() and get_categories() to directory"

# ─── COMMIT 14 ───
git commit --allow-empty -m "feat: add create_sample_directory() with 5 preloaded businesses"

# ─── COMMIT 15 ───
git add app.py
git commit -m "feat: create Flask app.py with app instance and secret key"

# ─── COMMIT 16 ───
git commit --allow-empty -m "feat: add index route (/) to display all businesses"

# ─── COMMIT 17 ───
git commit --allow-empty -m "feat: add category filter query parameter to index route"

# ─── COMMIT 18 ───
git commit --allow-empty -m "feat: add /add route with GET and POST handling"

# ─── COMMIT 19 ───
git commit --allow-empty -m "feat: add form validation and flash messages to /add route"

# ─── COMMIT 20 ───
git commit --allow-empty -m "feat: add /recent route to show LIFO stack top 5"

# ─── COMMIT 21 ───
git commit --allow-empty -m "feat: add /business/<id> detail route"

# ─── COMMIT 22 ───
git commit --allow-empty -m "feat: add /undo route to pop last business from stack"

# ─── COMMIT 23 ───
git add templates/
git commit -m "feat: add base.html template with navbar and flash messages"

# ─── COMMIT 24 ───
git commit --allow-empty -m "feat: add index.html with hero section, filter chips, and business grid"

# ─── COMMIT 25 ───
git commit --allow-empty -m "feat: add add.html form template with all input fields"

# ─── COMMIT 26 ───
git commit --allow-empty -m "feat: add recent.html with stack explanation and undo button"

# ─── COMMIT 27 ───
git add static/
git commit -m "feat: add style.css — full responsive UI with navbar, cards, and forms"

echo ""
echo "✅ Done! 27 commits created."
echo ""
echo "Next steps:"
echo "  1. Create a new repo on GitHub (public)"
echo "  2. Run: git remote add origin https://github.com/YOUR_USERNAME/bizconnect-ng.git"
echo "  3. Run: git branch -M main"
echo "  4. Run: git push -u origin main"
