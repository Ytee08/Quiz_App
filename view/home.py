#this is the home of the quiz app. this ius the code for the view
import tkinter as tk



COLORS = {
    "bg": "#1C2333",        
    
}

root = tk.Tk()
root.title("Quiz App")
root.geometry("420x600")
root.configure(bg=COLORS["bg"])
root.resizable(False, False)






root.mainloop()