class Classroom:
    def __init__(self, classteacher, numstud):
        self.classteacher = classteacher
        self.capacity = 20
        self.numstud = numstud

    def classinfo(self):
        print (f'This classroom has a standard capacity of {self.capacity} and is run by {self.classteacher}. It currently has {self.numstud} students')


