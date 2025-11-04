from view.home import HomeFrame
from model.home_model import HomeModel

class HomeController:
    def __init__(self, root):
        self.root = root
        self.model = HomeModel()  

        
        categories = self.model.get_categories()   #this to get the categlory model

        # Pass them to the view
        self.home = HomeFrame(root, self, categories)
        self.home.pack(fill="both", expand=True)

    def category_selection(self, category_name):
        print(f"Selected: {category_name}")
        # we can later change to the quiz framer
