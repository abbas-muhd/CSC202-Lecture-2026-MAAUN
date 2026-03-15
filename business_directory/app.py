#ABBAS MUHAMMAD YUSUF
#MAAUN/24/CSC/0052

"""
app.py - Flask Web Application for Local Business/Startup Directory
Routes: Home (view all), Add Business, Recently Added, Category Filter, Undo
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from models import Business, BusinessDirectory, create_sample_directory
from datetime import datetime

app = Flask(__name__)
app.secret_key = "business_directory_secret_2024"

# ── In-memory directory instance (persists for app lifetime) ──
directory = create_sample_directory()


# ─────────────────────────────────────────────
# Route 1: Home Page — View All Businesses
# ─────────────────────────────────────────────
@app.route("/")
def index():
    """Home page: display all businesses with optional category filter."""
    category_filter = request.args.get("category", "")
    
    if category_filter:
        businesses = directory.get_by_category(category_filter)
    else:
        businesses = directory.get_all_businesses()

    categories = directory.get_categories()
    total = directory.total_count()
    now = datetime.now().strftime("%B %d, %Y %H:%M")

    return render_template(
        "index.html",
        businesses=businesses,
        categories=categories,
        total=total,
        selected_category=category_filter,
        now=now,
    )


# ─────────────────────────────────────────────
# Route 2: Add Business Page (GET + POST)
# ─────────────────────────────────────────────
@app.route("/add", methods=["GET", "POST"])
def add_business():
    """Form to add a new business listing."""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        category = request.form.get("category", "").strip()
        description = request.form.get("description", "").strip()
        location = request.form.get("location", "").strip()
        contact = request.form.get("contact", "").strip()

        # Basic validation
        if not all([name, category, description, location, contact]):
            flash("All fields are required. Please fill in every field.", "error")
            return render_template("add.html", form_data=request.form)

        new_business = Business(name, category, description, location, contact)
        directory.add_business(new_business)

        flash(f'"{name}" has been successfully added to the directory!', "success")
        return redirect(url_for("index"))

    return render_template("add.html", form_data={})


# ─────────────────────────────────────────────
# Route 3: Recently Added Page
# ─────────────────────────────────────────────
@app.route("/recent")
def recently_added():
    """Shows the 5 most recently added businesses (LIFO stack peek)."""
    recent = directory.get_recently_added(count=5)
    return render_template("recent.html", businesses=recent)


# ─────────────────────────────────────────────
# Route 4: Business Detail Page
# ─────────────────────────────────────────────
@app.route("/business/<int:business_id>")
def business_detail(business_id):
    """Shows full details for a single business."""
    business = directory.get_business_by_id(business_id)
    if not business:
        flash("Business not found.", "error")
        return redirect(url_for("index"))
    return render_template("detail.html", business=business)


# ─────────────────────────────────────────────
# Route 5: Undo Last Add
# ─────────────────────────────────────────────
@app.route("/undo", methods=["POST"])
def undo_last():
    """Removes the most recently added business (Stack pop — LIFO undo feature)."""
    removed = directory.undo_last_add()
    if removed:
        flash(f'Undo successful! "{removed["name"]}" has been removed.', "info")
    else:
        flash("Nothing to undo — the directory is empty.", "warning")
    return redirect(url_for("recently_added"))


# ─────────────────────────────────────────────
# Run the app
# ─────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)
