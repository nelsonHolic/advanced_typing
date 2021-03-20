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

class MyUserDict(TypedDict, total=False):
    name: str
    age: int

    extra_info: ExtraInfo

# Doing that we can skip some fields and still getting a valid typing
valid_user_dict_1: MyUserDict = {"name": "Carlos", "age": 15}

valid_user_dict_2: MyUserDict = {"name": "Carlos", "age": 15, "extra_info": {"birthday": "sunday"}}

# breaking check with wrong values for TypedDict
invalid_user_dict_1: MyUserDict = {"name": "Carlos", "age": 15, "extra_info": "invalid_value"}
invalid_user_dict_4: MyUserDict = {"name": "Carlos", "age": 15, "extra_info": {}}
invalid_user_dict_2: MyUserDict = {"name": "Carlos", "age": 15, "invalid_key": {}}
invalid_user_dict_3: MyUserDict = {"name": "Carlos", "age": 15.6}

# Now there is actually a way for specifying fields that can be omit and as in type script but it's
# kind of hacky, this consists in using a base class set to `total=False` and putting the omittable
# fields then create your typed dict and make it to inherent from this base class.


class _OmittablePersonFields(TypedDict, total=False):
    # mypy does not fully support recursive type so this will likely fail
    # https://github.com/python/mypy/issues/731
    friends: list["PersonDict"]  # type: ignore
    school: str
    age: str


class PersonDict(_OmittablePersonFields):
    name: str
    last_name: str
    height: float


# let's test
valid_person_dict: PersonDict = {"name": "Charles", "last_name": "Xavier", "height": 1.75}

# it worked

valid_person_dict_2: PersonDict = {"name": "Charles", "last_name": "Xavier", "height": 1.75, "friends": [1, 23]}