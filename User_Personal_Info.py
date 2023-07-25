import json

class UserData:
    def __init__(self, name, age, birthday, gender, contacts, email, address):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.gender = gender
        self.contacts = contacts
        self.email = email
        self.address = address

    def to_json(self):
        # Convert the UserData object to a dictionary
        user_data_dict = {
            "name": self.name,
            "age": self.age,
            "birthday": self.birthday,
            "gender": self.gender,
            "contacts": self.contacts,
            "email": self.email,
            "address": self.address
        }
        return json.dumps(user_data_dict, indent=4)

    def save_to_json_file(self, file_path):
        # Save the UserData object as a JSON file
        with open(file_path, 'w') as file:
            json.dump(self.to_json(), file)