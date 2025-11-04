class HomeModel:
    def __init__(self):
        
        self.categories = ["Beginner", "Intermediate", "Pro"]

    def get_categories(self):
        """Return the list of available categories."""
        return self.categories
