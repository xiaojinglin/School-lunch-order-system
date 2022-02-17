
from classes import Person

data = Person.data


def service(role):
        service = {
                    'student': [ 'check menu', 'check order', 'update order', 'change password'],
                    'staff': ['check menu', 'update menu', 'check total', 
                                'check student', 'add student', 'update student', 
                                'delete student','change password']
                }    
        print("*******************************")
        for i in list(enumerate(service[role],start = 1)):
            print(f"{i[0]} . {i[1]}")
        print("*******************************")


def get_data(role):
    return data.student_data if role == 'student' else data.staff_data


def get_id(role):
    data = get_data(role)
    ids = list(data.keys())
    while True:        
        id = input('Enter ID: ')
        if id not in ids:
            print("This id is not in the system")
            continue
        else:
            break
    return id


def check_pwd(id, role):
    data = get_data(role)
    while True:
        pwd = input("Enter password: ")        
        if pwd != data[id][0]:
            print("password is not correct")
            continue
        else:
            break


def get_new_pwd():
    while True:
        new_pwd = input("New password(6 characters long): ")
        if len(new_pwd) != 6:
            print("New password should be 6 characters long.")
            continue
        else:
            break
    return new_pwd


def get__new_menu():
    varieties = ['protein', 'veggies', 'drink']
    new_menu = {variety: input(f"{variety}: ") for variety in varieties}
    return new_menu



def get_stu_details():
    details = ['name', 'grade']
    stu_details = [input(f"{info}: ") for info in details]
    return stu_details


def get_order():
    while True:
        order = input("Enter your new order(not more than 3): ")
        if order not in ['1', '2', '3']:
            print("Invalid Input")
            continue
        else:
            break
    return int(order)