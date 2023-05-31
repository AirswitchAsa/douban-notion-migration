from abc import ABC, abstractmethod
from schema import movie_schema, book_schema, music_schema, game_schema, drama_schema

class DataBuilder(ABC):

    movie_schema = movie_schema
    book_schema = book_schema
    music_schema = music_schema
    game_schema = game_schema
    drama_schema = drama_schema

    @abstractmethod
    def build_movie_entries(self):
        pass

    @abstractmethod
    def build_book_entries(self):
        pass

    @abstractmethod
    def build_music_entries(self):
        pass

    @abstractmethod
    def build_game_entries(self):
        pass

    @abstractmethod
    def build_drama_entries(self):
        pass
