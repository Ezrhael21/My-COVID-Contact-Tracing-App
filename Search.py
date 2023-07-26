import customtkinter as ctk
from tkinter import messagebox
import json

# Create a class for Search Frame
class Search(ctk.CTkFrame):
	def __init__(self,parent):
		super().__init__(parent)
		self.pack(side = "top", expand = "True", fill = "both")

		self.create_widgets()
		self.create_buttons()
	
	# Method to create widgets for search frame
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
		
		self.output_covid_positive = ctk.CTkLabel(self, text = "Have you tested positive for covid 19?")
		self.output_covid_positive.place(x=50, y=450)

	# Method to create buttons
	def create_buttons(self):
		self.columnconfigure((0,1,2), weight = 1)
		self.rowconfigure((0,1,2,3,4,5), weight = 1)
		back_button = ctk.CTkButton(self, text = "BACK", command = self.show_personal_info)
		search_button = ctk.CTkButton(self, text = "SEARCH", command = self.search_data)
		exit_button = ctk.CTkButton(self, text = "EXIT", command = self.ask_exit)
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
    
	# Method to search data in json file
	def search_data(self):
		reference_number = self.search_entry.get()
		
		# Try to open the existing JSON file
		with open("user_data.json", "r") as file:
			user_data = json.load(file)

		found_data = None
		for data in user_data:
			# Check if the current data has the same reference number as the one searched for
			if "reference_number" in data and data["reference_number"] == reference_number:
				found_data = data
				break
			
		if found_data:
			# If data is found, update the labels with the corresponding values
			self.output_name.configure(text=f"Name: {found_data['name']}")
			self.output_age.configure(text=f"Age: {found_data['age']}")
			self.output_birthday.configure(text=f"Date of Birth: {found_data['birthday']}")
			self.output_gender.configure(text=f"Gender: {found_data['gender']}")
			self.output_contacts.configure(text=f"Contact Number: {found_data['contacts']}")
			self.output_email.configure(text=f"Email Address: {found_data['email']}")
			self.output_address.configure(text=f"Current Home Address: {found_data['address']}")
			self.output_covid_positive.configure(text=f"Have you tested positive for covid 19? {found_data['covid_positive']}")
		else:
			# If data is not found, show an error message and reset the labels
			messagebox.showinfo("Error", "Reference number not found.")
			self.output_name.configure(text="Name:")
			self.output_age.configure(text="Age:")
			self.output_birthday.configure(text="Date of Birth:")
			self.output_gender.configure(text="Gender:")
			self.output_contacts.configure(text="Contact Number:")
			self.output_email.configure(text="Email Address:")
			self.output_address.configure(text="Current Home Address:")
			self.output_address.configure(text="Have you tested positive for covid 19?")

	# Method to exit the app with a confirmation message box
	def ask_exit(self):
		result = messagebox.askquestion("Confirm Exit", "Are you sure you want to exit?")
		if result == "yes":
			self.exit_app()
	
	# Method to exit app completely
	def exit_app(self):
		self.master.destroy()