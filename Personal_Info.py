import customtkinter as ctk
from tkinter import messagebox
from tkinter import END
from Search import Search
import json
import random

# Create a class for Personal Info Frame
class PersonalInfo(ctk.CTkFrame):
	def __init__(self,parent):
		super().__init__(parent)
		self.pack(side = "top", expand = "True", fill = "both")
		self.create_widgets()
		self.create_buttons()

	# Method to create widgets for Personal Info 
	def create_widgets(self):
		# Label
		info_label = ctk.CTkLabel(self, text = "Personal Information", font=("Helvetica", 20, "bold"))
		name_label = ctk.CTkLabel(self, text = "Name:")
		age_label = ctk.CTkLabel(self, text = "Age:")
		birthday_label = ctk.CTkLabel(self, text = "Date of Birth:")
		gender_label = ctk.CTkLabel(self, text = "Gender:")
		contacts_label = ctk.CTkLabel(self, text = "Contact Number:")
		email_label = ctk.CTkLabel(self, text = "Email Address:")
		address_label = ctk.CTkLabel(self, text = "Current Home Address:")
		covid_positive_label = ctk.CTkLabel(self, text = "Have you tested positive for covid 19? (Yes/No)")

		# Layout for Label
		info_label.place(x=50, y=50)
		name_label.place(x=50, y=100)
		age_label.place(x=50, y=150)
		birthday_label.place(x=50, y=200)
		gender_label.place(x=50, y=250)
		contacts_label.place(x=50, y=300)
		email_label.place(x=50, y=350)
		address_label.place(x=50, y=400)
		covid_positive_label.place(x=50, y=450)

		# Entry Widgets
		self.name_entry = ctk.CTkEntry(self)
		self.age_entry = ctk.CTkEntry(self)
		self.birthday_entry = ctk.CTkEntry(self)
		self.gender_entry = ctk.CTkEntry(self)
		self.contacts_entry = ctk.CTkEntry(self)
		self.email_entry = ctk.CTkEntry(self)
		self.address_entry = ctk.CTkEntry(self)
		self.covid_positive_entry = ctk.CTkEntry(self)

		# Layout for Entry Widgets
		self.name_entry.place(x=400, y=100)
		self.age_entry.place(x=400, y=150)
		self.birthday_entry.place(x=400, y=200)
		self.gender_entry.place(x=400, y=250)
		self.contacts_entry.place(x=400, y=300)
		self.email_entry.place(x=400, y=350)
		self.address_entry.place(x=400, y=400)
		self.covid_positive_entry.place(x=400, y=450)

	# Method to create the Back/Submit Buttons
	def create_buttons(self):
		self.columnconfigure((0,1,2), weight = 1)
		self.rowconfigure((0,1,2,3,4,5), weight = 1)
		back_button = ctk.CTkButton(self, text = "BACK", command = self.show_terms_conditions)
		save_button = ctk.CTkButton(self, text = "SAVE", command = self.save_to_json)
		next_button = ctk.CTkButton(self, text = "NEXT", command = self.show_search_frame)
		back_button.grid(row=5, column=0, padx=10, pady=10)
		save_button.grid(row=5, column=1, padx=10, pady=10)
		next_button.grid(row=5, column=2, padx=10, pady=10)


	# Method to redirect the current frame to Terms & Conditions
	def show_search_frame(self):
		# Hide the current Welcome frame
		self.pack_forget()
	
		# Call the Terms & Condtions Frame
		search_frame = Search(self.master)
		search_frame.pack(side="top", expand=True, fill="both")	

	# Method to redirect to Terms & Conditions
	def show_terms_conditions(self):
        # Hide the current PersonalInfo frame
		self.pack_forget()
		from Terms_Conditions import TermsConditions

		# Call the Terms & Conditions Frame
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
		# Get Entry Values for Personal Information
		name = self.name_entry.get()
		age = self.age_entry.get()
		birthday = self.birthday_entry.get()
		gender = self.gender_entry.get()
		contacts = self.contacts_entry.get()
		email = self.email_entry.get()
		address = self.address_entry.get()
		covid_positive = self.covid_positive_entry.get()

		# Add message box that will require user to provide all information
		if not name or not age or not birthday or not gender or not contacts or not email or not address:
			messagebox.showinfo("Message", "Please provide all information.")
			return
		
		# Validate the inputs for COVID Postive Question
		valid_inputs = {"Yes", "No"}
		if covid_positive not in valid_inputs:
			messagebox.showinfo("Error", "Please enter 'Yes' or 'No' for COVID and Travel questions.")
			return

        # Generate a reference number for the user
		reference_number = self.generate_reference_number(name, age)
			
		# Create the user data object
		data = {
			"name": name,
			"age": age,
			"birthday": birthday,
			"gender": gender,
			"contacts": contacts,
			"email": email,
			"address": address,
			"reference_number": reference_number,
			"covid_positive": covid_positive
			}

		# Try to open the existing JSON file or create a new one if not found
		try:		 		
			with open("user_data.json", "r") as file:
				user_data = json.load(file)
		except FileNotFoundError:
			user_data = []

		# Append the new data to the existing user_data list
		user_data.append(data)

		# Save the updated user_data list to the JSON file
		with open("user_data.json", "w") as file:
			json.dump(user_data, file, indent=4)
		
		# Show a success message with the reference number
		messagebox.showinfo("Success", f"Data saved to JSON file.\nYour reference number: {reference_number}")

        # Clear the input fields
		self.name_entry.delete(0, END)
		self.age_entry.delete(0, END)
		self.birthday_entry.delete(0, END)
		self.gender_entry.delete(0, END)
		self.contacts_entry.delete(0, END)
		self.email_entry.delete(0, END)
		self.address_entry.delete(0, END)
		self.covid_positive_entry.delete(0, END)


