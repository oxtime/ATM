from db import db_handler
import os
from confs import settings
def check_user(username):
    path = os.path.join(settings.DB_PATH, f'{username}.json')
    if os.path.exists(path):
        return True

def load_login(func):
    from core import src
    def inner(*args,**kwargs):
        if src.user_auth['user'] == None:
            src.login()
        else:
            res = func(*args,**kwargs)
            return res
    return inner