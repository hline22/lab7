from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide
from business.pricing_service import PricingService
from dtos.create_pricing_dto import CreatePricingDto

from infrastructure.container import Container
from models.pricing import Pricing

router = APIRouter(
    prefix='/pricings',
)


@router.get('/')
@inject
def get_pricings(pricing_service: PricingService = Depends(Provide[Container.pricing_service])):
    return pricing_service.get_all()


@router.post('/', status_code=status.HTTP_201_CREATED)
@inject
def create_pricing(request: CreatePricingDto, pricing_service: PricingService = Depends(Provide[Container.pricing_service])):
    pricing = Pricing(
        name=request.name,
        price=request.price,
    )

    pricing_service.create_pricing(
        pricing
    )

    return pricing
