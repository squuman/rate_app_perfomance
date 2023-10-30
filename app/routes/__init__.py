"""Модуль для инициации роутов"""
from app.routes.routes import Routes
from app.internal.routes import user

__routes__ = Routes(routes=(user.router,))
