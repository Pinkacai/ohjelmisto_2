print("")
cars = []
time = 0
class Car:
     def __init__(self,reg_num,max_speed,type):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.type = type
        self.current_speed = 0
        self.travelled_dist = 0


     def acceleration(self,speeds):
        self.current_speed = speeds
        #if self.current_speed > self.max_speed:
           # self.current_speed = self.max_speed
        #if self.current_speed < 0:
            #self.current_speed = 0
        return self.current_speed

     def drive(self,time):
         self.travelled_dist = self.travelled_dist + (time * self.current_speed)
         return self.travelled_dist

     class Race:
         def __init__(self, name, dist, list_of_cars):
             self.name = name
             self.dist = dist
             self.list_of_cars = list_of_cars

         def hour_passes(self):
             for car in self.list_of_cars:
                 car.drive(1)
             return


class ElectricCar(Car):
    def __int__(self,reg_num,max_speed,type,capacity):
        capacity = 0
        super().__init__(reg_num,max_speed,type)
        self.capacity = capacity + capacity

    def print_information(self):
        print(f"{self.reg_num}: An {self.type} car, which drove {self.travelled_dist}km in {time} hours.")


class GasolineCar(Car):
    def __int__(self,reg_num,max_speed,type,volume):
        volume = 0
        super().__init__(reg_num,max_speed,type)
        self.volume = volume + volume
    def print_information(self):
        print(f"{self.reg_num}: A {self.type} car, which drove {self.travelled_dist}km in {time} hours.")



electric = ElectricCar("ABC-15",180,"Electric")
electric.acceleration(170)
gasoline = GasolineCar("ACD-123",165,"Gasoline")
gasoline.acceleration(160)
cars.append(electric)
cars.append(gasoline)


r = Car.Race("Great escape",8000,cars)
while time < 3:
    for i in cars:
        i.drive(1)
    time += 1
for i in cars:
    i.print_information()
