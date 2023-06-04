from data_ingestion.builder import DataBuilder

MOVIE_FIELDS = ['title', 'director', 'writer', 'actor', 'region', 'language', 'labels', 'comment', 'release', 'iMDb', 'rating', 'property_url', 'poster', 'created_on']

def build_movie_data_for_notion(builder: DataBuilder):
    '''
    construct the movie data for notion database
    '''
    movie_entries = builder.build_movie_entries()
    notion_movie_entries = []
    return notion_movie_entries
