class Elevator:
    def __init__(self,bottom_floor,top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.location = 0

    def go_to_floor(self,floor):
        print("Going up!")
        while self.location < floor:
            self.floor_up()
            print(f"Elevator number {elevator_number} is at floor: {self.location}")
        print("Going down!")
        while self.location > 0:
            self.floor_down()
            print(f"Elevator number {elevator_number} is at floor: {self.location}")

    def floor_up(self):
        self.location = self.location + 1

    def floor_down(self):
        self.location = self.location - 1

class Building:
    def __init__(self,bottom_floor,top_floor,amt_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.amt_of_elevators = amt_of_elevators
        self.elevators = []

        for i in range(1,amt_of_elevators + 1):
            self.elevators.append(Elevator(self.bottom_floor,self.top_floor))

    def run_elevator(self,elevator_number,floor):
            self.elevators[elevator_number].go_to_floor(floor)

flo = int(input("Which floor would you like to go to?: "))
b = Building(0,10,6)

elevator_number = int(input("Which elevator would you like to use?(1-6): "))
b.run_elevator(elevator_number,flo)
print("")





