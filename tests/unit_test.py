import pytest

import dozenal

def test_dozenal_digit_decimals():
    assert dozenal.dozenal_digit(0) == '0'
    assert dozenal.dozenal_digit(1) == '1'
    assert dozenal.dozenal_digit(2) == '2'
    assert dozenal.dozenal_digit(3) == '3'
    assert dozenal.dozenal_digit(4) == '4'
    assert dozenal.dozenal_digit(5) == '5'
    assert dozenal.dozenal_digit(6) == '6'
    assert dozenal.dozenal_digit(7) == '7'
    assert dozenal.dozenal_digit(8) == '8'
    assert dozenal.dozenal_digit(9) == '9'


def test_dozenal_digit_dek():
    assert dozenal.dozenal_digit(10) == 'ᘔ'


def test_dozenal_digit_elv():
    assert dozenal.dozenal_digit(11) == 'Ɛ'


def test_dozenal_digit_outofrange():
    with pytest.raises(ValueError):
        dozenal.dozenal_digit(12)


def test_dozenal_digit_float():
    with pytest.raises(ValueError):
        dozenal.dozenal_digit(3.0)


def test_dozenal_digit_str():
    with pytest.raises(ValueError):
        dozenal.dozenal_digit('9')


def test_iso2doz_normal():
    assert dozenal.iso2doz('2017-10-20') == '6901-9-25'


def test_iso2doz_single_digit_day():
    assert dozenal.iso2doz('2017-10-22') == '6901-ᘔ-00'
