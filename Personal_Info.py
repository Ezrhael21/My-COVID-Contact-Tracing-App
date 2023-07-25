import customtkinter as ctk
from User_Personal_Info import UserData
from tkinter import messagebox
import json
import random

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

		self.name_entry = ctk.CTkEntry(self)
		self.age_entry = ctk.CTkEntry(self)
		self.birthday_entry = ctk.CTkEntry(self)
		self.gender_entry = ctk.CTkEntry(self)
		self.contacts_entry = ctk.CTkEntry(self)
		self.email_entry = ctk.CTkEntry(self)
		self.address_entry = ctk.CTkEntry(self)

		self.name_entry.place(x=400, y=100)
		self.age_entry.place(x=400, y=150)
		self.birthday_entry.place(x=400, y=200)
		self.gender_entry.place(x=400, y=250)
		self.contacts_entry.place(x=400, y=300)
		self.email_entry.place(x=400, y=350)
		self.address_entry.place(x=400, y=400)

	def create_buttons(self):
		self.columnconfigure((0,1), weight = 1)
		self.rowconfigure((0,1,2,3,4,5), weight = 1)
		back_button = ctk.CTkButton(self, text = "BACK", command = self.show_terms_conditions)
		next_button = ctk.CTkButton(self, text = "NEXT", command = self.save_to_json)
		back_button.grid(row=5, column=0, padx=10, pady=10)
		next_button.grid(row=5, column=1, padx=10, pady=10)

	# Method to redirect to Terms & Conditions
	def show_terms_conditions(self):
        # Hide the current PersonalInfo frame
		self.pack_forget()
		from Terms_Conditions import TermsConditions
		welcome_frame = TermsConditions(self.master)
		welcome_frame.pack(side="top", expand=True, fill="both")
	
	# Method to generate a unique reference number
	def generate_reference_number(self, name, age):
        # Combine name and age to create a unique string
		name_age_str = name + str(age)

        # Generate a random number between 1000 and 9999
		random_num = random.randint(1000, 9999)

        # Combine the name/age string with the random number to get the reference number
		reference_number = name_age_str + str(random_num)
		return reference_number	
	
	# Method to save to json file
	def save_to_json(self):
		try:
		# Get Entry Values for Personal Information
			name = self.name_entry.get()
			age = self.age_entry.get()
			birthday = self.birthday_entry.get()
			gender = self.gender_entry.get()
			contacts = self.contacts_entry.get()
			email = self.email_entry.get()
			address = self.address_entry.get()

            # Generate a reference number for the user
			reference_number = self.generate_reference_number(name, age)
			
			# Create the user data object
			user_personal_info = UserData(name, age, birthday, gender, contacts, email, address, reference_number)

			# Save the UserData object to a JSON file
			with open("user_data.json", "w") as file:
				file.write(user_personal_info.to_json())

            # Show the reference number to the user
			messagebox.showinfo("Reference Number", f"Your reference number is: {reference_number}")			

		except ValueError:
			messagebox.showinfo("Message", "Please answer all the required information.")
		
        	


