# Python typing has its own `Interface` implementation but in this case
# it is called `Protocol`. We are going to see some of them here
from dataclasses import dataclass
from typing import Iterable

# iterable it's just the protocol for a class which implements the __iter__ method
my_iterable: Iterable[int] = [1, 2, 3, 4, 5, 6]
my_iterable_2: Iterable[int] = (1, 2, 3, 4, 5, 6,)

from typing import Sized


@dataclass
class MySized:
    len: int

    def __len__(self) -> int:
        return self.len


my_sized: Sized = MySized(3)

# Callable is also a Protocol that ensure when an object implements __call__
from typing import Callable


class MyAwesomeCallable:

    def __call__(self, *args, **kwargs) -> None:
        print("awesome")


my_valid_callable: Callable = MyAwesomeCallable()
my_valid_callable_2: Callable = lambda *args, **kwargs: print("lambda callable")


# So a Protocol is just a utility for specify a structure we want that a variable/parameter
# has
from typing import Protocol, TypeVar, Generic


class Barker(Protocol):
    def bark(self) -> None: ...  # this is not abbreviated, it is actually valid code


class Dog:
    def bark(self) -> None:
        print("woof")


class Person:
    def speak(self) -> None:
        print("not woof")


def bark(doglike_entity: Barker) -> None:
    doglike_entity.bark()


bark(Dog())  # valid
bark(Person())  # Argument 1 to "bark" has incompatible type "Person"; expected "Barker"


class NamedProtocol(Protocol):
    name: str
    last_name: str

    @property
    def full_name(self) -> str: ...


T = TypeVar("T", bound=NamedProtocol)


class ListOfNames(Generic[T]):
    my_list: list[T]

    def __init__(self):
        self.my_list = []

    def add(self, val: T) -> None:
        self.my_list.append(val)

    def get_at(self, index: int) -> T:
        return self.my_list[index]

    def get_names(self) -> list[str]:
        result: list[str] = []
        for item in self.my_list:
            result.append(item.full_name)

        return result


@dataclass
class ParentClass:
    name: str
    last_name: str

    @property
    def full_name(self) -> str:
        return self.name + self.last_name


class ValidNamedClass(ParentClass):
    ...


class InvalidNamedClass(ParentClass):

    @property
    def full_name(self) -> int:
        return 25


my_list_of_names: ListOfNames[ParentClass] = ListOfNames()

my_list_of_names.add(ValidNamedClass(name="test", last_name="valid"))
my_list_of_names.add(InvalidNamedClass(name="test", last_name="valid"))