#class Dog:
 #   pass
#print("")
#dog = Dog()
#dog.name = "Goober"
#dog.birth_year = 2002

#print(f"{d# og.name} was born in {dog.birth_year}")


#class Dog:
    #def __init__(self,name,birthyear):
        #self.name = name
        #self.birthyear = birthyear

#print("")
#dog = Dog("Goober",2002)

#print(f"{dog.name} was born in {dog.birthyear}.")

#class Dog:
    #def __init__(self,name,birthyear,sound ="Woof woof"):
       # self.name = name
      #  self.birthyear = birthyear
     #   self.sound = sound
    #def bark(self, times):
   #     for i in range (times):
  #          print(self.sound)
 #           return

#dog1 = Dog("Gooba", 2022)
#dog2 = Dog("Goober", 2020,"Yip Yip")


#dog1.bark(2)
#dog2.bark(4)
#print("")
#class Dog:
    #created = 0
    #def __init__(self,name,birthyear,sound ="Yeehaw"):
        #self.name = name
        #self.birthyear = birthyear
        #self.sound = sound
        #Dog.created = Dog.created + 1

#dog1 = Dog("Rhone",2030)
#dog2 = Dog("Hira",2062,"WOOF")
#dog3 = Dog("Aatu",2001)
#print(f"{Dog.created} dogs have been created")

#class Bog:
 #   def __init__(self,color):
  #      self.color = color
#    def change(self):
 #       self.color = "Blue"

#print("")
#C = input("Please enter a color that you wish your bog to be: ").capitalize()
#b = Bog(C)


#if C == "Red":
 #   Bog.change(b)
 #   print("Your bog is now " + b.color + ". We don't like red ones.")
 #   print("")
#else:
 #   print("Your bog is " + b.color + ".")


#class Book:
 #   def __init__(self,title,author,year_pub):
  #      self.title = title
   #     self.author = author
    #    self.year_pub = year_pub

    #def get_info(self):
     #   return "Title: " + self.title + ", Author: " + self.author + ", Published: " + self.year_pub + "."


#b1 = Book("Holly","Stephen King","2021")
#b2 = Book("Permutation city","Greg Egan","1994")

#print(b1.get_info())
#print(b2.get_info())

#class Vehicle:
 #   def __init__(self,make,model):
  #      self.make = make
   #     self.model = model

    #def start(self):
     #   print("Vehicle started.")

#class Car(Vehicle):
 #   def __init__(self,make,model,num_doors):
 #       super().__init__(make,model)
  #      self.num_doors = num_doors


   # def start(self):
    #    print("Car started with key")


#v = Vehicle("Marcedes","Beans")
#c = Car("Toyota","Corolla","4")

#v.start()
#c.start()


class Pet:
    def __init__(self,name, species):
        self.name = name
        self.species = species

class Person:
    def __init__(self,name,age,pet):
        self.name = name
        self.age = age
        self.pet = pet

    def show_pet(self):
        print(self.name + " owns " + dog.name + ". " + dog.name + " is a " + dog.species + ".")




dog = Pet("Orvald","Corgi")
p = Person("Gary","24",dog)


p.show_pet()




