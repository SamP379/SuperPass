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