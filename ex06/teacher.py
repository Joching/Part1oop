from person import Person

class Teacher(Person):

    def teachgreeting(self):
        student = self.studentlist[self.x]
        print (f'{self.teacher}: Welcome to class, {student}')
        self.x += 1