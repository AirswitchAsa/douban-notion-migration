import requests
import json
from config import notion_api

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
        'parent': {
            'type': 'page_id',
            'page_id': page_id
        },
        'title': [{
            'type': 'text',
            'text': {
                'content': title,
                'link': None
            }
        }],
        'properties': property_schema
    }
    response = requests.post(db_api_address, headers=headers, json=data)
    return response


def insert_to_db(db_id: str, data: dict):
    '''
    update a notion database
    '''
    body = {'parent': {'database_id': db_id}, 'properties': data}
    url = page_api_address
    response = requests.post(url, headers=headers, json=body)
    return response


def query_db(db_id):
    '''
    query a notion database
    '''
    url = db_api_address + db_id + '/query'
    response = requests.post(url, headers=headers, json={})
    data = json.loads(response.content)['results']
    return data


def retrieve_db(db_id):
    '''
    query a notion database
    '''
    url = db_api_address + db_id
    response = requests.get(url, headers=headers, json={})
    data = json.loads(response.content)
    return data
