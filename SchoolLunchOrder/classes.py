from data import Data


class Person:

    data = Data
    def __init__(self,id):
        self.id = id
        data = Data(self.id)
        self.info = data.get_info()

    def __str__(self):
        return f"{self.id}: {self.info[1]}, {self.info[2]}, {self.info[3]}"
    
    def get(self):
        return self.info

    @classmethod
    def check_menu(cls):
        for vairety, dish in cls.data.menu.items():
            print(f"{vairety: <8}: {dish}")

    def change_pwd(self, new_pwd):
        self.info[0] = new_pwd
        print("Password update successfully")

    
class Student(Person):

    def check_order(self):
        print(f"You ordered {self.info[3]} lunch.")

    def update_order(self, qty):
        self.info[3] = qty
        print(f"Update succesfully!")


class Staff(Person):

    def check_total(self):
        total = Person.data.total()       
        print(f"The total order is {total }")

    def update_menu(self, new_menu):
        Person.data.menu = new_menu
        print("Update successfully")

    def check_student(self, stu_id):
        print(Person(stu_id))
 
    def add_student(self, stu_details):
        st_id = Person.data.id_data['student'].pop(0)
        Person.data.student_data[st_id] = stu_details

    def update_student(self, stu_id , name, grade):
        Person.data.student_data[stu_id][1:3] = name, grade

    def del_student(self, stu_id):
        Person.data.student_data.pop(stu_id)
