# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #
#                                                                          #
#  Similar to variables we can type functions and methods, using the next  #
#  syntax:                                                                 #
#                                                                          #
#  `def my_function(arg1: type_1, arg2: type2, ...) -> return_type : ...`  #
#                                                                          #
#  They can also be combined with default values                           #
#                                                                          #
#  `def my_function(arg1: type_1 = my_default_value) -> return_type : ...` #
#                                                                          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #


def sum_tuple(my_tuple: tuple[int, ...]) -> int:
    return sum(my_tuple)


def sort_keys(my_dict: dict) -> list[str]:
    return sorted(my_dict.values())


def multiply(a: int, b: int) -> int:
    return a * b


total = sum_tuple((1, 2, 3, 4))
my_keys = sort_keys({"key_2": 1, "key_3": 1, "key_1": 1, })
result = multiply(3, 5)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #
#                                                                          #
# *args and **kwargs are special since they are always tuple and dict      #
# therefore python expects that the type value we set for *args and        #
# **kwargs are the internal types:                                         #
#                                                                          #
# - `tuple[my_internal]`                                                   #
# - `dict[internal_key, internal_value]                                    #
#                                                                          #
#                                                                          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #


def average_of(*args: int) -> float:
    return sum(args) / len(args)


average = average_of(2, 4, 9)


def sort_kwargs(**kwargs: [str, float]) -> list[float]:
    return sorted(kwargs.values())


sorted_kwargs = sort_kwargs(kwarg_2=1.5, kwarg_1=5.6, kwargs_3=4.5)


# now something really useful is using literals for determining values
from typing import Literal, Union


def return_value(my_literal: Literal["integer", "string"]) -> Union[int, str]:
    if my_literal == "integer":
        return 25
    elif my_literal == "string":
        return "25"


# now we can call it
my_number = return_value("integer")

# if we call it with an invalid parameter it throws an error
my_number_2 = return_value("number")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #
#                                                                          #
# now there is an interesting scenario here, what about if we know that    #
# every time we request `return_value("string")` is going to be a string   #
# we should be able to use string methods right?                           #
#                                                                          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #

my_string = return_value("string")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #
#                                                                          #
# if we check the next statement it must complain about                    #
# `Item "int" of "Union[int, str]" has no attribute "replace"`             #
#                                                                          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #
other_string = my_string.replace("2", "3")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #
# the reason for this is that the type checker can't know when it is an    #
# integer or a string                                                      #
# then how can we tell that the return value is always the same depending  #
# of the parameters. That is a good use case for `overload` decorator      #
#                                                                          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #

from typing import overload


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #
#                                                                          #
#  First we defined the overload methods without a body since they are only#
#  meant to be use for typing  (you would need to fix you coverage file to #
#  this specific decorated functions since they are never going to be      #
#  called)                                                                  #
#                                                                          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #

@overload
def return_value_2(my_literal: Literal["integer"]) -> int: ...


@overload
def return_value_2(my_literal: Literal["string"]) -> str: ...

# and after decorating your typed method you must define the actual function


def return_value_2(my_literal: Literal["integer", "string"]) -> Union[int, str]:
    if my_literal == "integer":
        return 25
    elif my_literal == "string":
        return "25"

# now we can do the same case but now it should be fine

my_string = return_value_2("string")
result_string = my_string.replace("2", "3")

# overload can be used to specify  any special scenario and it can help when you have
# Union types(Optionals are actually Unions). We should avoid using Union but in case
# we can't, we always can be more specific using overload

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #
#                                                                          #
# bonus, we can type decorator functions but those are actually trickier   #
# and there is not a standard way to do it (at least mypy nor python have  #
# given guides about how to do it                                          #
#                                                                          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #

from typing import Callable


def print_args_method(my_function: Callable) -> Callable:
    def internal(*args, **kwargs):
        print(my_function)
        return my_function(*args, **kwargs)

    return internal
