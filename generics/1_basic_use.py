# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #
#                                                                          #
# Generic types and Type Vars are a little be complicated to understand at #
# first but they are pretty handy when you want to specify complex typing  #
# let's begin with a function that takes a list of type T and return its   #
# last element.                                                            #
#                                                                          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #
from typing import Any


def get_last(my_list: list) -> Any:
    return my_list[-1]

my_list = ["1", "2", "3"]
my_last = get_last(my_list)

# that works but we lost our type and then we can use the result type wrongly
# since the type checks will not complain

result = my_last - 14  # not complaining but it will fail due to `str - int`

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #
#                                                                          #
#  We can fix this using TypeVar which allows to specify generic types     #
#                                                                          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #

from typing import TypeVar


T = TypeVar("T")  # String value must be the same as the variable name


def get_last_2(my_list: list[T]) -> T:
    return my_list[-1]


# now we can re try our previous scenario
my_last_2 = get_last_2(my_list)

result_2 = my_last_2 - 14  # now this will throws an error during type checking


# Now what about if we want to restrict our generic type to a limit type values for list?
# We can do it when defining our TypeVar

P = TypeVar("P", str, bool)  # restricting TypeVar to only support Union[str, int]


def get_last_3(my_list: list[P]) -> P:
    return my_list[-1]


my_last_2 = get_last_2(my_list)
my_last_3 = get_last_3([23, 24, 25])  # This is not allowed

# For restricting to only one type we need to use kwarg `bound`

Q = TypeVar("Q", bound=str)  # restricting TypeVar to only support `str`


def get_last_4(my_list: list[Q]) -> Q:
    return my_list[-1]


# Now that we have defined TypeVar we can define Generics which are convenient classes
# here is an example of a Mapping generic class taken from official python docs

from typing import Mapping

X = TypeVar('X')
Y = TypeVar('Y')


def lookup_name(mapping: Mapping[X, Y], key: X, default: Y) -> Y:
    try:
        return mapping[key]
    except KeyError:
        return default

my_dict: dict[str, bool] = {"typing_rocks": True, "typing_is_hard": False}
my_truth = lookup_name(my_dict, "typing_rocks", True)

