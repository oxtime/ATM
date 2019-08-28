from libs import common
from db import db_handler
def register_interface(username,pwd):
    flag = common.check_user(username)
    if flag:
        return '用户已存在'
    else:
        content = {'username':username,'pwd':pwd,'extra':15000,'history':[],'shop_car':{}}
        db_handler.save_json(username,content)
        return '注册成功'

def login_interface(username,pwd):
    flag = common.check_user(username)
    if not flag:
        return False,'用户不存在'
    else:
        data = db_handler.read_json(username)
        if data['pwd'] == pwd:
            return True,'登录成功'
        else:
            return False,'密码错误'


def check_extra_interface(username):
    data = db_handler.read_json(username)
    return data['extra']