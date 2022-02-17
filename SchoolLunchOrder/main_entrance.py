import get_input
import student_entrance
import staff_entrance

def main():
    """
    This is the first operation window. User can choose a role and start.
    it also check the validation of the input value.
    """
    while True:
        role = input("Choose your role(enter 'q' to quit): 1.student 2.staff: ")
        if role == 'q':
            exit()
        if role == '1':
            student_entrance.stu_entr()
        elif role == '2':
            staff_entrance.staff_entr()
        else:
            print("Invalid Input")
            continue


main()