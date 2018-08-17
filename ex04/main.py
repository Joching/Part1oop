from campus import Campus
from building import Building
def main():
    mb = Building('"Math Building"', 25)
    sb = Building('"Science Building"', 17)
    mb.get_info()
    sb.get_info()

    campus_total = Campus('"Math Building"', 1, 25)
    campus_total.add_building('"Science Building"', 1, 17)
    campus_total.get_info()
    campus_total.name_b()

# mb = ('Math Building', 25)
# sb = ('Science Building', 17)
# b = Building()
# b.get_info('"Math Building"', 25)
# b.get_info('"Science Building"', 17)

if __name__ == '__main__':
    main()