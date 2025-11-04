import tkinter as tk

COLORS = {
    "bg": "#1C2333",        
    "category": "#2E3A59",       
    "select": "#FF8C32",    
    "text": "#FFFFFF",  
    "muted": "#A9B4C2",     
}

class HomeFrame(tk.Frame):
    def __init__(self, root, controller,categories):
        super().__init__(root, bg=COLORS["bg"])
        self.controller = controller
        self.categories = categories
        self.widgets()

    def widgets(self):
        # Title
        title_label = tk.Label(
            self,
            text="Quiz App 🧠",
            bg=COLORS["bg"],
            fg=COLORS["text"],
            font=("Segoe UI", 22, "bold"),
            pady=20
        )
        title_label.pack()

        # Subtitle
        subtitle_label = tk.Label(
            self,
            text="Choose a category to start",
            bg=COLORS["bg"],
            fg=COLORS["muted"],
            font=("Segoe UI", 12)
        )
        subtitle_label.pack(pady=(0, 20))

        # Category Buttons
    
        for cat in self.categories:
            btn = tk.Button(
                self,
                text=cat,
                bg=COLORS["category"],
                fg=COLORS["text"],
                activebackground=COLORS["select"],
                activeforeground=COLORS["text"],
                font=("Segoe UI", 12),
                relief="flat",
                width=25,
                pady=8,
                command=lambda c=cat: self.controller.category_selection(c)
            )
            btn.pack(pady=8)

        
