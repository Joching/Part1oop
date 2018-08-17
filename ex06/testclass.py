class Classroom:
    def __init__(self, teacher, studentlist):
        self.capacity = 20
        self.teacher = teacher
        self.studentlist = studentlist
        self.x = 0
        self.z = 0

    def classinfo(self):
        print (f'This classroom has a standard capacity of {self.capacity} and is run by {self.teacher}. It currently has {len(self.studentlist)} students')

    def teachgreeting(self):
        student = self.studentlist[self.x]
        print (f'{self.teacher}: Welcome to class, {student}')
        self.x += 1

    def studentgreeting(self):
        student = self.studentlist[self.z]
        print (f'{student}: Good morning, {self.teacher}')
        self.z += 1

    def printgreeting(self):
        for i in self.studentlist:
            self.teachgreeting()
            self.studentgreeting()
           
