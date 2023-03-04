from functions import operation_for_auth, operation_for_not_auth
from auth import register, authorization, id_user, write_to_history, check_history
from datetime import datetime

time_today = datetime.now().strftime('%d-%m-%y')

switcher = True
while True:
    registration = input('Sign up/Log in/Guest: ').lower().strip()
    if registration == 'sign up':
        reg = True
        while reg:
            user_login = input('login >>> ').strip()
            user_password = input('paswword >>> ').strip()
            confirm_password = input('confirm password >>> ').strip()
            register(user_login, user_password, confirm_password)
            id_from_user = id_user(user_login)
            break    
        while switcher:
            try:
                first_number = int(input('Введіть перше число: ').strip())
                print('Команда для перегляду історії "history"\nЯкщо хочете закінчити напишіть "break')
                user_operation = input('Введіть операцію: ').lower().strip()
                calculate = operation_for_auth(user_operation)
                if user_operation == 'history':
                    check_history(id_from_user)
                if user_operation in ['sin', 'cos', 'tg', 'ctg']:
                    result = f'{user_operation}({first_number})={calculate(first_number)}'
                    print(result)
                    write_to_history(date=time_today, operation=result, user_id=id_from_user)
                elif user_operation in ['+', '-', '/', '*']:
                    second_number = int(input('Введіть другу цифру: ').strip())
                    a = first_number
                    r = calculate(first_number, second_number)
                    result = f'{first_number} {user_operation} {second_number} = {r}'     
                    print(result)
                    write_to_history(date=time_today, operation=result, user_id=id_from_user)
                elif user_operation == 'break':
                    switcher = False
            except ValueError:
                print('Введіть цифру')
            except ZeroDivisionError:
                print('Не можна ділити на нуль')

    elif registration == 'log in':
        cycle = True
        while cycle:
            try:
                user_login = input('Login: ').strip()
                user_password = input('Password: ').strip()
                id_from_user = id_user(user_login)
                print(authorization(user_login, user_password))
                break
            except ValueError:
                print('Логін/Пароль не вірний')
        while switcher:
            try:
                first_number = int(input('Введіть перше число: ').strip())
                print('Команда для перегляду історії "history"\nЯкщо хочете закінчити напишіть "break')
                user_operation = input('Введіть операцію: ').lower().strip()
                calculate = operation_for_auth(user_operation)
                if user_operation == 'history':
                    check_history(id_from_user)
                if user_operation in ['sin', 'cos', 'tg', 'ctg']:
                    result = f'{user_operation}({first_number})={calculate(first_number)}'
                    print(result)
                    write_to_history(date=time_today, operation=result, user_id=id_from_user)
                elif user_operation in ['+', '-', '/', '*']:
                    second_number = int(input('Введіть другу цифру: ').strip())
                    r = calculate(first_number, second_number)
                    result = f'{first_number}{user_operation}{second_number} = {r}'
                    print(result)
                    write_to_history(date=time_today, operation=result, user_id=id_from_user)
                elif user_operation == 'break':
                    switcher = False
            except ValueError:
                print('Введіть цифру')
            except ZeroDivisionError:
                print('Не можна ділити на нуль')

    elif registration == 'guest':
        while switcher:
            try:
                first_number = int(input('Введіть перше число: ').strip())
                print('Якщо хочете закінчити напишіть "break')
                user_operation = input('Введіть операцію: ').strip()
                calculate = operation_for_auth(user_operation)
                if user_operation in ['+', '-', '/', '*']:
                    second_number = int(input('Введіть другу цифру: ').strip())
                    a = first_number
                    calculate = operation_for_not_auth(user_operation)
                    result = calculate(first_number, second_number)
                    x = f'{first_number} {user_operation} {second_number} = {result}'
                    print(x)
                elif user_operation == 'break':
                    switcher = False
            except ValueError:
                print('Введіть цифру')
            except ZeroDivisionError:
                print('Не можна ділити на нуль')
    else:
        print('Введіть корректно')