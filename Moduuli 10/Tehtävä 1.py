
class Elevator:
    def __init__(self,bottom_floor,top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.location = 0

    def go_to_floor(self,floor):
        print("Going up!")
        while self.location <= floor:
            self.floor_up()
            print(f"You are at floor: {self.location}")
        print("Going down!")
        while self.location > 0:
            self.floor_down()
            print(f"You are at floor: {self.location}")

    def floor_up(self):
        self.location = self.location + 1

    def floor_down(self):
        self.location = self.location - 1

h = Elevator(0,10)
print("")
flo = int(input("Which floor would you like to go to?: "))
if flo <= h.top_floor:
    h.go_to_floor(flo-1)
else:
    print("That floor does not exist!")


