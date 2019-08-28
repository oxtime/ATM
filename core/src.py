from interface import user,bank,store
from libs import common
user_auth = {'user':None}

def register():
    username = input('请输入账号')
    pwd = input('请输入密码')
    msg = user.register_interface(username,pwd)
    print(msg)

def login():
    username = input('请输入账号')
    pwd = input('请输入密码')
    flag,msg = user.login_interface(username, pwd)
    print(msg)
    if flag:
        user_auth['user'] = username
@common.load_login
def check_extra():
    m = user.check_extra_interface(user_auth['user'])
    print(f'余额为{m}元')
@common.load_login
def withdraw():
    m = input('请输入要取多少钱')
    m = int(m)
    msg = bank.withdraw_interface(user_auth['user'],m)
    print(msg)
@common.load_login
def repay():
    m = input('请输入要还的钱')
    m = int(m)
    msg = bank.repay_interface(user_auth['user'],m)
    print(msg)
@common.load_login
def transfer():
    trf_name = input('请输入要转的用户')
    m = int(input('请输入转入的金额'))
    msg = bank.transfer_interface(trf_name,user_auth['user'],m)
    print(msg)
@common.load_login
def history():
    lt = bank.history_interface(user_auth['user'])
    for i in lt:
        print(i)

@common.load_login
def shopping():
    shopping_list = [
        ['雪碧',20],
        ['芬达', 80],
        ['可乐', 30],
        ['美连达', 10],
        ['脉动', 50],

    ]
    while True:
        for ind,v in enumerate(shopping_list):
            print(ind,v)
        choice = input('请选择商品,q退出')
        if choice == 'q':
            break
        if not choice.isdigit():
            continue
        choice = int(choice)
        goods_price = shopping_list[choice]
        msg = store.shopping_interface(user_auth['user'],goods_price)
        print(msg)
@common.load_login
def shopping_car():
    dic = store.shopping_check(user_auth['user'])
    print(dic)
    choice = input('是否支付y or n')
    msg = store.shopping_car_pay(user_auth['user'],choice)
    print(msg)

def logout():
    user_auth['user'] = None
    print('用户已注销')


def run():
    func_msg = '''   
   1.注册
   2.登录
   3.查看额度
   4.提现
   5.还款
   6.转账
   7.查看流水
   8.购物功能
   9.查看购物车
   0.注销
   q.退出'''
    go = {'1':register,'2':login,'3':check_extra,'4':withdraw,'5':repay,'6':transfer,
          '7':history,'8':shopping,'9':shopping_car,'0':logout}
    while True:
        print(func_msg)
        choice = input('请输入功能,q退出')
        if choice == 'q':
            break
        if not choice.isdigit():
            continue
        go.get(choice)()