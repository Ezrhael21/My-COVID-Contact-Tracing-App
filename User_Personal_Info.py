#import json
#file_path = "user_data.json"


# Create a class for user data
#class UserData:
#    def __init__(self, name, age, birthday, gender, contacts, email, address, reference_number):
#        self.name = name
#        self.age = age
#        self.birthday = birthday
#        self.gender = gender
#        self.contacts = contacts
#        self.email = email
#        self.address = address
#        self.reference_number = reference_number
#
#    def add_data(self, file_path):
        # Convert the UserData object to a dictionary
#        user_data_dict = {
#            "name": self.name,
#            "age": self.age,
#            "birthday": self.birthday,
#            "gender": self.gender,
#            "contacts": self.contacts,
#            "email": self.email,
#            "address": self.address,
#            "reference_number": self.reference_number
#       }
#        try:
#            # Read existing data from the JSON file
#            with open(file_path, "r") as file:
#                data = json.load(file)
#        except FileNotFoundError:
            # If the file does not exist, initialize an empty list
 #           data = []

        # Append the new user data to the existing data
 #       data.append(user_data_dict)

        # Save the updated data to the JSON file
  #      with open(file_path, "w") as file:
   #         json.dump(data, file, indent=4)