import customtkinter as ctk
class Welcome(ctk.CTkFrame):
	def __init__(self,parent):
		super().__init__(parent)
		self.pack(side = "top", expand = "True", fill = "both")
		self.introduction()

	def introduction(self):
		title_label = ctk.CTkLabel(self, text = "Welcome to ES Covid Tracing App", font=("Helvetica", 30, "bold"))
		title2_label = ctk.CTkLabel(self, text = "Your Reliable Contact Tracing Companion", font=("Helvetica", 20))
		title3_label = ctk.CTkLabel(self, text ="Programmed by: Ezrhael R. Sicat", font=("Helvetica", 15))
		
		title_label.place(x=50, y=100)
		title2_label.place(x=50, y=150)
		title3_label.place(x=50, y=300)
		
		