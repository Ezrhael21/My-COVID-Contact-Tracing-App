import json

# Create a class for user data
class UserData:
    def __init__(self, name, age, birthday, gender, contacts, email, address, reference_number):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.gender = gender
        self.contacts = contacts
        self.email = email
        self.address = address
        self.reference_number = reference_number

    def to_json(self):
        # Convert the UserData object to a dictionary
        user_data_dict = {
            "name": self.name,
            "age": self.age,
            "birthday": self.birthday,
            "gender": self.gender,
            "contacts": self.contacts,
            "email": self.email,
            "address": self.address,
            "reference_number": self.reference_number
        }
        return json.dumps(user_data_dict, indent=4)

    def save_to_json_file(self, file_path):
        # Save the UserData object as a JSON file
        with open(file_path, 'w') as file:
            json.dump(self.to_json(), file)