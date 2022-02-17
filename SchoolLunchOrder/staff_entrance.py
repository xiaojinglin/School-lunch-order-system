
from classes import Person
from classes import Staff
import student_entrance
import get_input


def update_menu(staff):
    new_menu = get_input.get__new_menu()
    staff.update_menu(new_menu)


def check_stu(staff):
    stu_id = get_input.get_id('student')
    staff.check_student(stu_id)


def add_stu(staff):
    stu_details = get_input.get_stu_details()
    stu_details.insert(0, '1111')
    stu_details.append(0)
    staff.add_student(stu_details)
    print("Adding successful")


def update_stu(staff):
    stu_id = get_input.get_id('student')
    new_details = get_input.get_stu_details()
    staff.update_student(stu_id, new_details[0], new_details[1])
    print("Student information update successfully")


def del_stu(staff):
    stu_id = get_input.get_id('student')
    staff.del_student(stu_id)
    print("Student information delete successfully")


def staff_entr():
    staff_id = get_input.get_id('staff')
    get_input.check_pwd(staff_id, 'staff')
    staff = Staff(staff_id)
    while True:
            get_input.service('staff')
            enter = input("What do you want to do?('q' to quit) ")
            if enter == 'q':
                exit()
            if int(enter) not in range(1,9):
                print("Invalid Input!")
                continue            
            if enter == '1':
                Person.check_menu()
            elif enter == '2':
                update_menu(staff)
            elif enter == '3':
                staff.check_total()
            elif enter == '4':
                check_stu(staff)
            elif enter == '5':
                add_stu(staff)
            elif enter == '6':
                update_stu(staff)
            elif enter == '7':
                del_stu(staff)
            elif enter == '8':
                student_entrance.change_pwd(staff)
