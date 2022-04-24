import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))


# @dataclass(frozen=False) # frozen is default False so it's not needed to write it
# kw_only is default False, if it's True, you are obliged to use keyword arguments and not only their values
# kw_only=False is the default value and it's no need to write it inside @dataclass(kw_only=False)
@dataclass()
# @dataclass(frozen=True) #frozen = True means that the class is immutable and it's usefull to create constants
class Person:
    name: str
    address: str
    active: bool = True
    email_adresses: list[str] = field(default_factory=list)
    id: str = field(default_factory=generate_id)
    _search_string: str = field(init=False)
    # _search_string: str = field(init=False,repr=False) # repr=False: repr() will not show this field

    # id: str = field(init=False,default_factory=generate_id) #init=False impede
    # mencionar o id no construtor

    def __post_init__(self) -> None: # here we initialize the search_string
        self._search_string = f'{self.name} {self.address}'


def main() -> None:
    person = Person(name='John', address='123 Main St', id='123')
    # person = Person('John', '123 Main St','123') #this is not allowed when kw_only=True
    # person.name='Paulo'  # frozen=True don't allow this
    # under the hood on the clas there is a dict so you can use it
    # print(person.__dict__['name'])

    print(person)


if __name__ == '__main__':
    main()
