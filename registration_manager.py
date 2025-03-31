import os
import json


class RegistrationManager:
    "A class to handle registering a user for the SuperPass program."


    def __init__(self, master_file_path : str):
        self.master_file_path = master_file_path