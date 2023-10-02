from dependency_injector import containers, providers
from business.movie_service import MovieService
from business.subscription_service import SubscriptionService
from business.twilio_gateway_fake import TwilioGatewayFake
from business.user_service import UserService
from infrastructure.settings import Settings
from persistence.database import Database
from persistence.mappings.movie_mapping import MovieMapping
from persistence.mappings.pricing_mapping import PricingMapping
from persistence.mappings.subscription_mapping import SubscriptionMapping
from persistence.mappings.user_mapping import UserMapping
from persistence.repositories.movie_repository import MovieRepository
from persistence.repositories.pricing_repository import PricingRepository
from business.pricing_service import PricingService
from persistence.repositories.subscription_repository import SubscriptionRepository
from persistence.repositories.user_repository import UserRepository


class Container(containers.DeclarativeContainer):
    config: Settings = providers.Configuration()

    database = providers.Singleton(
        Database,
        db_url=config.db_connection,
        mappings=providers.List(
            providers.Factory(MovieMapping),
            providers.Factory(PricingMapping),
            providers.Factory(SubscriptionMapping),
            providers.Factory(UserMapping),
        ),
    )

    user_repository = providers.Factory(
        UserRepository,
        session_factory=database.provided.session,
    )

    movie_repository = providers.Factory(
        MovieRepository,
        session_factory=database.provided.session,
    )

    pricing_repository = providers.Factory(
        PricingRepository,
        session_factory=database.provided.session,
    )

    subscription_repository = providers.Factory(
        SubscriptionRepository,
        session_factory=database.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        repository=user_repository,
    )

    movie_service = providers.Factory(
        MovieService,
        repository=movie_repository,
    )

    pricing_service = providers.Factory(
        PricingService,
        repository=pricing_repository,
    )

    sms_service = providers.Factory(
        TwilioGatewayFake,
    )

    subscription_service = providers.Factory(
        SubscriptionService,
        repository=subscription_repository,
        sms_service=sms_service,
    )
