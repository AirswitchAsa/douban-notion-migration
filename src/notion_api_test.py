from notion_api import create_db, insert_to_db, query_db, retrieve_db
from config import page_id
import json
from data_ingestion.notion_data import get_schema, generate_property_data
from data_ingestion.constructor import MOVIE_FIELDS

schema = get_schema(MOVIE_FIELDS)
response = create_db(page_id, 'movies', schema)
db_info = json.loads(response.text)
created_db_id = db_info['id']


test_db_id = '90d2af9e-df29-4f85-9dc8-a41e1d8b6db2'
data = query_db(test_db_id)
db_info = retrieve_db(created_db_id)
db_id = db_info['id']
db_schema: dict = db_info['properties']

test_data = {
    'property_url': 'www.google.com',
    'created_on': '2021-01-01',
}
test_fields = list(test_data.keys())
test_values = list(test_data.values())

field_ids = [db_schema[field]['id'] for field in test_fields]

response = insert_to_db(db_id, generate_property_data(test_fields, test_values, field_ids))
print(json.loads(response.text)['message'])
