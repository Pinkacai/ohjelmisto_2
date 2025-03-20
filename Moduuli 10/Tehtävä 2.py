class Elevator:
    def __init__(self,bottom_floor,top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.location = 0

    def go_to_floor(self,floor):
        print("Going up!")
        while self.location <= floor:
            self.floor_up()
            print(f"{elevator_num} is at floor: {self.location}")
        print("Going down!")
        while self.location > 0:
            self.floor_down()
            print(f"{elevator_num} is at floor: {self.location}")

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
            self.elevator_num = f"Elevator no.{i}"
            self.elevators.append(self.elevator_num)

    def run_elevator(self,elevator_number,floor):
        elevator_number = Elevator(self.bottom_floor,self.top_floor)
        if flo <= b.top_floor:
            elevator_number.go_to_floor(flo-1)
        else:
            print("That floor does not exist!")

b = Building(0,10,6)
print("")
flo = int(input("Which floor would you like to go to?: "))

for i in range(1,b.amt_of_elevators+1):
    elevator_num = f"Elevator no.{i}"
print(b.elevators)
b.run_elevator(3,5)

