Hertz Documentation
=====================
``pip install hertz``

`hertz` provides a convenient and standard way to represent frequency values.
The :py:class:`hertz.Frequency` class is a subclass of :py:class:`float`,
which means that you can use its instances just like regular numbers, but they have some additional features.
If no units are specified, MHz is assumed.
Example usage::

    from hertz import *

    foo = kHz(4)
    foo += 1.2
    print(foo) # prints 1.204 because if units aren't specified everything is done in MHz
    print(foo.in_hz) # prints 1204000.0
    foo += GHz('3')
    print(foo.in_ghz) # prints 3.001204

:py:func:`hertz.Hz`, :py:func:`hertz.kHz`, :py:func:`hertz.MHz`, :py:func:`hertz.GHz`, and :py:func:`hertz.THz`
are convenience functions to simplify creation of :py:class:`Frequency` values.
They're just partials of the constructor.
for example, ``Hz(5)`` is shorthand for ``Frequency(5, 'Hz')``.
:py:class:`kHz` and :py:class:`KHz` are both acceptable.

.. autoclass:: hertz.Frequency
    :members: __init__, __new__, in_hz, in_khz, in_mhz, in_ghz