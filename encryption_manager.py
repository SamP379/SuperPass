import os
from cryptography.fernet import Fernet


class EncryptionManager:
    """A class to handle encrypting and decrypting data using the Fernet class."""
     

    def __init__(self, key_file_path):
        self.key_file_path = key_file_path
        self.key = self.load_key()
        self.cipher = Fernet(self.key)


    def load_key(self) -> bytes:
        """Generates or loads the secret key and returns it."""
        if os.path.exists(self.key_file_path):
            with open(self.key_file_path, mode = "rb") as file:
                return file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file_path, mode = "wb") as file:
                file.write(key)
            return key
    

    def encrypt(self, text : str) -> str:
        """Encrypts some text using the Fernet cipher and then returns it."""
        return self.cipher.encrypt(text.encode()).decode()
    

    def decrypt(self, encrypted_text : str) -> str:
        """Decrypts some text using the Fernet cipher and then returns it."""
        return self.cipher.decrypt(encrypted_text.encode()).decode()
    

    def handle_encryption(self, password_data : dict) -> dict:
        """Handles encryption of usernames, emails, and passwords for each website in the provided data."""
        for website, website_data in password_data.items():
            website_data["username"] = self.encrypt(website_data["username"])
            website_data["email"] = self.encrypt(website_data["email"])
            website_data["password"] = self.encrypt(website_data["password"])
        return password_data
    

    def handle_decryption(self, password_data : dict) -> dict:
            """Handles decryption of usernames, emails, and passwords for each website in the provided data."""
            for website, website_data in password_data.items():
                website_data["username"] = self.decrypt(website_data["username"])
                website_data["email"] = self.decrypt(website_data["email"])
                website_data["password"] = self.decrypt(website_data["password"])
            return password_data