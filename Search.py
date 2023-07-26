import customtkinter as ctk
class Search(ctk.CTkFrame):
	def __init__(self,parent):
		super().__init__(parent)
		self.pack(side = "top", expand = "True", fill = "both")

		self.create_widgets()
		self.create_buttons()
		
	def create_widgets(self):
		pass

	# Method to create buttons
	def create_buttons(self):
		self.columnconfigure((0,1,), weight = 1)
		self.rowconfigure((0,1,2,3,4,5), weight = 1)
		back_button = ctk.CTkButton(self, text = "BACK", command = self.show_personal_info)
		exit_button = ctk.CTkButton(self, text = "EXIT")
		back_button.grid(row=5, column=0, padx=10, pady=10)
		exit_button.grid(row=5, column=1, padx=10, pady=10)
	
	# Method to redirect from current frame to Personal Info Frame
	def show_personal_info(self):
		self.pack_forget()
		from Personal_Info import PersonalInfo
	
		# Call the Personal Info Frame
		personal_info_frame = PersonalInfo(self.master)
		personal_info_frame.pack(side="top", expand=True, fill="both")
