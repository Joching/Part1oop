from person import Person

class Student(Person):

    def studentgreeting(self):
        student = self.studentlist[self.x]
        print (f'{student}: Good morning, {self.teacher}')
        self.x += 1