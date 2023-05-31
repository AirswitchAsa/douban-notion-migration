movie_schema = {
    'type' : 'object',
    'properties' : {
        'created_on' : {'type' : 'string'},
        'property_url' : {'type' : 'string'},
        'title': {'type' : 'string'},
        'cover_url': {'type' : ['string', 'null']},
        'comment': {'type' : ['string', 'null']},
        'rating': {'type' : ['number', 'null']},
        'region': {'type' : ['string', 'null']},
        'director': {'type' : ['string', 'null']},
        'writer': {'type' : ['string', 'null']},
        'actor': {'type' : ['string', 'null']},
        'language': {'type' : ['string', 'null']},
        'labels': {'type' : ['string', 'null']},
        'release': {'type' : ['string', 'null']},
        'iMDb': {'type' : ['string', 'null']},
        'note': {'type' : ['string', 'null']},
    },
    'required': ['created_on', 'property_url']
}

book_schema = {}

music_schema = {}

game_schema = {}

drama_schema = {}
