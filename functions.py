from math import sin, cos, tan

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mul(a, b):
    return a * b

def new_sin(a):
    return sin(a)

def new_cos(a):
    return cos(a)

def tg(a):
    return tan(a)

def ctg(a):
    return sin(a) / cos(a)

operation_for_not_registered_user = {
    '+': add,
    '-': sub,
    '/': div,
    '*': mul
}

operation_for_registered_user = {
    'sin': new_sin,
    'cos': new_cos,
    'tg': tg,
    'ctg': ctg
}
operation_for_registered_user.update(operation_for_not_registered_user)

def operation_for_auth(operation):
    for k, v in operation_for_registered_user.items():
        if k == operation:
            return v

def operation_for_not_auth(operation):
    for k, v in operation_for_not_registered_user.items():
        if k == operation:
            return v

def get_operation(is_loging_user, operation):   
    calc_object = operation_for_registered_user if is_loging_user else operation_for_not_registered_user
    for k, v in calc_object.items():
        if k == operation:
            return v


get_operation(True, 'sin')
get_operation(False, '+')