import random

cars = []
race_ongoing = True
class Car:
     def __init__(self,reg_num,max_speed):
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

     def drive(self,time):
         self.travelled_dist = self.travelled_dist + (time * self.current_speed)
         return self.travelled_dist


for i in range(1,11):
    reg_num = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(reg_num,max_speed))

while race_ongoing:
    for car in cars:
        car.acceleration(random.randint(-10, 15))
        car.drive(1)
        if car.travelled_dist >= 10000:
            race_ongoing = False
            break


cars.sort(key= lambda a: a.travelled_dist, reverse=True)
print("")
print("Final Race Results:")
print("")
print(f"{'Registration number:':<15} {'Distance (km)':<15} {'Current speed:':<15} {' top speed:':<10}")
for car in cars:
    print(f"{car.reg_num:<24}{car.travelled_dist:<18}{car.current_speed:<15}{car.max_speed:<15}")
    print("")








