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


class SelfRaw(BaseField):
    """for types that already represent and initialize their state completely
    with repr -- simply wraps repr with the required raw property"""
    def raw(self):
        return repr(self)

        
#class Boolean(SelfRaw, bool): pass # lol nope
class Integer(SelfRaw, int): pass # DANGER: watch for overflows...
class Float(SelfRaw, float): pass
class Complex(SelfRaw, complex): pass # !!! will this one work?
class String(SelfRaw, str): pass # nooooooo repr adds quotes
#class Unicode(SelfRaw, UnicodeType): pass # !!! will this one work?
class Tuple(SelfRaw, tuple): pass
class List(SelfRaw, list): pass
class Dictionary(SelfRaw, dict): pass

class String(object):
    """docstring for String"""
    def __init__(self, arg):
        super(String, self).__init__()
        self.arg = arg



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
