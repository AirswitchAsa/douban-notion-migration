import requests
import json
from config import notion_api, page_id

db_api_address = 'https://api.notion.com/v1/databases/'
page_api_address = 'https://api.notion.com/v1/pages/'

headers = {
    'Notion-Version': '2022-06-28',
    'content-type': 'application/json',
    'authorization': notion_api
}

def create_db(page_id, title, property_schema):
    '''
    create an empty notion database under an existing page
    '''
    data = {
        'parent': {'type': 'page_id', 'page_id': page_id},
        'title': [{'type': 'text', 'text': {'content': title, 'link': None}}],
        'properties': property_schema
    }
    response = requests.post(db_api_address, headers=headers, json=data)
    return response

from data_ingestion.notion_schema import get_movie_schema
response = create_db(page_id, 'movies', get_movie_schema())
db_info = json.loads(response.text)
db_id = db_info['id']

def insert_to_db(db_id, data):
    '''
    update a notion database
    '''
    body = {
        'parent': {'database_id': db_id},
        'properties': data
    }
    url = page_api_address
    response = requests.post(url, headers=headers, json=body)
    return response

from data_ingestion.notion_schema import get_movie_entry_template


def query_db(db_id):
    '''
    query a notion database
    '''
    url = db_api_address + db_id + '/query'
    response = requests.post(url, headers=headers, json={})
    data = json.loads(response.content)['results']

    return data

test_db_id = '90d2af9e-df29-4f85-9dc8-a41e1d8b6db2'
data = query_db(test_db_id)
response = insert_to_db(db_id, get_movie_entry_template())
print()
