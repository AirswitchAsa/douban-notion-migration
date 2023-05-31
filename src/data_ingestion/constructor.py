from builder import DataBuilder

def build_movie_data_for_notion(builder: DataBuilder):
    '''
    construct the movie data for notion database
    '''
    movie_entries = builder.build_movie_entries()
    notion_movie_entries = []
    return notion_movie_entries
