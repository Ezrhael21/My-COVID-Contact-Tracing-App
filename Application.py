import customtkinter as ctk
from Personal_Info import PersonalInfo

# Create a class for user interface
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ES COVID Contact Tracing App")
        self.geometry("400x700")

        self.personal_info = PersonalInfo(self)
    