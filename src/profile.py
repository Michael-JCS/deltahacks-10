from tkinter import Tk, Label, Button, Frame, RAISED, SE, font as tkFont

class Profile(Tk):
    def __init__(self):
        super().__init__()

        self.data = {}

        self.title("Resume Roti")
        self.geometry('1920x1080')

        # Define a larger font
        large_font = tkFont.Font(family="Helvetica", size=20, weight="bold")

        # Create a Label widget with the larger font
        label = Label(self, text="Resume Filler", font=large_font)
        label.grid(row=0, column=0)

        # Initialize frames
        self.frames = {}
        for F in (PersonalInfo, Profiles, Projects, Education, Jobs):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=1, column=0, sticky="nsew")

        self.show_frame(PersonalInfo)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()

       
        
class PersonalInfo(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        label = Label(self, text="Personal Info")
        label.pack(pady=10, padx=10)

        next_button = Button(self, text="Next",
                                command=lambda: parent.show_frame(Profiles))
        next_button.pack()

class Profiles(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        label = Label(self, text="Second Page")
        label.pack(pady=10, padx=10)

        next_button = Button(self, text="Next",
                                command=lambda: parent.show_frame(Projects))
        next_button.pack()

class Projects(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        label = Label(self, text="Final Page")
        label.pack(pady=10, padx=10)

        # Add additional widgets or information here


class Education(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        label = Label(self, text="Final Page")
        label.pack(pady=10, padx=10)

        # Add additional widgets or information here

class Jobs(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        label = Label(self, text="Final Page")
        label.pack(pady=10, padx=10)

        # Add additional widgets or information here