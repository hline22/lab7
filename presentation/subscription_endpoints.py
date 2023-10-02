from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide
from business.subscription_service import SubscriptionService
from dtos.create_subscription_dto import CreateSubscriptionDto
from dtos.create_user_dto import CreateUserDto

from infrastructure.container import Container
from models.subscription import Subscription

router = APIRouter(
    prefix='/subscriptions',
)


@router.get('/')
@inject
def get_users(subscription_service: SubscriptionService = Depends(Provide[Container.subscription_service])):
    return subscription_service.get_all()


@router.post('/', status_code=status.HTTP_201_CREATED)
@inject
def create_user(request: CreateSubscriptionDto, subscription_service: SubscriptionService = Depends(Provide[Container.subscription_service])):
    subscription = Subscription(
        start_date=request.start_date,
        end_date=request.end_date,
        user_id=request.user_id,
        pricing_id=request.pricing_id
    )

    subscription_service.create_subscription(
        subscription
    )

    return subscription
