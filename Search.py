import customtkinter as ctk
from tkinter import messagebox
import json

class Search(ctk.CTkFrame):
	def __init__(self,parent):
		super().__init__(parent)
		self.pack(side = "top", expand = "True", fill = "both")

		self.create_widgets()
		self.create_buttons()
		
	def create_widgets(self):
		# Label
		search_label = ctk.CTkLabel(self, text = "Search: (Enter Reference Number)")

		# Layout
		search_label.place(x=50, y=50)

		# Entry Widgets
		self.search_entry = ctk.CTkEntry(self)

		# Layout for Entry Widgets
		self.search_entry.place(x=400, y=50)

        # Output display for user input values
		self.output_name = ctk.CTkLabel(self, text="Name:")
		self.output_name.place(x=50, y=100)
		
		self.output_age = ctk.CTkLabel(self, text="Age:")
		self.output_age.place(x=50, y=150)
		
		self.output_birthday = ctk.CTkLabel(self, text="Date of Birth:")
		self.output_birthday.place(x=50, y=200)
		
		self.output_gender = ctk.CTkLabel(self, text="Gender:")
		self.output_gender.place(x=50, y=250)

		self.output_contacts = ctk.CTkLabel(self, text="Contact Number:")
		self.output_contacts.place(x=50, y=300)

		self.output_email = ctk.CTkLabel(self, text="Email Address:")
		self.output_email.place(x=50, y=350)

		self.output_address = ctk.CTkLabel(self, text="Current Home Address:")
		self.output_address.place(x=50, y=400)	

	# Method to create buttons
	def create_buttons(self):
		self.columnconfigure((0,1,2), weight = 1)
		self.rowconfigure((0,1,2,3,4,5), weight = 1)
		back_button = ctk.CTkButton(self, text = "BACK", command = self.show_personal_info)
		search_button = ctk.CTkButton(self, text = "SEARCH", command = self.search_data)
		exit_button = ctk.CTkButton(self, text = "EXIT")
		back_button.grid(row=5, column=0, padx=10, pady=10)
		search_button.grid(row=5, column=1, padx=10, pady=10)
		exit_button.grid(row=5, column=2, padx=10, pady=10)
	
	# Method to redirect from current frame to Personal Info Frame
	def show_personal_info(self):
		self.pack_forget()
		from Personal_Info import PersonalInfo
	
		# Call the Personal Info Frame
		personal_info_frame = PersonalInfo(self.master)
		personal_info_frame.pack(side="top", expand=True, fill="both")
                
	def search_data(self):
		reference_number = self.search_entry.get()
				
		with open("user_data.json", "r") as file:
			user_data = json.load(file)

		found_data = None
        
		for data in user_data:
			if "reference_number" in data and data["reference_number"] == reference_number:
				found_data = data
				break
			
		if found_data:
			self.output_name.configure(text=f"Name: {found_data['name']}")
			self.output_age.configure(text=f"Age: {found_data['age']}")
			self.output_birthday.configure(text=f"Date of Birth: {found_data['birthday']}")
			self.output_gender.configure(text=f"Gender: {found_data['gender']}")
			self.output_contacts.configure(text=f"Contact Number: {found_data['contacts']}")
			self.output_email.configure(text=f"Email Address: {found_data['email']}")
			self.output_address.configure(text=f"Current Home Address: {found_data['address']}")
		else:
			messagebox.showinfo("Error", "Reference number not found.")
			self.output_name.configure(text="Name:")
			self.output_age.configure(text="Age:")
			self.output_birthday.configure(text="Date of Birth:")
			self.output_gender.configure(text="Gender:")
			self.output_contacts.configure(text="Contact Number:")
			self.output_email.configure(text="Email Address:")
			self.output_address.configure(text="Current Home Address")
