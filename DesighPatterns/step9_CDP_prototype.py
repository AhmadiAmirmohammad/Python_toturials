#creational design pattern

#creational design patterns focus on object creation, dealing with the best
#way to create objcets while hiding the creation logic and making the system
# independent of how its objects are created, composed and represented.

#prototype allows object to be copied or cloned.
#Prototype creates new objects by copying an existing object (prototype) instead of calling a constructor.
#Prototype = clone instead of new

from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class Soldier(Prototype):
    def __init__(self, health: int , power: int, position: str, model_3d= None):
        self.health = health
        self.power = power
        self.position = position
        self.model_3d = model_3d
        print (f"expensive load 3D model: {self.model_3d}" )

    def attack(self):
        print(f"Soldier at {self.position} attacks with power {self.power}")

    def move(self, new_position:str):
        self.position = new_position
        print(f"clone creating copy of soldier at {self.position}")
        return copy.deepcopy(self)

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Soldier at {self.position} attacks with power {self.power}"

#step1. creating prototype only first time
print("=== CREATING PROTOTYPES (Expensive - once) ===\n")
base_soldier = Soldier(health=100, power=50, position="(0,0)")
print()

#step2. use a copy object( expensive create it) if need to use new instances
print("=== CREATING ARMY VIA CLONING (Cheap) ===\n")

soldier1 = base_soldier.clone()
soldier1.move("(10, 212)")
soldier1.health = 95  # minor change

soldier2 = base_soldier.clone()
soldier2.move("(320, 1165)")
soldier2.power = 600   # minor change

soldier3 = base_soldier.clone()
soldier3.move("(510, 311)")

print("\n=== MY ARMY ===")
print(soldier1)
print(soldier2)
print(soldier3)