from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide
from business.user_service import UserService
from dtos.create_movie_dto import CreateMovieDto

from infrastructure.container import Container
from models.movie import Movie
from business.movie_service import MovieService

router = APIRouter(
    prefix='/movies',
)


@router.get('/')
@inject
def get_movies(movie_service: MovieService = Depends(Provide[Container.movie_service])):
    return movie_service.get_all()


@router.post('/', status_code=status.HTTP_201_CREATED)
@inject
def create_movie(request: CreateMovieDto, movie_service: MovieService = Depends(Provide[Container.movie_service])):
    movie = Movie(
        name=request.name,
        description=request.description,
        imdb_url=request.imdb_url,
    )

    movie_service.create_movie(movie)

    return movie
