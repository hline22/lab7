from dataclasses import dataclass


@dataclass
class CreateMovieDto:
    name: str
    description: str
    imdb_url: str
