"""
get it? *fields*? ...

fields are initialized with a dictionary of data that defines their state
fields must provide this dictionary when asked.

f = Field({init data})
assert f.raw == {init data}
... or to be stupid,
f == Field(Field(Field(Field(f.raw).raw).raw).raw)

"""

from abc import ABCMeta, abstractproperty
from types import UnicodeType

class BaseField(object):
    """inheriting from this might keep you in line."""
    __metaclass__ = ABCMeta

    @abstractproperty
    def raw(self): return # yum


class SelfRaw(BaseField):
    """for types that already represent their state completely
    simply adds a simple raw property"""
    @property
    def raw(self):
        return repr(self)

        
"""
yes these are kind of dumb.
but it feels good to import library classes, right?
"""

#class Boolean(SelfRaw, bool): pass # lol nope
class Integer(SelfRaw, int): pass # DANGER: watch for overflows...
class Float(SelfRaw, float): pass
class Complex(SelfRaw, complex): pass # !!! will this one work?
class String(SelfRaw, str): pass # nooooooo repr adds quotes
#class Unicode(SelfRaw, UnicodeType): pass # !!! will this one work?
class Tuple(SelfRaw, tuple): pass
class List(SelfRaw, list): pass
class Dictionary(SelfRaw, dict): pass


class AttrState(BaseField):
    """For fields whose state is tracked as simple-valued attributes"""
    def __init__(self, state):
        for name, value in state.items():
            setattr(self, name, value)
        self._acceptable_types = [int, float, complex, str, tuple, list, dict]
        self._exclude_attributes = ['_acceptable_types', '_exclude_attributes']

    @property
    def raw(self):
        return dict((name, value) for name, value in self.__dict__.items()
            if type(value) in self._acceptable_types and
            name not in self._exclude_attributes)


class Periodic(AttrState):
    """when does it happen next?"""
    def next(self):
        return self.last + 'blahblah'
        
p = Periodic({'last': 'tuesday', 'abc': 'wednesday'})

print p.last
print p.raw

q = Periodic(p.raw)

print q.next()
print q.raw

if __name__ == '__main__':

    class GoodF(BaseField):
        @property
        def value(self): return 5
        @property
        def raw(self): return 'a'
    f1 = GoodF()

    class SomeF(BaseField): pass

    try:
        f2 = SomeF()
    except TypeError:
        pass
    else:
        raise Exception('you shouldn\'t be allowed')
