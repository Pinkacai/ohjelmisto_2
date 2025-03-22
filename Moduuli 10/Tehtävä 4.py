import random

cars = []

class Car:
     def __init__(self,reg_num,max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_dist = 0
        self.time = 0


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
     def time_passed(self):
         self.time = self.time + 1
         return self.time


class Race:
    def __init__(self,name,dist,list_of_cars):
        self.name = name
        self.dist = dist
        self.list_of_cars = list_of_cars
    def hour_passes(self):
        i = 1
        for car in cars:
            car.acceleration(random.randint(-10, 15))
            car.drive(1)
            i = i +1
        return
    def print_status(self):
        cars.sort(key=lambda a: a.travelled_dist, reverse=True)
        print(f"{'Registration number:':<15} {'Distance (km)':<15} {'Current speed:':<15} {' top speed:':<10}")
        for car in cars:
            print(f"{car.reg_num:<24}{car.travelled_dist:<18}{car.current_speed:<15}{car.max_speed:<15}")
            print("")
    def race_finished(self):
        for car in cars:
            if car.travelled_dist >= 8000:
                return True
            else:
                return False

for i in range(1,11):
    reg_num = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    cars.append(Car(reg_num,max_speed))
r = Race(Car in cars,Car.drive,cars)



while not r.race_finished():
    r.hour_passes()
    #for car in cars:
        #if Car.time_passed(car) % 10 == 0:
    r.print_status()
            #print(Car.time_passed(car))
    r.race_finished()

if Race.race_finished:
    cars.sort(key= lambda a: a.travelled_dist, reverse=True)
    print("")
    print("Final Race Results:")
    print("")
    print(f"{'Registration number:':<15} {'Distance (km)':<15} {'Current speed:':<15} {' top speed:':<10}")
    for car in cars:
        print(f"{car.reg_num:<24}{car.travelled_dist:<18}{car.current_speed:<15}{car.max_speed:<15}")
        print("")