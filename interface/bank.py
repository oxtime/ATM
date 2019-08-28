from libs import common
from db import db_handler


def withdraw_interface(username,m):
    data = db_handler.read_json(username)
    if m*1.05>data['extra']:
        return '余额不足'
    else:
        data['extra'] -= m*1.05
        data['history'].append(f'{username}取款{m}元')
        db_handler.save_json(username,data)
        return '取款成功'

def repay_interface(username,m):
    data = db_handler.read_json(username)
    data['extra'] += m
    data['history'].append(f'{username}还款{m}元')
    db_handler.save_json(username,data)
    return '还款成功'

def transfer_interface(trf_name,username,m):
    flag = common.check_user(trf_name)
    if not flag:
        return '用户不存在'
    else:
        trf_data = db_handler.read_json(trf_name)
        user_data = db_handler.read_json(username)
        if m > user_data['extra']:
            return '余额不足'
        else:
            trf_data['extra'] += m
            user_data['extra'] -= m
            trf_data['history'].append(f'{trf_name}收到了{username}转的{m}元')
            user_data['history'].append(f'{username}向{trf_name}转了{m}元')
            db_handler.save_json(username,user_data)
            db_handler.save_json(trf_name,trf_data)
            return '转账成功'

def history_interface(username):
    data = db_handler.read_json(username)
    return data['history']