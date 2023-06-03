import csv
import numpy as np  
import requests
import re
from bs4 import BeautifulSoup
from builder import DataBuilder
from jsonschema import validate

movie_headers = {
    "Host": "movie.douban.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69",
}


def fetch_movie_data(movie_url):
    '''
    populate movie data from movie url by analyzing the html file
    '''
    # get movie page
    res = requests.get(movie_url, headers=movie_headers, allow_redirects=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = soup.find_all('div', id='content')
    moive_content = content[0]

    movie_data = {}
    # title and year
    title = moive_content.find('h1').find_all('span')
    title_year = title[0].text + ' ' + title[1].text
    movie_data['title'] = title_year

    # movie info
    base_information = moive_content.find('div', class_='subject clearfix')
    info = base_information.find('div', id='info').text.split('\n')
    split_info = np.array([info_item.split(': ') for info_item in info if info_item != ''], dtype='object').transpose()
    info_dict = dict(zip(split_info[0], split_info[1]))
    movie_data['region'] = info_dict.get('制片国家/地区', '')
    movie_data['language'] = info_dict.get('语言', '')
    if '首播' in info_dict:
        movie_data['release_date'] = info_dict.get('首播', '')
    else:
        movie_data['release_date'] = info_dict.get('上映日期', '')
    movie_data['labels'] = info_dict.get('类型', '')
    movie_data['director'] = info_dict.get('导演', '')
    movie_data['writer'] = info_dict.get('编剧', '')
    movie_data['actors'] = info_dict.get('主演', '')
    movie_data['iMDb'] = info_dict.get('IMDb', '')

    # movie poster url
    movie_data['poster'] = soup.find('div', class_='article').find_all('img')[0]['src']

    return movie_data

def parse_csv(filename):
    entries = []
    with open(filename,'r') as file:
        for line in csv.reader(file):
            entries.append(line)
    headers = entries[0]
    data = np.array(entries[1:]).transpose()
    entry_dict = dict(zip(headers, data))
    return entry_dict


class DoubanCSVBuilder(DataBuilder):

    def __init__(self, movie_csv_path=None, book_csv_path=None, music_csv_path=None, game_csv_path=None, drama_csv_path=None):
        self.movie_csv_path = movie_csv_path
        self.book_csv_path = book_csv_path
        self.music_csv_path = music_csv_path
        self.game_csv_path = game_csv_path
        self.drama_csv_path = drama_csv_path

    def build_movie_entries(self, validate_entry=False):
        # parse entry data from csv
        if self.movie_csv_path is None:
            raise ValueError('movie_csv_path is not specified')
        entry_dict = parse_csv(self.movie_csv_path)

        # build movie entries
        movie_entries = []
        for created_on, property_url, comment, rating in zip(entry_dict['打分日期'], entry_dict['条目链接'], entry_dict['我的短评'], entry_dict['个人评分']):
            movie_data = fetch_movie_data(property_url)
            movie_entry = {'created_on': created_on, 'property_url': property_url, 'comment': comment, 'rating': rating, **movie_data}
            # validate movie entry
            if validate_entry:
                validate(instance=movie_entry, schema=self.movie_schema)
            movie_entries.append(movie_entry)
        return movie_entries

    def build_book_entries(self):
        pass

    def build_music_entries(self):
        pass

    def build_game_entries(self):
        pass

    def build_drama_entries(self):
        pass

if __name__ == '__main__':
    filename = '../../csv/db-movie-20230530.csv'
    builder = DoubanCSVBuilder(movie_csv_path=filename)
    movie_entries = builder.build_movie_entries()
