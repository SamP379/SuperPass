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