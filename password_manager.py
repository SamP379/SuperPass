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
    

    def handle_registration(self, master_password : str) -> bool:
        """Attempts to register a user and returns True if successful, otherwise False."""
        if not self.registration.check_registration():
            hashed = self.hasher.hash_password(master_password)
            return self.registration.save_master_password(hashed)
        else:
            return False
    

    def handle_login(self, password : str) -> bool:
         """Attempts to log in by checking registration and verifying the password."""
         if self.login.check_registration():
              return self.login.check_login_password(password)
         else:
              return False
    

    def handle_search_website(self, website : str) -> dict | None:
        """Handles searching for a website in the password data."""
        return self.storage.get_password(website)
    

    def handle_add_website(self, new_entry : dict) -> bool:
        """Handles adding a website to the password data."""
        return self.storage.add_password(new_entry)
    

    def handle_view_websites(self):
        """Handles getting all websites saved in the password data."""
        return self.storage.get_websites()