class Car:
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_dist = 0



car1 = Car("ABD-123", 142)

print("")
print(f"The registration number of the new car is {car1.reg_num}, it's max speed is {car1.max_speed}km/h."
      f"\nIt's currently moving at {car1.current_speed}km/h, and has travelled {car1.travelled_dist}km")