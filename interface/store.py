from libs import common
from db import db_handler


def shopping_interface(username,goods_price):
    goods = goods_price[0]
    price = goods_price[1]
    data = db_handler.read_json(username)
    if goods in data['shop_car']:
        data['shop_car'][goods] += price
    else:
        data['shop_car'][goods] = price
    db_handler.save_json(username,data)
    return f'{goods}已加入购物车 计{price}元'


def shopping_check(username):
    data = db_handler.read_json(username)
    return data['shop_car']

def shopping_car_pay(username,choice):

    if choice == 'y':
        data = db_handler.read_json(username)
        m = sum(data['shop_car'].values())
        data['extra'] -= m
        data['shop_car'].clear()
        data['history'].append(f'{username}支付了{m}元')
        db_handler.save_json(username,data)
        return f'支付成功 共{m},购物车已经清空'
    elif choice == 'n':
        return '购物车已保留'
    else:
        return '请好好输'