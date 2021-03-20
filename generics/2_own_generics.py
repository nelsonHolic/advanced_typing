# We can construct our own generic classes using `Generic` class from `typing`
from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar("T")

# Using Generic[Type, ...]


class MyListHandler(Generic[T]):
    my_list: list[T]

    def __init__(self):
        self.my_list = []

    def add(self, val: T) -> None:
        self.my_list.append(val)

    def get_at(self, index: int) -> T:
        return self.my_list[index]


@dataclass
class Test:
    number: int

    def test(self) -> None:
        print(f"testing number {self.number}")


my_handler: MyListHandler[Test] = MyListHandler()

my_handler.add(Test(1))
my_handler.add(Test(2))
my_handler.add(Test(3))
my_handler.add(Test(4))

my_test_2 = my_handler.get_at(2)
my_test_2.test()

my_test_2.not_a_method()