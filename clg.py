class University:
    def __init__(self,university_name):
        self.name=university_name
    def showdetails(self):
        print(self.name)
class Course(University):
    def __init__(self, course_name):
        self.course = course_name
    def showdetails(self):
        print(self.course)
class Branch(Course):
    def __init__(self, university_name, course_name, branch_name):
      University.__init__(self, university_name)
      Course.__init__(self, course_name )
      self.branch = branch_name
    def showdetails(self):
        print(f"i am from {self.name},and from {self.course},and from {self.branch}")

class Student( Branch):
    def __init__(self, studentname, course_name,university_name, branch_name):
        self.student = studentname
        Branch.__init__(self,university_name,course_name,branch_name)


    def showdetails(self):
        print(f"my name is {self.student}, i am from {self.name} university, and i am from {self.branch} department, and i am pursing in {self.course}")

student_1=Student("rick","ai&ds","vit","engineering")
student_1.showdetails()
student_2=Student("grimes","cse","srm","engineering")
student_2.showdetails()

