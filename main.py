from tkinter import Tk
from controller.home_con import HomeController

root = Tk()
root.title("Quiz App")
root.geometry("420x600")
root.resizable(False, False)

app = HomeController(root)
root.mainloop()
