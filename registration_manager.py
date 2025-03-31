import os
import json


class RegistrationManager:
    "A class to handle registering a user for the SuperPass program."


    def __init__(self, master_file_path : str):
        self.master_file_path = master_file_path


    def check_registration(self) -> bool:
        """Checks if a user has already registered and returns True or False."""
        return os.path.exists(self.master_file_path)