import customtkinter as ctk
class CovidDiagnosis(ctk.CTkFrame):
	def __init__(self,parent):
		super().__init__(parent)
		self.pack(side = "top", expand = "True", fill = "both")

		self.create_widgets()
		
	def create_widgets(self):
		diagnosis_label = ctk.CTkLabel(self, text = "COVID-19 Diagnosis")
		question_label = ctk.CTkLabel(self, text = "Have you been sick of any of the following in the past 14 days?")
		fever_label = ctk.CTkLabel(self, text = "Fever - Yes/No")
		colds_label = ctk.CTkLabel(self, text = "Colds - Yes/No")
		cough_label = ctk.CTkLabel(self, text = "Cough - Yes/No")
		sore_throat_label = ctk.CTkLabel(self, text = "Sore Throat - Yes/No")
		breathing_label = ctk.CTkLabel(self, text = "Difficulty in Breating - Yes/No")
		
		self.columnconfigure((0,1), weight = 1)
		self.rowconfigure((0,1,2,3,4,5,6,7,8), weight = 1)

		diagnosis_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
		question_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
		fever_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
		colds_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
		cough_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
		sore_throat_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
		breathing_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
		
		fever_entry = ctk.CTkEntry(self)
		colds_entry = ctk.CTkEntry(self)
		cough_entry = ctk.CTkEntry(self)
		sore_throat_entry = ctk.CTkEntry(self)
		breathing_entry = ctk.CTkEntry(self)

		fever_entry.grid(row=2, column=1, padx=10, pady=10)
		colds_entry.grid(row=3, column=1, padx=10, pady=10)
		cough_entry.grid(row=4, column=1, padx=10, pady=10)
		sore_throat_entry.grid(row=5, column=1, padx=10, pady=10)
		breathing_entry.grid(row=6, column=1, padx=10, pady=10)
		