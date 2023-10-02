from models.pricing import Pricing
from persistence.repositories.pricing_repository import PricingRepository


class PricingService:
    def __init__(self, repository: PricingRepository) -> None:
        self.__repository = repository

    def get_all(self) -> list[Pricing]:
        return self.__repository.get_all()

    def create_pricing(self, pricing: Pricing) -> None:
        self.__repository.create_pricing(pricing)
