from testclass import *

def main():
    print('\n'*100)
    Wesleyclass = Classroom('Wesley', ['Alice', 'Carol', 'Eve'])
    Anandclass = Classroom('Anand', ['Bob', 'Dave'])
    Wesleyclass.classinfo()
    Anandclass.classinfo()
    Wesleyclass.printgreeting()
    Anandclass.printgreeting()

if __name__ == '__main__':
    main()