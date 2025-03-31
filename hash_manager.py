import bcrypt

class HashManager:
    """A class to handle password hashing and verification using bycrypt."""

    def __init__(self):
        pass

    def hash_password(self, password : str) -> str:
        """Hashes a given password using bcrypt and returns the hashed version."""
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed.decode()
    
    def verify_password(self, password : str, hashed_password : str) -> bool:
        """Verifies a password against a hashed password and returns a boolean."""
        return bcrypt.checkpw(password.encode(), hashed_password.encode())