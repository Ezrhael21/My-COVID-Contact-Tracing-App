import customtkinter as ctk
from Welcome import Welcome

# Create a class for the App
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ES COVID Contact Tracing App")
        self.geometry("600x600")

        self.welcome = Welcome(self)
    