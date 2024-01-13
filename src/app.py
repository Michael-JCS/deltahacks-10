from tkinter import Tk
from profile import Profile
import tools

if __name__ == "__main__":
    root = Tk()
    my_gui = Profile(root)
    root.mainloop()