class Campus:
    def __init__(self, buildings, num_buildings, capacity):
        self.buildings = buildings
        self.num_buildings = num_buildings
        self.capacity = capacity

    def add_building(self, buildings, num_buildings, capacity):
        self.buildings = self.buildings + ', and ' + buildings
        self.num_buildings = self.num_buildings + num_buildings
        self.capacity = self.capacity + capacity
        
    def get_info(self):
        print (f'The campus has {self.num_buildings} building(s) with a combined capacity of {self.capacity} people')
    def name_b(self):
        print(f'The buildings on campus are {self.buildings}')









    # print (self.num_buildings)
    # pass
    # buildings
    # num_buildings
    # capacity
    # def get_info():
    # def add_building():