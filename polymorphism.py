class Car:
  def move(self):
    return "Car is moving"
  
class Plane:
  def move(self):
    return "Plane is flying"
  
class Person:
  def move(self):
    return "Person is walking"

for mover in [Car(), Plane(), Person()]:
  print(mover.move())
