from confs import settings
import os
import json

def save_json(username,content):
    path = os.path.join(settings.DB_PATH,f'{username}.json')
    with open(path,'w',encoding='utf8') as f:
        json.dump(content,f)


def read_json(username):
    path = os.path.join(settings.DB_PATH, f'{username}.json')
    with open(path, 'r', encoding='utf8') as f:
        data = json.load(f)
        return data