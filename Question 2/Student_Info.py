class  Student:
    
    def __init__(self, name, roll_number, age, contact):
        self.__name = name
        self.__roll_number = roll_number
        self.__age = age
        self.__contact = contact

        # self._freeze()

    # Getter methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_roll_number(self):
        return self.__roll_number
    
    def get_contact(self):
        return self.__contact

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number
   
    def set_contact(self, contact):
        self.__contact = contact
    

class StudentProgram:
    def __init__(self):
        self.students = []

    def add_student(self,Student:object ):
        self.students.append(Student)

    def add_student(self, name, roll_number, age, contact):
        student = Student(name, roll_number, age, contact)
        self.students.append(student)

    def display_student_details(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                print("Student Details:")
                print(f"Name: {student.get_name()}")
                print(f"Roll Number: {student.get_roll_number()}")
                print(f"Age: {student.get_age()}")
                print(f"Contact: {student.get_contact()}")
                return

        print("Student not found.")
    

    def update_student_details(self, roll_number, name, age, contact):
        for student in self.students:
            if student.roll_number == roll_number:
                student.name = name
                student.age = age
                student.contact = contact
                print("Student details updated.")
                return

        print("Student not found.")


    def view_all_students(self):
        print("Student Details:")
        for student in self.students:
            print(f"Name: {student.get_name()}")
            print(f"Roll Number: {student.get_roll_number()}")
            print(f"Age: {student.get_age()}")
            print(f"Contact: {student.get_contact()}")
            print("------------------")


    def delete_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print("Student deleted.")
                return

        print("Student not found.")


student1 = Student("Alice1", 1, 10, 8448743791)
student2 = Student("Alice2", 2, 20, 8448743792)
student3 = Student("Alice3", 3, 30, 8448743793)
student4 = Student("Alice4", 4, 40, 8448743794)

s1 = StudentProgram()
print(s1.view_all_students())
s1.add_student("Alice4", 4, 40, 8448743794)
s1.add_student(student1)
print(s1.view_all_students())
