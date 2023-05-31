from notion_api import DataBase_item_query, DataBase_additem
from notion_import import film_info2, download_picture 
import time
from config import *

def run():
    notion_moives = DataBase_item_query(databaseid)
    for item in notion_moives:
        print(item)
        watch_time = item['properties']['观看时间']['date']['start']
        movie_url = item['properties']['影片链接']['url']
        movie_url = movie_url.replace('http://movie.douban.com/subject/', 'https://movie.douban.com/subject/')
        comment = ''
        title, movie_type, director = film_info2(movie_url)
        cover_url = download_picture(movie_url)
        score = "⭐⭐"
        body = {
            'properties': {
                '名称': {
                    'title': [{'type': 'text', 'text': {'content': str(title)}}]
                },
                '观看时间': {'date': {'start': str(watch_time)}},
                '评分': {'type': 'select', 'select': {'name': str(score)}},
                '封面': {
                    'files': [{'type': 'external', 'name': '封面', 'external': {'url': str(cover_url)}}]
                },
                '有啥想说的不': {'type': 'rich_text',
                                'rich_text': [
                                    {'type': 'text', 'text': {'content': str(comment)}, 'plain_text': str(comment)}]},
                '影片链接': {'type': 'url', 'url': str(movie_url)},
                '类型': {'type': 'multi_select', 'multi_select': [{'name': str(itemm)} for itemm in movie_type]},
                '导演': {'type': 'multi_select', 'multi_select': [{'name': str(itemm)} for itemm in director]},

            }
        }
        print(body)
        DataBase_additem(databaseid, body, title)
        time.sleep(3)


if __name__ == 'main':
    run()
