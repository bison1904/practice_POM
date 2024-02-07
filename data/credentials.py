import os
from dotenv import load_dotenv

load_dotenv()

class Credentials:
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")

    LOGIN1 = os.getenv("LOGIN1")
    PASSWORD1 = os.getenv("PASSWORD1")
