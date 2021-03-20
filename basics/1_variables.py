# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#               Introduction for typing variables                         #
#                                                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  Variables can be typed using `:` after the name of the variable and    #
#  before the equal `=`  assignation operator. i.e                        #
#                                                                         #
#   `my_variable: my_type = ...`                                          #
#                                                                         #
#  Primitive types that don't require any import for typing are:          #
#  int, float, str, bool, dict, list, tuple, None                         #
#                                                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

int_number: int = 1
float_number: float = 1.1
string: str = "this is my string"
my_boolean: bool = True

my_dict: dict = {"key_1": 1, "key_2": 2}
my_list: list = [1, 2, 3, 4, 5]
my_tuple: tuple = (1, 2, 3, 4, 5, 6)
my_none: None = None

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #
#                                                                          #
#  Since python 3.9 we can use the primitives dict, list, tuple to specify #
#  internal types, as follow:                                              #
#  - dict[key_type, value_type]                                            #
#  - list[type]                                                            #
#  - tuple[type, ...]                                                      #
#                                                                          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  #

other_dict = {}
my_dict: dict[str, int] = my_dict
my_list: list[int] = my_list

# Tuple has a special syntax, since every position type is a specific type
# for that position

my_tuple_1: tuple[int] = (0,)
my_tuple_2: tuple[int, str, bool] = (0, "", False)

# if We want to specify tuple as we do with `list` we must use ellipsis object
# tuple[type, ...]

my_tuple_3: tuple[int, ...] = (1, 2, 3, 4, 5, 6)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                         #
#  Before python 3.9 we had to use specific types from `typing` module in #
#  to specify internal types, these types are `Dict`, `List` and `Tuple`  #
#  they are used similar as primitives in python 3.9, but you have to     #
#  import them, as follow:                                                #
#                                                                         #
#  from typing import Dict, List, Tuple                                   #
#  - Dict[key_type, value_type]                                           #
#  - List[type]                                                           #
#  - Tuple[type, ...]                                                     #
#                                                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from typing import Dict, List, Tuple

my_dict: Dict[str, int] = my_dict
my_list: List[int] = my_list

# Tuple has a special syntax, since every position type is a specific type
# for that position

my_tuple_1: Tuple[int] = my_tuple_1
my_tuple_2: Tuple[int, str, bool] = my_tuple_2

# if We want to specify tuple as we do with `list` we must use ellipsis object
# Tuple[type, ...]

my_tuple_3: Tuple[int, ...] = my_tuple_3

# If we want to specify callables we can't use `callable` builtin since this is not
# valid

my_callable: callable = lambda: None  # invalid, throws a check type error

# we must use typing.Callable instead

from typing import Callable

my_callable_2: Callable = lambda: None  # valid

# same for `any`

my_any_value: any = 1  # wrong

from typing import Any

my_any_value_2: Any = 2  # valid

# Similar to other types we can specify the types for Callable using `[[args_type,..], return_type]`

my_callable_3: Callable[[int], int] = lambda x: x*x


# as a bonus something really useful for implementations is using Literal values  as part of constants behavior
# Literal works as Literal[my_literal_value]

from typing import Literal

my_literal_number: Literal[2] = 2

# Setting other values drives to a validation issue
my_literal_number_2: Literal[2] = 3

# String also works

my_literal_string: Literal["Rocka", "rocks"] = "Rocka"

# or booleans

my_literal_boolean: Literal[True] = True

# this helps us to type special cases that can be seen in the functions module


# Also it is important to highlight that there is an special class for naming tuples

from typing import NamedTuple


# this is a good replacement for config tuples since we can actually understand which
# values are save in each position

class UserTuple(NamedTuple):
    name: str
    age: int


my_user_tuple: tuple[str, int] = ("Carlos", 25)
my_user_tuple_2: UserTuple = UserTuple(*my_user_tuple)


# We can access using index as a usual tuple

name, age = my_user_tuple[0], my_user_tuple[1]
name_2, age_2 = my_user_tuple_2[0], my_user_tuple_2[1]

# Or using names
name_3, age_3 = my_user_tuple_2.name, my_user_tuple_2.age

# or Even unpack

name_4, age_4 = my_user_tuple
name_5, age_5 = my_user_tuple_2

name_2 = 2  # This must throw an error since name_2 is `str`


# We can even type dictionaries
from typing import TypedDict


class ExtraInfo(TypedDict):
    birthday: str


my_extra_info: ExtraInfo = {"birthday": "Saturday"}
my_extra_info_2: ExtraInfo = {"birthday": 15}
my_extra_info_3: ExtraInfo = {"no_a_key": "Saturday"}
my_extra_info_4: ExtraInfo = {}

# Sadly in python we can't specify which fields are skippable as in typescript using `myField?`
# but we can actually tell python that we don't want to be that strict when there are missing
# fields using total=False

class MyUserDict(TypedDict):
    name: str
    age: int

    extra_info: ExtraInfo


class MyChildDict(MyUserDict):
    weight: int

# Doing that we can skip some fields and still getting a valid typing
valid_user_dict_1: MyUserDict = {"name": "Carlos", "age": 15}

valid_user_dict_2: MyUserDict = {"name": "Carlos", "age": 15, "extra_info": {"birthday": "sunday"}}

# breaking check with wrong values for TypedDict
invalid_user_dict_1: MyUserDict = {"name": "Carlos", "age": 15, "extra_info": "invalid_value"}
invalid_user_dict_4: MyUserDict = {"name": "Carlos", "age": 15, "extra_info": {}}
invalid_user_dict_2: MyUserDict = {"name": "Carlos", "age": 15, "invalid_key": {}}
invalid_user_dict_3: MyUserDict = {"name": "Carlos", "age": 15.6}
