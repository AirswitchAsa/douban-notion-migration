from abc import ABC, abstractmethod

class DataBuilder(ABC):

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
