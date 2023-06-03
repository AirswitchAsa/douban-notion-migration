def get_movie_schema():
    return {'title': {'title': {},},
            'poster': {'files': {}},
            'created_on': {'date': {}},
            'comment': {'rich_text': {}},
            'rating': {'number': {}},
            'director': {'multi_select': {}},
            'writer': {'multi_select': {}},
            'actor': {'multi_select': {}},
            'release': {'rich_text': {}},
            'region': {'multi_select': {}},
            'language': {'multi_select': {}},
            'labels': {'multi_select': {}},
            'iMDb': {'rich_text': {}},
            'property_url': {'url': {}},
        }

def get_movie_entry_template():
    return {
            'title': [{'type': 'text', 'text': {'content': 'foobar', 'link': None}}],
            'poster': {'name': 'poster', 'id': 'external', 'start': 'https://uploads.kcwiki.cn/commons/3/3a/KanMusu011.jpg'},
            'comment': {'type':'rich_text', 'rich_text': [{'type': 'text', 'text': {'content': 'foobar', 'link': None}}]},
            'rating': {'type': 'number', 'number': 5},
            'director': {'type':'multi_select', 'multi_select': [{'name': 'a'}, {'name': 'b'}]},
            'writer': {'type':'multi_select', 'multi_select': [{'name': 'a'}, {'name': 'b'}]},
            'actor': {'type':'multi_select', 'multi_select': [{'name': 'a'}, {'name': 'b'}]},
            'release': {'type':'rich_text', 'rich_text': [{'type': 'text', 'text': {'content': 'foobar', 'link': None}}]},
            'region': {'type':'multi_select', 'multi_select': [{'name': 'a'}, {'name': 'b'}]},
            'language': {'type':'multi_select', 'multi_select': [{'name': 'a'}, {'name': 'b'}]},
            'labels': {'type':'multi_select', 'multi_select': [{'name': 'a'}, {'name': 'b'}]},
            'iMDb': {'type':'rich_text', 'rich_text': [{'type': 'text', 'text': {'content': 'foobar', 'link': None}}]},
            'property_url': {'type':'url', 'url': 'https://www.douban.com/subject/1292052/'},
        }


book_schema = {}

music_schema = {}

game_schema = {}

drama_schema = {}
