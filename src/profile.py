from tkinter import Tk, Label, Button, Frame, RAISED, SE, font as tkFont, Entry
from db import set_education_info, set_info, set_job_info

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
        
        # Configure the grid
        self.grid_columnconfigure(0, weight=1)  # Configure columns to expand
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)     # Configure rows to expand
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        # Define a larger font
        large_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        largest_font = tkFont.Font(family="Helvetica", size=25, weight="bold")
        regular_font = tkFont.Font(family="Helvetica", size=20)

        # Widgets
        label = Label(self, text="Personal Info", font=largest_font)
        label.grid(row=0, columnspan=2, sticky="w")

        nameLabel = Label(self, text="Name:", font=large_font)
        nameLabel.grid(row=1, column=0, sticky="w")

        self.nameEntry = Entry(self, font=regular_font)
        self.nameEntry.grid(row=1, column=1, sticky="ew")

        phoneLabel = Label(self, text="Phone Number:", font=large_font)
        phoneLabel.grid(row=2, column=0, sticky="w")

        self.phoneEntry = Entry(self, font=regular_font)
        self.phoneEntry.grid(row=2, column=1, sticky="ew", pady=100)

        emailLabel = Label(self, text="Email:", font=large_font)
        emailLabel.grid(row=3, column=0, sticky="w")

        self.emailEntry = Entry(self, font=regular_font)
        self.emailEntry.grid(row=3, column=1, sticky="ew")

        next_button = Button(self, text="Next", command=lambda: (parent.show_frame(Education), self.read_data))
        next_button.grid(row=8, column=1, columnspan=1, sticky="ew")

        # Set the frame to expand
        self.grid(sticky="nsew")
    
    def read_data(self):
        set_info("jack133003", "name", self.nameEntry.get())
        set_info("jack133003", "phone", self.phoneEntry.get())
        set_info("jack133003", "email", self.emailEntry.get())


class Profiles(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        # Configure the grid
        self.grid_columnconfigure(0, weight=1)  # Configure columns to expand
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)     # Configure rows to expand
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        # Define a larger font
        large_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        largest_font = tkFont.Font(family="Helvetica", size=25, weight="bold")
        regular_font = tkFont.Font(family="Helvetica", size=20)

        # Widgets
        label = Label(self, text="Profiles", font=largest_font)
        label.grid(row=0, columnspan=2, sticky="w")

        linkedinLabel = Label(self, text="LinkedIn:", font=large_font)
        linkedinLabel.grid(row=1, column=0, sticky="w")

        self.linkedInEntry = Entry(self, font=regular_font)
        self.linkedInEntry.grid(row=1, column=1, sticky="ew")

        gitHubLabel = Label(self, text="GitHub:", font=large_font)
        gitHubLabel.grid(row=2, column=0, sticky="w")

        self.gitHubEntry = Entry(self, font=regular_font)
        self.gitHubEntry.grid(row=2, column=1, sticky="ew", pady=100)

        next_button = Button(self, text="Next", command=lambda: (parent.show_frame(Projects), self.read_data))
        next_button.grid(row=8, column=1, columnspan=1, sticky="ew")

        # Set the frame to expand
        self.grid(sticky="nsew")

    
    def read_data(self):
        set_education_info("jack133003", "linkedin", self.linkedInEntry.get())
        set_education_info("jack133003", "github", self.gitHubEntry.get())
    
        

class Projects(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        label = Label(self, text="Final Page")
        label.pack(pady=10, padx=10)

        # Configure the grid
        self.grid_columnconfigure(0, weight=1)  # Configure columns to expand
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)     # Configure rows to expand
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        # Define a larger font
        large_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        largest_font = tkFont.Font(family="Helvetica", size=25, weight="bold")
        regular_font = tkFont.Font(family="Helvetica", size=20)

        # Widgets
        label = Label(self, text="Profiles", font=largest_font)
        label.grid(row=0, columnspan=2, sticky="w")

        linkedinLabel = Label(self, text="LinkedIn:", font=large_font)
        linkedinLabel.grid(row=1, column=0, sticky="w")

        self.linkedInEntry = Entry(self, font=regular_font)
        self.linkedInEntry.grid(row=1, column=1, sticky="ew")

        gitHubLabel = Label(self, text="GitHub:", font=large_font)
        gitHubLabel.grid(row=2, column=0, sticky="w")

        self.gitHubEntry = Entry(self, font=regular_font)
        self.gitHubEntry.grid(row=2, column=1, sticky="ew", pady=100)

        next_button = Button(self, text="Next", command=lambda: (parent.show_frame(Projects), self.read_data))
        next_button.grid(row=8, column=1, columnspan=1, sticky="ew")

        add_button = Button(self, text="Add", command=lambda: (parent.show_frame(Projects), self.read_data))
        add_button.grid(row=8, column=0, columnspan=1, sticky="ew")

        # Set the frame to expand
        self.grid(sticky="nsew")



        # Add additional widgets or information here


