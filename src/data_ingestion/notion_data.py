MULTI_SELECT_FIELDS = ['director', 'writer', 'actor', 'region', 'language', 'labels']
TEXT_FIELDS = ['comment', 'release', 'iMDb']
DATE_FIELDS = ['created_on']
NUMBER_FIELDS = ['rating']
URL_FIELDS = ['property_url']
FILE_FIELDS = ['poster']

def get_schema(fields):
    schema_values = list(map(get_field_schema, fields))
    return dict(zip(fields, schema_values))

def generate_property_data(fields, data, field_ids):
    data_values = list(map(get_field_data, fields, data, field_ids))
    return dict(zip(fields, data_values))


def get_field_schema(field_name: str) -> dict:
    match field_name:
        case field_name if field_name in MULTI_SELECT_FIELDS:
            return {'multi_select': {}}
        case field_name if field_name in TEXT_FIELDS:
            return {'rich_text': {}}
        case field_name if field_name in DATE_FIELDS:
            return {'date': {}}
        case field_name if field_name in NUMBER_FIELDS:
            return {'number': {}}
        case field_name if field_name in URL_FIELDS:
            return {'url': {}}
        case field_name if field_name in FILE_FIELDS:
            return {'files': {}}
        case 'title':
            return {'title': {}}
        case _:
            raise ValueError(f'unknown field name: {field_name}')

def get_field_data(field: str, data: str, field_id: str) -> dict:
    match field:
        case field if field in MULTI_SELECT_FIELDS:
            assert data != '' # assume data is a string of labels separated by '/'
            return {'id': field_id, 'multi_select': [{'name': label} for label in data.split('/')]} 
        case field if field in TEXT_FIELDS:
            return {'id': field_id, 'rich_text': [{'type': 'text', 'text': {'content': data, 'link': None}}]}
        case field if field in DATE_FIELDS:
            return {'id': field_id, 'date': {'start': data, 'end': None}}
        case field if field in NUMBER_FIELDS:
            return {'id': field_id, 'number': data}
        case field if field in URL_FIELDS:
            return {'id': field_id, 'url': data}
        case field if field in FILE_FIELDS:
            return {'id': field_id, 'files': [{'name': data, 'type': 'external', 'external': {'url': data}}]}
        case 'title':
            return {'id': field_id, 'title': [{'type': 'text', 'text': {'content': data, 'link': None}}]}
        case _:
            raise ValueError(f'unknown field name: {field}')