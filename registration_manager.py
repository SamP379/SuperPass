import os
import json


class RegistrationManager:
    "A class to handle registering a user for the SuperPass program."


    def __init__(self, master_file_path : str):
        self.master_file_path = master_file_path


    def check_registration(self) -> bool:
        """Checks if a user has already registered and returns True or False."""
        return os.path.exists(self.master_file_path)
    

    def save_master_password(self, hashed_password : str) -> bool:
        """Saves the hashed master password to a file and returns True if successful, otherwise False."""
        user_data = {"master_password" : hashed_password}
        try:
            with open(self.master_file_path, mode = "w") as file:
                json.dump(user_data, file)
                return True
        except Exception:
            return False