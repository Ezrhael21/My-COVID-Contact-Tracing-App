import customtkinter as ctk
from Personal_Info import PersonalInfo
from Covid_Diagnosis import CovidDiagnosis
from Welcome import Welcome

# Create a class for user interface
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("ES COVID Contact Tracing App")
        self.geometry("600x600")

        #self.personal_info = PersonalInfo(self)
        #self.covid_diagnosis = CovidDiagnosis(self)
        self.welcome = Welcome(self)
    