"""
get it? *fields*? ...

fields are initialized with a dictionary of data that defines their state
fields must provide this dictionary when asked.

f = Field({init data})
assert f.raw == {init data}
... or to be stupid,
f == Field(Field(Field(Field(f.raw).raw).raw).raw)

"""

from abc import ABCMeta, abstractmethod, abstractproperty
from types import UnicodeType

class BaseField(object):
    """inheriting from this might keep you in line."""
    __metaclass__ = ABCMeta
    @abstractmethod
    def raw(self): return # yum


class Float(BaseField, float):
    def raw(self):
        return float(self)


class Integer(BaseField, int):
    def raw(self):
        return int(self)


class Float(BaseField, float):
    def raw(self):
        return float(self)


class Complex(BaseField, complex):
    def __init__(self, state):
        super(Complex, self).__init__(state['real'], state['imag'])
    def raw(self):
        return {'real': self.real, 'imag': self.imag}


class String(BaseField, str):
    def raw(self):
        return str(self)


class Tuple(BaseField, tuple):
    def raw(self):
        """json has no notion of tuples, only lists"""
        return list(self)


class List(BaseField, list):
    def raw(self):
        return list(self)


class Dictionary(BaseField, dict):
    def raw(self):
        return dict(self)


class SimpleState(BaseField):
    """fields whose state is tracked by simple properties."""
    __metaclass__ = ABCMeta

    def __init__(self, state):
        for name, value in state.items():
            setattr(self, name, value)

    @abstractproperty
    def _state_property_names(self):
        """a list of property names on the object"""
        return ()
    
    def raw(self):
        state = dict((n, getattr(self, n)) for n in self._state_property_names)
        return state


class Periodic(SimpleState):
    """when does it happen next?"""
    _state_property_names = ('period', 'phase')

    def next(self):
        return self.last + 'blahhh'
