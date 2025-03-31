from hash_manager import HashManager
from login_manager import LoginManager
from password_storage import PasswordStorage
from registration_manager import RegistrationManager


class PasswordManager:
    """Coordinates backend logic for the SuperPass program, handling registration, 
       logging in, retrieving password data and saving new password data."""
    

    MASTER_FILE_PATH = "user_data.json"
    PASSWORDS_FILE_PATH = "passwords.json"


    def __init__(self):
        self.hasher = HashManager()
        self.login = LoginManager(PasswordManager.MASTER_FILE_PATH)
        self.storage = PasswordStorage(PasswordManager.PASSWORDS_FILE_PATH)
        self.registration = RegistrationManager(PasswordManager.MASTER_FILE_PATH)