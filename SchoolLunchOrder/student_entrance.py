from classes import Person
from classes import Student
import get_input


def change_pwd(stu):
    new_pwd = get_input.get_new_pwd()
    stu.change_pwd(new_pwd)


def update_order(stu):
    order = get_input.get_order()
    stu.update_order(order)


def stu_entr():
    stu_id = get_input.get_id('student')
    get_input.check_pwd(stu_id, 'student')
    stu = Student(stu_id)
    while True:
            get_input.service('student')
            enter = input("What do you want to do?('q' to quit) ")
            if enter == 'q':
                exit()
            if enter not in ['1', '2', '3', '4']:
                print("Invalid Input!")
                continue            
            if enter == '1':
                Person.check_menu()
            elif enter == '2':
                stu.check_order()
            elif enter == '3':
                update_order(stu)
            elif enter == '4':
                change_pwd(stu)

