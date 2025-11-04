#this is the home of the quiz app. this ius the code for the view

import tkinter as tk

# COLORS
COLORS = {
    "bg": "#1C2333",        
    "categlory": "#2E3A59",       
    "select": "#FF8C32",    
    "text": "#FFFFFF",  
    "muted": "#A9B4C2",     
}

# --- Main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("420x600")
root.configure(bg=COLORS["bg"])
root.resizable(False, False)

# Home 
home_frame = tk.Frame(root, bg=COLORS["bg"])
home_frame.pack(fill="both", expand=True)

# Title
title_label = tk.Label(
    home_frame,
    text="Quiz App 🧠",
    bg=COLORS["bg"],
    fg=COLORS["text"],
    font=("Segoe UI", 22, "bold"),
    pady=20
)
title_label.pack()

# Subtitle
subtitle_label = tk.Label(
    home_frame,
    text="Choose a category to start",
    bg=COLORS["bg"],
    fg=COLORS["muted"],
    font=("Segoe UI", 12)
)
subtitle_label.pack(pady=(0, 20))

# Category Buttons
categories = ["Beginner", "Intermidate", "Pro"]

for cat in categories:
    btn = tk.Button(
        home_frame,
        text=cat,
        bg=COLORS["categlory"],
        fg=COLORS["text"],
        activebackground=COLORS["select"],
        activeforeground=COLORS["text"],
        font=("Segoe UI", 12),
        relief="flat",
        width=25,
        pady=8
    )
    btn.pack(pady=8)

# Footer
footer = tk.Label(
    home_frame,
    text="© 2025 Quiz App",
    bg=COLORS["bg"],
    fg=COLORS["muted"],
    font=("Segoe UI", 9)
)
footer.pack(side="bottom", pady=10)

root.mainloop()
