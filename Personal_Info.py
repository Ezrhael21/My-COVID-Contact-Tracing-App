import customtkinter as ctk

class PersonalInfo(ctk.CTkFrame):
	def __init__(self,parent):
		super().__init__(parent)
		self.pack(side = "top", expand = "True", fill = "both")
		self.create_widgets()
		self.create_buttons()

	def create_widgets(self):
		info_label = ctk.CTkLabel(self, text = "Personal Information", font=("Helvetica", 20, "bold"))
		name_label = ctk.CTkLabel(self, text = "Name:")
		age_label = ctk.CTkLabel(self, text = "Age:")
		birthday_label = ctk.CTkLabel(self, text = "Date of Birth:")
		gender_label = ctk.CTkLabel(self, text = "Gender:")
		contacts_label = ctk.CTkLabel(self, text = "Contact Number:")
		email_label = ctk.CTkLabel(self, text = "Email Address:")
		address_label = ctk.CTkLabel(self, text = "Current Home Address:")

		info_label.place(x=50, y=50)
		name_label.place(x=50, y=100)
		age_label.place(x=50, y=150)
		birthday_label.place(x=50, y=200)
		gender_label.place(x=50, y=250)
		contacts_label.place(x=50, y=300)
		email_label.place(x=50, y=350)
		address_label.place(x=50, y=400)
		
		name_entry = ctk.CTkEntry(self)
		age_entry = ctk.CTkEntry(self)
		birthday_entry = ctk.CTkEntry(self)
		gender_entry = ctk.CTkEntry(self)
		contacts_entry = ctk.CTkEntry(self)
		email_entry = ctk.CTkEntry(self)
		address_entry = ctk.CTkEntry(self)

		name_entry.place(x=400, y=100)
		age_entry.place(x=400, y=150)
		birthday_entry.place(x=400, y=200)
		gender_entry.place(x=400, y=250)
		contacts_entry.place(x=400, y=300)
		email_entry.place(x=400, y=350)
		address_entry.place(x=400, y=400)

	def create_buttons(self):
		self.columnconfigure((0,1), weight = 1)
		self.rowconfigure((0,1,2,3,4,5), weight = 1)
		back_button = ctk.CTkButton(self, text = "BACK", command = self.show_terms_conditions)
		next_button = ctk.CTkButton(self, text = "NEXT")
		back_button.grid(row=5, column=0, padx=10, pady=10)
		next_button.grid(row=5, column=1, padx=10, pady=10)

	def show_terms_conditions(self):
        # Hide the current PersonalInfo frame
		self.pack_forget()
		from Terms_Conditions import TermsConditions
		welcome_frame = TermsConditions(self.master)
		welcome_frame.pack(side="top", expand=True, fill="both")