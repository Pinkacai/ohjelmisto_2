class Elevator:
    def __init__(self,bottom_floor,top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.location = 0

    def go_to_floor(self,floor,name):
        print("")
        if self.location < floor:
            print(f"Elevator number {name} is going up!")
        if floor < self.location:
                print(f"Elevator number {name} is going down!")
        i = 1
        while self.location < floor:
            self.floor_up()
            print(f"Elevator {name} is at floor: {self.location}")
        while self.location > floor:
            self.floor_down()
            print(f"Elevator {name} is at floor: {self.location}")
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
            self.elevators[elevator_number].go_to_floor(floor,elevator_number)


    def fire_alarm(self):
        b.run_elevator(1, self.bottom_floor)
        b.run_elevator(2, self.bottom_floor)
        b.run_elevator(3, self.bottom_floor)
        b.run_elevator(4, self.bottom_floor)
        b.run_elevator(5, self.bottom_floor)
        b.run_elevator(6, self.bottom_floor)


b = Building(0,10,7)

b.run_elevator(1,10)
b.run_elevator(2,3)
b.run_elevator(3,9)
b.run_elevator(4,8)
b.run_elevator(5,5)
b.run_elevator(6,3)
print("")
print("There was a fire alarm!! ")
b.fire_alarm()



print("")
