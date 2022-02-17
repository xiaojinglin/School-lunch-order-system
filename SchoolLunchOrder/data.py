class Data:
    student_data = {'stu1': ['1111', 'John', '1st', 1],
                    'stu2': ['1111', 'Jake', '2nd', 1],
                    'stu3': ['1111', 'Jane', '3rd', 1]
                    }
                    
    staff_data = {'staff1': ['1111', 'Bela', 'staff'],
                  'staff2': ['1111', 'Arby', 'staff'],
                  'man1': ['1111', 'Joe', 'manager']
                 }

    menu = {'protein': 'fish',
            'veggies': 'salad or green been',
            'drink': 'juice or milk'
            }

    id_data = {
                'student':['stu4','stu5','stu6','stu7','stu8',],
                'staff':['staff3','staff4','staff5','staff6','staff7','staff8',],
              }

    def __init__(self, id):
        self.id = id
        role = id[ :3]        
        self.data = Data.student_data if role == 'stu' else Data.staff_data

    def get_info(self):
        return self.data[self.id]
   
    def update_info(self, new_info):
        self.data[self.id] = new_info

    @classmethod
    def total(cls):
        total = 0
        for details in cls.student_data.values():
            total += details[3]
        return total