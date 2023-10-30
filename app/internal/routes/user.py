"""Модуль для инициации роутов компонента Users"""
from fastapi import APIRouter

router = APIRouter(
    prefix='/api/v1'
)


@router.get('/ping')
def ping():
    return {
        "response": "pong",
        "status_code": 200
    }
