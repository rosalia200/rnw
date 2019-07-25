class Car(object):
  condition = "new"

  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg = mpg

  def display_car(self):
    print("This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg)))

  def drive_car(self):
    self.condition = "used"


my_car = Car("DeLorean", "silver", 88)

print(my_car.condition)
my_car.drive_car()
print(my_car.condition)
# len("eric")
# my_dict

# class Animal(object):
#   """Makes cute animals."""
#   is_alive = True
#   def __init__(self, name, age,):
#     self.name = name
#     self.age = age
# print( giraffe.name, giraffe.age, giraffe.is_alive)
# print (panda.name, panda.age,panda.)

#
# class Car(object):
#     condition = "new"
#     def __init__(self, model, color, mpg):
#        self.model = model
#        self.color = color
#        self.mpg   = mpg
#     def display_car(self):
#         print("This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg)))
#
#
# my_car = Car("DeLorean", "silver", 88)
# my_car.display_car()
#     def __init__(self, model, color, mpg):
#         self.model = model
#         self.color = color
#         self.mpg = mpg
#
#     def display_car(self):
#         print("This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg)))
# my_car = Car("DeLorean", "silver", 88)
#
# my_car.display_car()
#

#
# zebra = Animal("Jeffrey", 2)
# giraffe = Animal("Bruce", 1)
# panda = Animal("Chad", 7)
#
#
# class Car(object):
#     condition = "new"
#
# print( zebra.name, zebra.age, zebra.is_alive)