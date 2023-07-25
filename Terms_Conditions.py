import customtkinter as ctk
from Personal_Info import PersonalInfo

class TermsConditions(ctk.CTkFrame):
	def __init__(self,parent):
		super().__init__(parent)
		self.pack(side = "top", expand = "True", fill = "both")
		self.introduction()

	def introduction(self):
		title_label = ctk.CTkLabel(self, text = "Terms & Conditions", font=("Helvetica", 20, "bold"))
		terms_condition_label = ctk.CTkLabel(self, text = "By using this COVID-19 contact tracing app, you agree to the following terms and conditions:", font=("Helvetica", 15), wraplength=500, anchor="w")
		term1_label = ctk.CTkLabel(self, text = "Consent for Data Collection: You consent to the collection and processing of your personal data for the purposes of COVID-19 contact tracing. This may include collecting information such as your name, phone number, location, and encounters with other users of the app.", font=("Helvetica", 10), wraplength=500)
		term2_label = ctk.CTkLabel(self, text = "Data Privacy and Security: We are committed to protecting your privacy and securing your data. We will handle your personal information in accordance with applicable data protection laws and implement appropriate technical and organizational measures to safeguard your data against unauthorized access, loss, or misuse.", font=("Helvetica", 10), wraplength=500)
		term3_label = ctk.CTkLabel(self, text = "User Responsibilities: You agree to provide accurate information during registration and promptly update any changes to your personal details. You are responsible for keeping your login credentials secure and for any activities conducted using your account.", font=("Helvetica", 10), wraplength=500)        
		term4_label = ctk.CTkLabel(self, text = "Appropriate Use: You agree to use the app in compliance with applicable laws, regulations, and these terms and conditions. You will not misuse or tamper with the app, interfere with its functionality, or engage in any activity that could harm the app or its users.", font=("Helvetica", 10), wraplength=500)
		term5_label = ctk.CTkLabel(self, text = "Limitations and Disclaimers: The app provides contact tracing assistance, but it does not guarantee the prevention or containment of COVID-19. We do not assume liability for any inaccuracies, delays, interruptions, or damages resulting from the use of the app.", font=("Helvetica", 10), wraplength=500)


		title_label.place(x=50, y=50)
		terms_condition_label.place(x=50, y=100)
		term1_label.place(x=50, y=150)
		term2_label.place(x=50, y=200)
		term3_label.place(x=50, y=250)
		term4_label.place(x=50, y=300)
		term5_label.place(x=50, y=350)

	

