from re import sub
from infrastructure.settings import Settings
from fastapi import FastAPI

from infrastructure.container import Container
import presentation.user_endpoints as user_endpoints
import presentation.movie_endpoints as movie_endpoints
import presentation.pricing_endpoints as pricing_endpoints
import presentation.subscription_endpoints as subscription_endpoints


def __get_endpoint_modules():
    return [user_endpoints, movie_endpoints, pricing_endpoints, subscription_endpoints]


def create_app() -> FastAPI:
    settings = Settings("./infrastructure/.env")
    container = Container()
    container.config.from_pydantic(settings)
    endpoint_modules = __get_endpoint_modules()
    container.wire(modules=endpoint_modules)

    app = FastAPI()
    app.container = container
    for module in endpoint_modules:
        app.include_router(module.router)
    return app
