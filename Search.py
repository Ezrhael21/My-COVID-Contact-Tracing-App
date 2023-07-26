import customtkinter as ctk
class Search(ctk.CTkFrame):
	def __init__(self,parent):
		super().__init__(parent)
		self.pack(side = "top", expand = "True", fill = "both")

		self.create_widgets()
		
	def create_widgets(self):
		pass
		