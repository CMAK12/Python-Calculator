import os
import json
import hmac


def check_pass(pass1, pass2):
    return pass1 == pass2


def register(user_login, user_password, user_confirm_password):
    repeat_register = True
    user = None
    while repeat_register:
        login = user_login
        password = user_password
        confirm_password = user_confirm_password
        try:
            if check_pass(password, confirm_password):
                try:
                    user = write_to_db(login=login, password=password)
                    repeat_register = False
                    print('register success!')
                except ValueError as e:
                    repeat_register = True
                    print(e)
            else:
                print('incorrect password')
        except Exception as e:
            print(e)
    return user


def write_to_db(**new_user):
    file = os.path.join('users.json')

    def check_user_in_db(login):
        nonlocal file
        with open(file, 'r') as users:
            list_users = json.load(users)
            for user in list_users:
                if user['login'] == login:
                    raise ValueError('user already exists with login {}'.format(login))

    with open(file, 'r') as users:
        user_data = json.load(users)
        if len(user_data) == 0:
            new_user.update(
                {'id': 1}
            )
        else:
            check_user_in_db(login=new_user['login']) # raise ValueError('user already exists with login {}'.format(login))
            new_id = user_data[-1]['id'] + 1
            new_user.update({
                'id': new_id
            })
    user_data.append(new_user)
    with open(file, 'w+') as f:
        json.dump(user_data, f)
    return new_user


def authorization(user_login, user_password):
    file = os.path.join('users.json')
    cycle = True
    while cycle:
        with open(file, 'r') as file:
            list_users = json.load(file)
            for user in list_users:
                if user['login'] == user_login and user['password'] == user_password:
                    cycle = False
                    return 'Ви успішно залогінились'
                else:
                    cycle = True
                    raise ValueError('Такого логіну немає')

def id_user(log):
    file = os.path.join('users.json')
    id_user = None
    with open(file, 'r') as users:
        list_users = json.load(users)
        for some_user in list_users:
            if some_user['login'] == log:
                id_user = some_user['id']
    return id_user

def write_to_history(**new_history):
    file = os.path.join('history.json')
    res_new_history = {}
    with open(file, 'r') as history:
        history_data = json.load(history)
        if len(history_data) == 0:
            res_new_history(
                {'id': 1}
            )
        else:
            new_id = history_data[-1]['id'] + 1
            res_new_history.update({
                'id': new_id
            })
            res_new_history.update(new_history)
            history_data.append(res_new_history)
            with open(file, 'w+') as f:
                json.dump(history_data, f)
            return new_history
        
def check_history(user_id):
    file = os.path.join('history.json')
    with open(file, 'r') as history:
        user_info = json.load(history)
        for user in user_info:
            if user['user_id'] == user_id:
                print(user)