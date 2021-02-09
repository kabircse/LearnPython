class StudentClass:
    """
        The __init__() is called automatically every time the class create a new object.
        The self is a reference to the current instance of the class, and used to access variables that belongs to class.
        You can call it  whatever you like, but it has to be the first parameter of any function in the class:
    """

    def __init__(self, roll, name):
        self.roll = roll
        self.name = name

    def get_details(self):
        return "Student details: {}, roll: {}".format(self.name, self.roll)


student = StudentClass(1, "kabir Hossain")
print("Student roll:{}, name: {}".format(student.roll, student.name))
print(student.get_details())


# Inheritance
class ExamClass(StudentClass):
    SchoolCode = '1205'
    exam_name = ''

    def get_exam_name(self):
        return self.exam_name

    def set_exam_name(self, exam_name):
        self.exam_name = exam_name


# student = StudentClass(2, 'Abdullah')
exam = ExamClass(2, 'Abdullah')
exam.set_exam_name('final')
print(exam.get_details() + ' passed '+exam.get_exam_name() + ' exam.')
