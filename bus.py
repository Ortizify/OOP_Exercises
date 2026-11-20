
class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(person.name, "entered the bus")
        else:
            print("The bus is full")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(person.name, "left the bus")
        else:
            print("Passenger not found")


bus = Bus(2)

person1 = Person("John")
person2 = Person("Maria")
person3 = Person("David")

bus.add_passenger(person1)
bus.add_passenger(person2)
bus.add_passenger(person3)

bus.remove_passenger(person1)
bus.add_passenger(person3)
