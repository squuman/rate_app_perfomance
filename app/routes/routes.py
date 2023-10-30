"""Модуль для управления роутами"""
from dataclasses import dataclass
from fastapi import FastAPI


@dataclass(frozen=True)
class Routes:
    """Класс для регистрации и хранения роутов"""
    routes: tuple

    def register_routes(self, app: FastAPI):
        """Метод для регистрации путей"""
        for route in self.routes:
            app.include_router(route)
