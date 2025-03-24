import json
import copy
from encryption_manager import EncryptionManager


class PasswordStorage:
    """A class to handle loading, storing, and updating password data for the SuperPass program."""
    

    KEY_FILE_PATH = "encryption_key.key"


    def __init__(self, passwords_file_path : str):
        self.passwords_path = passwords_file_path
        self.encryptor = EncryptionManager(PasswordStorage.KEY_FILE_PATH)
        self.password_data = self.load_data()
    

    def load_data(self) -> dict:
        """Loads the data from passwords.json or returns an empty {} if the file doesn't exist."""
        try:
            with open(self.passwords_path, mode = "r") as file:
                data = json.load(file)
                decrypted_data = self.encryptor.handle_decryption(data)
                return decrypted_data
        except Exception:
            return {}
    

    def get_password(self, website : str) -> dict | None:
        """Gets the password data of the given website and returns it."""
        website = website.lower()
        if website in self.password_data:
            return self.password_data[website]
        else:
            return None
    

    def get_websites(self) -> list:
        """Gets a list of all the websites in the password data and returns it."""
        return list(self.password_data.keys())
    

    def add_password(self, new_entry : dict) -> bool:
        """Adds a new password entry to the password data and updates the JSON file."""
        self.password_data.update(new_entry)
        encrypted_data = self.encryptor.handle_encryption(copy.deepcopy(self.password_data))
        try:
            with open(self.passwords_path, mode = "w") as file:
                json.dump(encrypted_data, file, indent = 4)
                return True
        except Exception:
            return False