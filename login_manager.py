import os 
import json
from hash_manager import HashManager


class LoginManager():
    """A class to handle logging a user in for the SuperPass program."""
    
    
    def __init__(self, master_file_path : str):
        self.master_file_path = master_file_path
        self.hasher = HashManager()
    

    def check_registration(self) -> bool:
        """Checks if a user has already registered and returns True or False."""
        return os.path.exists(self.master_file_path)
    

    def check_login_password(self, login_password : str) -> bool:
        """Handles verifying a login password against the stored master password."""
        try:
            with open(self.master_file_path, mode = "r") as file:
                master_password = json.load(file).get("master_password")
                return self.hasher.verify_password(login_password, master_password)
        except Exception:
            return False