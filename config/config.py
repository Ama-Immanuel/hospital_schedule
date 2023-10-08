import os

from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()

        # Server Env
        self.server_host = os.getenv("SERVER_HOST")
        self.server_port = os.getenv("SERVER_PORT")

        # DB Env
        self.db_host = os.getenv("DB_HOST")
        self.db_port = int(os.getenv("DB_PORT"))
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_name = os.getenv("DB_NAME")


cfg = Config()
