from dataclasses import dataclass
from typing import Optional, Type


@dataclass
class Person:
    name: str
    age: int
    position: Optional[str]
    weight: float

    # self reference
    def say_hi_to(self, other: 'Person') -> None:
        print(f"Hi {other.name}, I'm {self.name}")

    def copy(self) -> 'Person':
        return Person(**self.__dict__)


person_a = Person(name="Charles", age=21, position=None, weight=73.2)
person_b = Person(name="Xavier", age=35, position="professor", weight=73.2)

person_b.say_hi_to(person_a)

person_a_clone = person_a.copy()

from typing import Type


@dataclass
class Vehicle:
    engine_type: str


class Car(Vehicle):
    ...


class MotorCycle(Vehicle):
    ...


class Factory:

    @staticmethod
    def construct_vehicle(my_class: Type[Vehicle], engine_type: str) -> Vehicle:
        return my_class(engine_type=engine_type)


my_car = Factory.construct_vehicle(Car, "medium")
my_motorcycle = Factory.construct_vehicle(MotorCycle, "small")
