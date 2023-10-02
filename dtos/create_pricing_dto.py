from dataclasses import dataclass


@dataclass
class CreatePricingDto:
    name: str
    price: float
