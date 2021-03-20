from typing import Protocol, Literal


class Vehicle(Protocol):
    name: str

    def turn_on(self) -> None: ...

    def turn_off(self) -> None: ...


class Factory(Protocol):

    def construct_vehicle(self) -> Vehicle: ...


class Car(Vehicle):
    name: str = "car"

    def turn_on(self) -> None:
        print("turning the car on")


class CarFactory(Protocol):

    def construct_vehicle(self) -> Car:
        return Car()


class MotorCycle(Vehicle):
    name: str = "motor cycle"

    def turn_on(self) -> None:
        print("turning the motorcycle on")


class MotorCycleFactory(Protocol):

    def construct_vehicle(self) -> MotorCycle:
        return MotorCycle()


class Concessionary:
    vehicle: Vehicle
    factory: Factory

    def __init__(self, vehicle_type: Literal["car", "motorcycle"]):
        if vehicle_type == "car":
            self.factory = CarFactory()
        elif vehicle_type == "motorcycle":
            self.factory = MotorCycleFactory()

    def client_buys(self) -> None:
        self.vehicle = self.factory.construct_vehicle()