class Education(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        # Configure the grid
        self.grid_columnconfigure(0, weight=1)  # Configure columns to expand
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)     # Configure rows to expand
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        # Define a larger font
        large_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        largest_font = tkFont.Font(family="Helvetica", size=25, weight="bold")
        regular_font = tkFont.Font(family="Helvetica", size=20)

        # Widgets
        label = Label(self, text="Education", font=largest_font)
        label.grid(row=0, columnspan=2, sticky="w")

        schoolLabel = Label(self, text="School:", font=large_font)
        schoolLabel.grid(row=1, column=0, sticky="w")

        self.schoolEntry = Entry(self, font=regular_font)
        self.schoolEntry.grid(row=1, column=1, sticky="ew")

        programLabel = Label(self, text="Program:", font=large_font)
        programLabel.grid(row=2, column=0, sticky="w")

        self.programEntry = Entry(self, font=regular_font)
        self.programEntry.grid(row=2, column=1, sticky="ew", pady=100)

        yearLabel = Label(self, text="Year of graduation:", font=large_font)
        yearLabel.grid(row=3, column=0, sticky="w")

        self.yearEntry = Entry(self, font=regular_font)
        self.yearEntry.grid(row=3, column=1, sticky="ew")

        next_button = Button(self, text="Next", command=lambda: (parent.show_frame(Profiles), self.read_data))
        next_button.grid(row=8, column=1, columnspan=1, sticky="ew")

        # Set the frame to expand
        self.grid(sticky="nsew")
    
    def read_data(self):
        set_education_info("jack133003_education1", "school", self.schoolEntry.get())
        set_education_info("jack133003_education1", "end date", self.yearEntry.get())
        set_education_info("jack133003_education1", "major", self.programEntry.get())
    


        # Add additional widgets or information here

class Jobs(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        # Configure the grid
        self.grid_columnconfigure(0, weight=1)  # Configure columns to expand
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)     # Configure rows to expand
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)

        # Define a larger font
        large_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        largest_font = tkFont.Font(family="Helvetica", size=25, weight="bold")
        regular_font = tkFont.Font(family="Helvetica", size=20)

        # Widgets
        label = Label(self, text="Profiles", font=largest_font)
        label.grid(row=0, columnspan=2, sticky="w")

        linkedinLabel = Label(self, text="LinkedIn:", font=large_font)
        linkedinLabel.grid(row=1, column=0, sticky="w")

        self.linkedInEntry = Entry(self, font=regular_font)
        self.linkedInEntry.grid(row=1, column=1, sticky="ew")

        gitHubLabel = Label(self, text="GitHub:", font=large_font)
        gitHubLabel.grid(row=2, column=0, sticky="w")

        self.gitHubEntry = Entry(self, font=regular_font)
        self.gitHubEntry.grid(row=2, column=1, sticky="ew", pady=100)

        next_button = Button(self, text="Next", command=lambda: (parent.show_frame(Projects), self.read_data))
        next_button.grid(row=8, column=1, columnspan=1, sticky="ew")

        # Set the frame to expand
        self.grid(sticky="nsew")

    
    def read_data(self):
        set_education_info("jack133003", "linkedin", self.linkedInEntry.get())
        set_education_info("jack133003", "github", self.gitHubEntry.get())
    
        

class Projects(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        # label = Label(self, text="Work Experiences:")
        # label.pack(pady=10, padx=10)

        # # Configure the grid
        # self.grid_columnconfigure(0, weight=1)  # Configure columns to expand
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_rowconfigure(1, weight=1)     # Configure rows to expand
        # self.grid_rowconfigure(2, weight=1)
        # self.grid_rowconfigure(3, weight=1)
        # self.grid_rowconfigure(4, weight=1)

        # # Define a larger font
        # large_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        # largest_font = tkFont.Font(family="Helvetica", size=25, weight="bold")
        # regular_font = tkFont.Font(family="Helvetica", size=20)

        # # Widgets
        # label = Label(self, text="Please List Work Experiences", font=largest_font)
        # label.grid(row=0, columnspan=2, sticky="w")

        # linkedinLabel = Label(self, text="LinkedIn:", font=large_font)
        # linkedinLabel.grid(row=1, column=0, sticky="w")

        # self.linkedInEntry = Entry(self, font=regular_font)
        # self.linkedInEntry.grid(row=1, column=1, sticky="ew")

        # gitHubLabel = Label(self, text="GitHub:", font=large_font)
        # gitHubLabel.grid(row=2, column=0, sticky="w")

        # self.gitHubEntry = Entry(self, font=regular_font)
        # self.gitHubEntry.grid(row=2, column=1, sticky="ew", pady=100)

        # next_button = Button(self, text="Next", command=lambda: (parent.show_frame(Projects), self.read_data))
        # next_button.grid(row=8, column=1, columnspan=1, sticky="ew")

        # add_button = Button(self, text="Add", command=lambda: (parent.show_frame(Projects), self.read_data))
        # add_button.grid(row=8, column=0, columnspan=1, sticky="ew")

        # # Set the frame to expand
        # self.grid(sticky="nsew")