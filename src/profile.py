from tkinter import Tk, Label, Button, Frame, RAISED, SE, font as tkFont, Entry, Text
from db import *

class Profile(Tk):
    def __init__(self):
        super().__init__()

        self.data = {}

        self.username = 'zayeedthegoat'

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

        create_user(self.username)

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
        self.phoneEntry.grid(row=2, column=1, sticky="ew")

        emailLabel = Label(self, text="Email:", font=large_font)
        emailLabel.grid(row=3, column=0, sticky="w")

        self.emailEntry = Entry(self, font=regular_font)
        self.emailEntry.grid(row=3, column=1, sticky="ew")

        next_button = Button(self, text="Next", command=lambda: (parent.show_frame(Education), self.read_data))
        next_button.grid(row=8, column=1, columnspan=1, sticky="ew")

        # Set the frame to expand
        self.grid(sticky="nsew")
    
    def read_data(self):
        set_info(Profile.username, "name", self.nameEntry.get())
        set_info(Profile.username, "phone", self.phoneEntry.get())
        set_info(Profile.username, "email", self.emailEntry.get())


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

        next_button = Button(self, text="Next", command=lambda: (parent.show_frame(Jobs), self.read_data))
        next_button.grid(row=8, column=1, columnspan=1, sticky="ew")

        # Set the frame to expand
        self.grid(sticky="nsew")

    
    def read_data(self):
        set_education_info(Profile.username, "linkedin", self.linkedInEntry.get())
        set_education_info(Profile.username, "github", self.gitHubEntry.get())
    


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
        self.programEntry.grid(row=2, column=1, sticky="ew")

        yearLabel = Label(self, text="Year of graduation:", font=large_font)
        yearLabel.grid(row=3, column=0, sticky="w")

        self.yearEntry = Entry(self, font=regular_font)
        self.yearEntry.grid(row=3, column=1, sticky="ew")

        next_button = Button(self, text="Next", command=lambda: (parent.show_frame(Profiles), self.read_data))
        next_button.grid(row=8, column=1, columnspan=1, sticky="ew")

        # Set the frame to expand
        self.grid(sticky="nsew")
    
    def read_data(self):
        set_education_info(f"{Profile.username}_education1", "school", self.schoolEntry.get())
        set_education_info(f"{Profile.username}_education1", "end date", self.yearEntry.get())
        set_education_info(f"{Profile.username}_education1", "major", self.programEntry.get())
    


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

        self.entries = []
        self.rowNum = 2

        # Define a larger font
        large_font = tkFont.Font(family="Helvetica", size=20, weight="bold")
        largest_font = tkFont.Font(family="Helvetica", size=25, weight="bold")
        regular_font = tkFont.Font(family="Helvetica", size=20)

        self.large_font = large_font
        self.largest_font = largest_font
        self.regular_font = regular_font

        # Widgets
        label = Label(self, text="Work Experiences", font=largest_font)
        label.grid(row=0, columnspan=2, sticky="w")

        # First set of widgets
        titleLabel1 = Label(self, text="Title:", font=large_font)
        titleLabel1.grid(row=1, column=0, sticky="w")

        self.titleEntry1 = Text(self, font=regular_font, height=10, width=50)
        self.titleEntry1.grid(row=1, column=1, sticky="ew")

        descriptionLabel1 = Label(self, text="What did you do?", font=large_font)
        descriptionLabel1.grid(row=2, column=0, sticky="w")

        self.descriptionEntry1 = Text(self, font=regular_font, height=10, width=50)
        self.descriptionEntry1.grid(row=2, column=1, sticky="ew")

        # Second set of widgets
        titleLabel2 = Label(self, text="Title:", font=large_font)
        titleLabel2.grid(row=3, column=0, sticky="w")

        self.titleEntry2 = Entry(self, font=regular_font)
        self.titleEntry2.grid(row=3, column=1, sticky="ew")

        descriptionLabel2 = Label(self, text="What did you do?", font=large_font)
        descriptionLabel2.grid(row=4, column=0, sticky="w")

        self.descriptionEntry2 = Entry(self, font=regular_font)
        self.descriptionEntry2.grid(row=4, column=1, sticky="ew")

        # Third set of widgets
        titleLabel3 = Label(self, text="Title:", font=large_font)
        titleLabel3.grid(row=5, column=0, sticky="w")

        self.titleEntry3 = Entry(self, font=regular_font)
        self.titleEntry3.grid(row=5, column=1, sticky="ew")

        descriptionLabel3 = Label(self, text="What did you do?", font=large_font)
        descriptionLabel3.grid(row=6, column=0, sticky="w")

        self.descriptionEntry3 = Entry(self, font=regular_font)
        self.descriptionEntry3.grid(row=6, column=1, sticky="ew")
        

        next_button = Button(self, text="Next", command=lambda: (parent.show_frame(Projects), self.read_data))
        next_button.grid(row=8, column=1, columnspan=1, sticky="ew")

        add_button = Button(self, text="Add", command=lambda: self.add_entry)
        add_button.grid(row=8, column=0, columnspan=1, sticky="ew")

        # Set the frame to expand
        self.grid(sticky="nsew")

    
    def read_data(self):
        # set_education_info(Profile.username, "linkedin", self.linkedInEntry.get())
        # set_education_info(Profile.username, "github", self.gitHubEntry.get())
        return
    
    def add_entry(self):        
        titleLabel = Label(self, text="Job Title:", font=self.large_font)
        titleLabel.grid(row=self.rowNum+1, column=0, sticky="w")

        titleEntry = Entry(self, font=self.regular_font)
        titleEntry.grid(row=self.rowNum+1, column=1, sticky="ew")

        descriptionLabel = Label(self, text="What did you do?", font=self.large_font)
        descriptionLabel.grid(row=self.rowNum+2, column=0, sticky="w")

        descriptionEntry = Entry(self, font=self.regular_font)
        descriptionEntry.grid(row=self.rowNum+2, column=1, sticky="ew", pady=100)

        # Add the new entry to the list of entries (for further processing if needed)
        self.entries.append([titleEntry, descriptionEntry])

        self.rowNum += 2

    
        

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