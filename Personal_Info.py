import customtkinter as ctk
class PersonalInfo(ctk.CTkFrame):
	def __init__(self,parent):
		super().__init__(parent)
		self.pack(side = "top", expand = "True", fill = "both")

		self.create_widgets()
		
	def create_widgets(self):
		info_label = ctk.CTkLabel(self, text = "Personal Information:")
		name_label = ctk.CTkLabel(self, text = "Name:")
		age_label = ctk.CTkLabel(self, text = "Age:")
		birthday_label = ctk.CTkLabel(self, text = "Date of Birth:")
		gender_label = ctk.CTkLabel(self, text = "Gender:")
		contacts_label = ctk.CTkLabel(self, text = "Contact Number:")
		email_label = ctk.CTkLabel(self, text = "Email Address:")
		address_label = ctk.CTkLabel(self, text = "Current Home Address:")
		
		self.columnconfigure((0,1), weight = 1)
		self.rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight = 1)

		info_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
		name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
		age_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
		birthday_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
		gender_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
		contacts_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
		email_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
		address_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")
		
		name_entry = ctk.CTkEntry(self)
		age_entry = ctk.CTkEntry(self)
		birthday_entry = ctk.CTkEntry(self)
		gender_entry = ctk.CTkEntry(self)
		contacts_entry = ctk.CTkEntry(self)
		email_entry = ctk.CTkEntry(self)
		address_entry = ctk.CTkEntry(self)

		name_entry.grid(row=1, column=1, padx=10, pady=10)
		age_entry.grid(row=2, column=1, padx=10, pady=10)
		birthday_entry.grid(row=3, column=1, padx=10, pady=10)
		gender_entry.grid(row=4, column=1, padx=10, pady=10)
		contacts_entry.grid(row=5, column=1, padx=10, pady=10)
		email_entry.grid(row=6, column=1, padx=10, pady=10)
		address_entry.grid(row=7, column=1, padx=10, pady=10)