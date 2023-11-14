import pickle
import math

from pytest import raises

from hertz import *


def test_advertisement():
    foo = kHz(4)
    foo += 1.2
    assert foo == 1.204
    assert foo.in_hz == 1204000.0
    foo += GHz('3')
    assert foo.in_ghz == 3.001204


def test_pickle():
    val = kHz(20)
    pickled_bytes = pickle.dumps(val)
    pickled_val = pickle.loads(pickled_bytes)

    assert val == pickled_val


def test_math():
    assert kHz(123) + 4 == 4.123
    assert THz(3) - Hz(0.1) < THz(3)
    assert MHz(5.2) == 5.2
    assert 10.1 == MHz(10.1)
    assert .5 == kHz(500)
    assert .7 + GHz(.5) == 500.7
    assert GHz(7).in_ghz == 7
    assert (Hz(1) * Hz(4)).in_hz == Hz(4)
    assert (GHz(1) / 2).in_khz == 5e5
    assert (MHz(1) * 2).in_hz == 2e6


def test_weird_math():
    assert math.ceil(MHz(1.2)).in_hz == 2e6
    assert math.floor(KHz(5)).in_hz == 0
    assert (MHz(3) % 2).in_mhz == 1
    assert (MHz(3) // 2).in_khz == 1e3
    assert (MHz(5) ** 2).in_mhz == 25
    assert -MHz(2) == -2


def test_invalid():
    with raises(ValueError):
        Frequency(1, 'jHz')

    with raises(Exception):
        Frequency(1, None)

    with raises(TypeError):
        Frequency(None)

    with raises(ValueError):
        Frequency('eeby deeby')


def test_str():
    assert str(MHz(1)) == '1.00 MHz'
    assert str(GHz(1e-3)) == '1.00 MHz'
    assert str(Hz(10002)) == '10.00 KHz'
    assert str(Hz(10009)) == '10.01 KHz'
    assert str(Hz(.03)) == '3.000e-02 Hz'
    assert str(GHz(1e9)) == '1000000.00 THz'
