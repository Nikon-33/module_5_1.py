class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        self.name = int(new_floor)
        x = 0
        if new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            while x < new_floor:
                x += 1
                print(x)



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)