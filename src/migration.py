from data_ingestion.douban_csv import DoubanCSVBuilder
from notion_api import create_db, insert_to_db
from config import page_id
from data_ingestion.notion_data import (get_schema, generate_property_data,
                                        MOVIE_FIELDS)
import json


def movie_migration(page_id=page_id):
    # build movie data
    builder = DoubanCSVBuilder(movie_csv_path='../csv/test-db-movie.csv')
    movie_entries = builder.build_movie_entries()

    # create database
    schema = get_schema(MOVIE_FIELDS)
    response = create_db(page_id, 'movies', schema)
    db_info = json.loads(response.text)
    db_id = db_info['id']
    db_schema: dict = db_info['properties']

    # insert data to database
    for movie_data in movie_entries:
        fields = list(movie_data.keys())
        values = list(movie_data.values())

        field_ids = [db_schema[field]['id'] for field in fields]

        response = insert_to_db(
            db_id, generate_property_data(fields, values, field_ids))
        if response.status_code == 200:
            print('successfully inserted')
        else:
            print(json.loads(response.text)['message'])


movie_migration()
