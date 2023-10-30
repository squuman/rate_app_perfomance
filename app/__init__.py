"""Модуль для инициации сервера"""
from fastapi import FastAPI
from app.configuration.server import Server


def create_app() -> FastAPI:
    """Функция инициации сервера"""
    return Server(FastAPI()).get_app()
