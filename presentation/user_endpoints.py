from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide
from business.user_service import UserService
from dtos.create_user_dto import CreateUserDto

from infrastructure.container import Container
from models.user import User

router = APIRouter(
    prefix='/users',
)


@router.get('/')
@inject
def get_users(user_service: UserService = Depends(Provide[Container.user_service])):
    return user_service.get_all()


@router.post('/', status_code=status.HTTP_201_CREATED)
@inject
def create_user(request: CreateUserDto, user_service: UserService = Depends(Provide[Container.user_service])):
    user = User(
        name=request.name,
        email=request.email,
        phone_number=request.phone_number
    )

    user_service.create_user(
        user
    )

    return user
