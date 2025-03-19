class Car:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_dist = 0

    def acceleration(self,speeds):
     self.current_speed = self.current_speed + speeds
     if self.current_speed > self.max_speed:
        self.current_speed = self.max_speed
     if self.current_speed < 0:
        self.current_speed = 0
     return self.current_speed


car1 = Car("ABD-123", 142)
speed1 = car1.acceleration(30)
speed2 = car1.acceleration(70)
speed3 = car1.acceleration(50)
print(f"The car is going at {car1.current_speed}kmh")
speed4 = car1.acceleration(-200)
print("The car made an emergency break!")
print(f"The car is going at {car1.current_speed}kmh")


print("")
print(f"The registration number of the new car is {car1.reg_num}, it's max speed is {car1.max_speed}km/h."
      f"\nIt's currently moving at {car1.current_speed}km/h, and has travelled {car1.travelled_dist}km")