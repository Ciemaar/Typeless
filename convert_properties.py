import logging
from decimal import Decimal

log = logging.getLogger(__name__)

__author__ = 'andriod'


def create_gsd_convert_Decimal(name):
    def getter(self):
        return self.__dict__[name]

    def setter(self, value):
        self.__dict__[name] = Decimal(value)

    def deleter(self):
        del self.__dict__[name]

    return getter, setter, deleter

def enforce_Decimal(name):
    return property(*create_gsd_convert_Decimal(name))

class Booking(object):
    max_room = 100

    def __init__(self):
        self.__age = None
        self.name = ''
        self.__dict__['room'] = None

    # Getter/Setter
    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = int(age)

    age = property(get_age, set_age)

    @property
    def name(self):
        return self.__dict__['name']

    @name.setter
    def name(self, value):
        self.__dict__['name'] = str(value)

    @name.deleter
    def name(self):
        del self.__dict__['name']

    room = property(lambda self: self.__dict__['room'])

    @room.setter
    def room(self, value):
        assert 0 < value < Booking.max_room
        self.__dict__['room'] = value

    price = property(*create_gsd_convert_Decimal('price'))

    tax = enforce_Decimal('tax')


norm = Booking()
norm.set_age('23')
assert norm.get_age() == 23

norm.age = '28'
assert norm.age == 28

norm.name = "Andy"
assert norm.name == "Andy"
norm.room = 34

enforced = Booking()
enforced.name = 42
assert enforced.name == "42"
try:
    enforced.room = 100
except AssertionError as e:
    print('Got expected AssertionError')
else:
    assert False, "Missed expected assertion"

try:
    enforced.room = '100'
except TypeError as e:
    print('Got expected TypeError')
else:
    assert False, "Missed expected assertion"

price = 380.23
norm.price = price
assert isinstance(price, float)
assert not isinstance(price, Decimal)
assert isinstance(norm.price, Decimal)
assert not isinstance(norm.price, float)

tax = 73.29
norm.tax = tax
assert isinstance(tax, float)
assert not isinstance(tax, Decimal)
assert isinstance(norm.tax, Decimal)
assert not isinstance(norm.tax, float)


