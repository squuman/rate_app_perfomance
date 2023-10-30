"""Модуль управления сервером"""
from fastapi import FastAPI

from app.routes import __routes__
from database.handler import DatabaseHandler


class Server:
    """Класс для управления сервером"""
    __app: FastAPI
    __db_handler: DatabaseHandler

    def __init__(self, app: FastAPI):
        self.__app = app
        self.register_routes(app=app)
        self.create_handler()

    def get_app(self) -> FastAPI:
        print("\nСервер был запущен\n")
        return self.__app

    @staticmethod
    def register_routes(app):
        __routes__.register_routes(app)

    def create_handler(self):
        print("\nСоздано соединение к базе данных\n")
        self.__db_handler = DatabaseHandler(name='tavern')
