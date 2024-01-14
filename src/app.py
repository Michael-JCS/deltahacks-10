from tkinter import Tk
from profile import Profile
import tools

if __name__ == "__main__":
    root = Profile()
    root.geometry('1920x1080')
    root.grid_columnconfigure(0,weight=1)
    root.mainloop()