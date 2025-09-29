class Classroom:
    pass 

class Student:
    def __init__(self,roll_no,name):
        self.roll_no = roll_no
        self.name = name
        self.__marks = {} # Private dictionary to store subject marks
        
    def get_marks(self):
        return self.__marks # Return the marks dictionary    
    
    def add_marks(self,subject,marks):
        self.__marks[subject] = marks # Add or update marks for a subject
        
    def avg_marks(self,total=0):
        for marks in self.__marks.values():
            total += marks
            
        average = total/len(self.__marks)
        return average if self.__marks else 0
        return self.__marks[id] # Return account if found
    
    def is_passed(self, passing_marks=40):
        # Return True if student has passed in all subjects, else False
        for marks in self.__marks.values():
            if marks < passing_marks:
                return False
        return True# Return True if all subjects are passed

    def cal_grade(self):
        if self.avg_marks()>=90:
            self.grade = 'A'
        elif self.avg_marks()>=80:
            self.grade = 'B'
        elif self.avg_marks()>=70:
            self.grade = 'C'
        elif self.avg_marks()>=60:
            self.grade = 'D'
        elif self.avg_marks()>=50:
            self.grade = 'E'
        else:
            self.grade = 'F'
        return self.grade # Calculate and return grade based on average marks

class ReportCard:
    def generate(self,student:Student):
        print(f"Name: {student.name} Roll No: {student.roll_no}")
        print("Subject Marks:")
        
        for subject,marks in student.get_marks().items():
            print(f"{subject}: {marks}")
        print(" ")
        print(f"Average Marks: {student.avg_marks():.2f}")
        # student.is_passed(41)
        # student.cal_grade(student.grade)
        
student1 = Student(1,"Alice")
for subject, marks in {"Math": 90, "Science": 90, "English": 98}.items():
    student1.add_marks(subject, marks)

if student1.is_passed(39):
    print("Student has passed in all subjects.")
else:
    print("Student has not passed in all subjects.")

#student1.cal_grade(91) # Calculate grade
student1.cal_grade() # Calculate grade
print(f"Grade: {student1.grade}")

report = ReportCard()
report.generate(student1)
        