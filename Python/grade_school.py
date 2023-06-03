from collections import namedtuple

Student = namedtuple('Student', ['name', 'grade'])

class School:
    """Given students' names along with the grade that they are in, create a roster for the school."""
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        """Add a student's name to the roster for a grade.""" 
        student = Student(name=name, grade=grade)
        self.students.append(student)

    def roster(self):
        """Get a sorted list of all students in all grades."""
        sorted_students = sorted(
            self.students,
            key=lambda student: (student.grade, student.name),
        )
        return [student.name for student in sorted_students]

    def grade(self, grade_number):
        """Get a list of all students enrolled in a grade."""
        return sorted(
            [student.name for student in self.students if student.grade == grade_number]
            )
