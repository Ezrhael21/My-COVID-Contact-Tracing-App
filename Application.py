import tkinter as tk
from tkinter import ttk
from Personal_Information import PersonalInfo

# Create a class for user interface
class UserInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ES COVID Contact Tracing App")
        self.geometry("800x500")
        self.personal_info = PersonalInfo(self)

    