
Introduction
============

kale!


Contexts
--------

heirarchcal (with inheritance and all that). a kind of description of a type.


Fields
------

information and functionality that can be attached to contexts

fields are kind of like data types you might set in an SQL schema. but they are
much more than that. a field is a python class, and more than that, a field can
be *any* python class, but it should conform to certain conventions for sanity's
sake.

you can add any new field you'd like to work with kale. field only need to:

# have a `raw` property (hint: use the `@property` decortor) which describes
  its state as an object which can be encoded to json.
# be initialized by providing it an object of that `raw` format.

How you structure the raw format is up to you. Go nuts! Stick versioning right
into your field, why not?


Cobs ... Things (rename me)
---------------------------

instances of a given point in a context. instances can exist at the intersection
of contexts, and inherit both contexts' fields. n stuf

