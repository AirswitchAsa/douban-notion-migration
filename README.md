# douban-notion-migration

forked from [AlieZVzz/Douban-Notion](https://github.com/AlieZVzz/Douban-Notion)

note: the original repo contains movietracker.py that can be used to update the notion database based on recent douban activity. I removed this feature and limited this tool for data migration only.

part of the project notion-marker. to be used for data migration from douban to entry-based data format.

## usage

this python script uses the csv files containing the douban entries to create notion page objects. it currently runs locally with the supplied files only.

### prerequisite
- Google Chrome
- Tampermonkey (chrome plugin)
- JavaScript sciprt [豆瓣读书+电影+音乐+游戏+舞台剧导出工具](https://greasyfork.org/zh-CN/scripts/420999-豆瓣读书-电影-音乐-游戏-舞台剧导出工具)
####
- Python >= 3.7
- beautifulsoup4 == 4.11.1
- feedparser == 6.0.8
- requests == 2.28.1

### steps
1. export the csv files from douban using the script
2. generate notion API key and provide database id in `config.py`
3. execute `main.py` to update the corresponding notion databse 

## future plan
to make it easier to use, I plan to bundle it as an image, simplify the parameters and potentially deploy it as a data migration service.