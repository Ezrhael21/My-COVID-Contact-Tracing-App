import customtkinter as ctk
from Personal_Info import PersonalInfo

class Welcome(ctk.CTkFrame):
	def __init__(self,parent):
		super().__init__(parent)
		self.pack(side = "top", expand = "True", fill = "both")
		self.introduction()
		self.create_widgets()

	def introduction(self):
		title_label = ctk.CTkLabel(self, text = "Welcome to ES Covid Tracing App", font=("Helvetica", 30, "bold"))
		title2_label = ctk.CTkLabel(self, text = "Your Reliable Contact Tracing Companion", font=("Helvetica", 20))
		title3_label = ctk.CTkLabel(self, text ="Programmed by: Ezrhael R. Sicat", font=("Helvetica", 15))
		
		title_label.place(x=50, y=100)
		title2_label.place(x=50, y=150)
		title3_label.place(x=50, y=300)
		
	def create_widgets(self):
		self.columnconfigure((0,1), weight = 1)
		self.rowconfigure((0,1,2,3,4,5), weight = 1)
		get_started_button = ctk.CTkButton(self, text = "Get Started", command = self.show_personal_info)
		get_started_button.grid(row=4, column=1, padx=20, pady=20)
			
	def show_personal_info(self):
		self.pack_forget()
	
		personal_info_frame = PersonalInfo(self.master)
		personal_info_frame.pack(side="top", expand=True, fill="both")	