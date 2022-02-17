from data import Data


class Person:
    """
    This class is a parent class, it loads data and get a persion infomaion.
    The check_menu method is a class method that get lunch menu.
    The change_pwd method changes password
    """
    
    data = Data

    def __init__(self,id):
        self.id = id
        role = id[ :3]        
        self.data = self.data.student_data if role == 'stu' else self.data.staff_data
        self.details = self.data[self.id]

    def __str__(self):
        return f"{self.id}: {self.details[1]}, {self.details[2]}, {self.details[3]}"

    @classmethod
    def check_menu(cls):
        for vairety, dish in cls.data.menu.items():
            print(f"{vairety: <8}: {dish}")

    def change_pwd(self, new_pwd):
        self.details[0] = new_pwd
        print("Password update successfully")

    
class Student(Person):
    """
    This is a child class. It inherits Person class's attributes and methods.
    It also has methods to check and update lunch order.
    """

    def check_order(self):
        print(f"You ordered {self.details[3]} lunch.")

    def update_order(self, qty):
        self.details[3] = qty
        print(f"Update succesfully!")


class Staff(Person):
    """
    This is a child class of Person. it has 6  class methods.
    """

    @classmethod
    def check_total(cls):
        total = 0
        for details in Person.data.student_data.values():
            total += details[3]      
        print(f"The total order is {total }")

    @classmethod
    def update_menu(cls, new_menu):
        Person.data.menu = new_menu
        print("Update successfully")

    @classmethod
    def check_student(cls, stu_id):
        print(Person(stu_id))
    
    @classmethod
    def add_student(cls, stu_details):
        st_id = Person.data.id_data['student'].pop(0)
        Person.data.student_data[st_id] = stu_details

    @classmethod
    def update_student(cls, stu_id , name, grade):
        Person.data.student_data[stu_id][1:3] = name, grade

    @classmethod
    def del_student(cls, stu_id):
        Person.data.student_data.pop(stu_id)
