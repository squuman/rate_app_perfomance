from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DatabaseHandler:
    def __init__(self, name: str):
        self.name = name

        creds = {
            'user': 'postgres',
            'password': '1',
            'host': 'localhost',
            'database': name,
        }
        self.url = f"postgresql://{creds['user']}:{creds['password']}@{creds['host']}/{creds['database']}"
        self.engine = create_engine(url=self.url, echo=False)
        self.session = None

    def __enter__(self):
        self.open_session()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            raise Exception(f"Something wrong.\nobj: Database\n{exc_val}")
        self.close_session()

    def open_session(self):
        """Создание новой сессии подключения к БД"""
        self.session = sessionmaker(bind=self.engine)()

    def close_session(self):
        """Закрытие сессии"""
        self.session.close()
