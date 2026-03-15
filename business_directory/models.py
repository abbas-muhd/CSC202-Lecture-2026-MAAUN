#ABBAS MUHAMMAD YUSUF
#MAAUN/24/CSC/0052

"""
models.py - OOP classes for the Local Business/Startup Directory App
Uses: Classes with __init__ and custom methods, Stack (LIFO) data structure,
      datetime module for timestamping
"""

from datetime import datetime


class Business:
    """Represents a local business or startup listing."""

    def __init__(self, name: str, category: str, description: str, location: str, contact: str):
        self.name = name
        self.category = category
        self.description = description
        self.location = location
        self.contact = contact
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.id = None  # Will be assigned by the directory

    def get_summary(self) -> str:
        """Returns a short summary string for the business."""
        return f"{self.name} ({self.category}) - {self.location}"

    def is_recently_added(self, hours: int = 24) -> bool:
        """Returns True if the business was added within the last `hours` hours."""
        added_time = datetime.strptime(self.timestamp, "%Y-%m-%d %H:%M:%S")
        delta = datetime.now() - added_time
        return delta.total_seconds() < hours * 3600

    def to_dict(self) -> dict:
        """Converts the business object to a dictionary for template rendering."""
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "description": self.description,
            "location": self.location,
            "contact": self.contact,
            "timestamp": self.timestamp,
            "is_recent": self.is_recently_added(),
        }

    def __repr__(self):
        return f"<Business: {self.name} | {self.category}>"


class BusinessDirectory:
    """
    Manages the collection of businesses.
    Uses a Stack (LIFO) to track recently added businesses.
    """

    def __init__(self):
        self._businesses: list = []          # Main list of all businesses
        self._recently_added_stack: list = [] # Stack (LIFO) for recently added
        self._next_id: int = 1

    def add_business(self, business: Business) -> Business:
        """Adds a new business to the directory and pushes it onto the recent stack."""
        business.id = self._next_id
        self._next_id += 1

        self._businesses.append(business)
        # Stack push — LIFO: most recent is at the top (end of list)
        self._recently_added_stack.append(business)

        return business

    def get_all_businesses(self) -> list:
        """Returns all businesses as a list of dicts."""
        return [b.to_dict() for b in self._businesses]

    def get_recently_added(self, count: int = 5) -> list:
        """
        Returns the most recently added businesses using LIFO stack logic.
        Peeks the top `count` items without removing them.
        """
        # Stack peek: read from the end (top of stack)
        recent = self._recently_added_stack[-count:][::-1]
        return [b.to_dict() for b in recent]

    def get_by_category(self, category: str) -> list:
        """Filters businesses by category."""
        filtered = [b for b in self._businesses if b.category.lower() == category.lower()]
        return [b.to_dict() for b in filtered]

    def get_categories(self) -> list:
        """Returns a sorted list of unique categories."""
        return sorted(set(b.category for b in self._businesses))

    def get_business_by_id(self, business_id: int):
        """Finds a business by its ID."""
        for b in self._businesses:
            if b.id == business_id:
                return b.to_dict()
        return None

    def total_count(self) -> int:
        """Returns the total number of businesses."""
        return len(self._businesses)

    def undo_last_add(self):
        """
        Removes the most recently added business using Stack pop (LIFO).
        This is the 'Undo' feature powered by the stack.
        """
        if not self._recently_added_stack:
            return None

        # Stack pop — remove from top (end)
        last_business = self._recently_added_stack.pop()

        # Also remove from main list
        self._businesses = [b for b in self._businesses if b.id != last_business.id]
        return last_business.to_dict()

    def __repr__(self):
        return f"<BusinessDirectory: {self.total_count()} businesses>"


# ──────────────────────────────────────────────
# Pre-load some sample data
# ──────────────────────────────────────────────

def create_sample_directory() -> BusinessDirectory:
    """Creates a BusinessDirectory pre-loaded with sample businesses."""
    directory = BusinessDirectory()

    samples = [
        Business("TechHub NG", "Technology", "Co-working space and startup incubator for tech entrepreneurs.", "Lagos, Nigeria", "techhub@example.com"),
        Business("Green Bites Café", "Food & Beverage", "Healthy, locally sourced meals and fresh juices.", "Abuja, Nigeria", "greenbites@example.com"),
        Business("QuickFix Repairs", "Services", "Fast and reliable phone and laptop repair services.", "Lagos, Nigeria", "quickfix@example.com"),
        Business("EduBridge Academy", "Education", "Affordable coding bootcamp for secondary school students.", "Port Harcourt, Nigeria", "edubridge@example.com"),
        Business("FreshFarm Organics", "Agriculture", "Farm-fresh vegetables and fruits delivered to your door.", "Ibadan, Nigeria", "freshfarm@example.com"),
    ]

    for business in samples:
        directory.add_business(business)

    return directory
