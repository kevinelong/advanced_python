class Animal: #parent/base/superclass
  def __init__(self, txt): # constructor
    self.message = txt

  def speak(self): # function in a class is a method
    print(self.message)

class Dog(Animal): # inherit from Parent
  def __init__(self):
    super().__init__("woof!")


class Cat: 
  def speak(self):
    print("Meow")

def speak_all(animal_list):
    for a in animal_list:
        a.speak()
        
data = [
    Animal("Quack!"),
    Dog(),
    Cat(),
]

speak_all(data)
speak_all(data)