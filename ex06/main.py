from student import Student
from teacher import Teacher
from classroom import Classroom

def main():
    print('\n'*100)

    Wesleyclass = Classroom('Wesley', '3')
    Anandclass = Classroom('Anand', '2')
    Weslystud = Student('Wesley', ['Alice', 'Carol', 'Eve'])
    Weslyteach = Teacher('Wesley', ['Alice', 'Carol', 'Eve'])
    Anandstud = Student('Anand', ['Bob', 'Dave'])
    Anandteach = Teacher('Anand', ['Bob', 'Dave'])

    Wesleyclass.classinfo()
    Anandclass.classinfo()

    Weslyteach.teachgreeting()
    Weslystud.studentgreeting()
    Weslyteach.teachgreeting()
    Weslystud.studentgreeting()
    Weslyteach.teachgreeting()
    Weslystud.studentgreeting()
    Anandteach.teachgreeting()
    Anandstud.studentgreeting()
    Anandteach.teachgreeting()
    Anandstud.studentgreeting()

if __name__ == '__main__':
    main()