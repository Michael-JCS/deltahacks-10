from tkinter import Tk, Label, Button, Frame, RAISED, SE

class Profile:
    def __init__(self, master):
        self.master = master
        
        master.title("A simple GUI")

        self.framePhoto = Frame(master, bg='gray50',relief = RAISED, width=800, height=600, bd=4)
        prevBtn = Button(self.framePhoto, text='Previous', command=master.quit)


        nextBtn = Button(self.framePhoto, text='Next', command=master.quit,
                        bg='green', fg='black')

        self.label = Label(master, text="Profile.py")
        self.label.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
    
    def run():
        return