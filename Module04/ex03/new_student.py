import random
import string
from dataclasses import dataclass, field

# field is a function from dataclass modules used to customize the behaviour
# of fields
def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    name: str
    surname: str
    active: bool = True

    id: str = field(init=False, default=generate_id())
    login: str = field(init=False) 

    # id and login fields must not be included as a parameter to the __init__ method
    # meaning it will not be set during object initialization via constructor

    def __post_init__(self):
        # login field is initialized
        self.login = self.name[0] + self.surname