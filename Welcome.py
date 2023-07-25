import customtkinter as ctk
from Terms_Conditions import TermsConditions

# Create a class for Welcome Frame
class Welcome(ctk.CTkFrame):
	def __init__(self,parent):
		super().__init__(parent)
		self.pack(side = "top", expand = "True", fill = "both")
		self.introduction()
		self.create_buttons()

	# Method to introduce the app to user
	def introduction(self):
		# Label
		title_label = ctk.CTkLabel(self, text = "Welcome to ES Covid Tracing App", font=("Helvetica", 30, "bold"))
		title2_label = ctk.CTkLabel(self, text = "Your Reliable Contact Tracing Companion", font=("Helvetica", 20))
		title3_label = ctk.CTkLabel(self, text ="Programmed by: Ezrhael R. Sicat", font=("Helvetica", 15))
		
		# Layout for Label
		title_label.place(x=50, y=100)
		title2_label.place(x=50, y=150)
		title3_label.place(x=50, y=300)
	
	# Method to create the get started button
	def create_buttons(self):
		self.columnconfigure((0,1), weight = 1)
		self.rowconfigure((0,1,2,3,4,5), weight = 1)
		get_started_button = ctk.CTkButton(self, text = "Get Started", command = self.show_terms_conditions)
		get_started_button.grid(row=4, column=1, padx=20, pady=20)
	
	# Method to redirect the current frame to Terms & Conditions
	def show_terms_conditions(self):
		# Hide the current Welcome frame
		self.pack_forget()
	
		# Call the Terms & Condtions Frame
		personal_info_frame = TermsConditions(self.master)
		personal_info_frame.pack(side="top", expand=True, fill="both")	