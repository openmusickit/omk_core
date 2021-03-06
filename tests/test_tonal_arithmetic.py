import pytest

from test_fixtures import tonal_tuples, tonal_oct_tuples
import omk_core as omk

def test_test(tonal_tuples):
    assert len(tonal_tuples) == 35

def test_tonal_sum_diff(tonal_tuples, tonal_oct_tuples):
    """Addition and subtraction are opposite operations,
    therefore x + y - y should equal x.
    """

    for x in tonal_tuples:
        for y in tonal_tuples:
            assert x == omk.tonal_diff(omk.tonal_sum(x, y), y)
            assert y == omk.tonal_sum(omk.tonal_diff(y, x), x)

    for x in tonal_oct_tuples:
        for y in tonal_oct_tuples:
            assert x == omk.tonal_diff(omk.tonal_sum(x, y), y)
            assert y == omk.tonal_sum(omk.tonal_diff(y, x), x)

def test_tonal_invert(tonal_tuples, tonal_oct_tuples):
    """An inversion is self-reversing,
    therefore tonal_invert(tonal_invert(x)) should equal x.
    """

    for x in tonal_tuples:
        assert omk.tonal_invert(omk.tonal_invert(x)) == x

        for y in tonal_tuples:
            assert omk.tonal_invert(omk.tonal_invert(x, y), y) == x

    for x in tonal_oct_tuples:
        assert omk.tonal_invert(omk.tonal_invert(x)) == x

        for y in tonal_oct_tuples:
            assert omk.tonal_invert(omk.tonal_invert(x, y), y) == x


def test_abs_diff(tonal_tuples, tonal_oct_tuples):
    for x in tonal_tuples:
        for y in tonal_tuples:
            assert omk.tonal_int(omk.tonal_abs_diff(x, y)) < 7

    for x in tonal_tuples:
        for y in tonal_tuples:
            z = omk.tonal_sum(x, y)
            a = omk.tonal_abs_diff(x, z)
            assert a == y or a == omk.tonal_invert(y)
            assert omk.tonal_int(a) < 7

    for x in tonal_oct_tuples:
        for y in tonal_oct_tuples:
            z = omk.tonal_sum(x, y)
            a = omk.tonal_abs_diff(x, z)
            assert a == y or a == omk.tonal_invert(y)

def test_nearest_instance(tonal_tuples, tonal_oct_tuples):
    for x in tonal_tuples:
        for y in tonal_tuples:
            z = omk.tonal_nearest_instance(x, y)

            assert omk.abs_int_diff(x, z) < 7

    for x in tonal_oct_tuples:
        for y in tonal_oct_tuples:
            z = omk.tonal_nearest_instance(x, y)

            assert omk.abs_int_diff(x, z) < 7

def test_abs_int_diff(tonal_tuples):
    for x in tonal_tuples:
        for y in tonal_tuples:
            z = omk.abs_int_diff(x,y)
            assert z < 7


#### Testing internal functions ####

from omk_core.tonal_algebra import tonal_arithmetic

def test_tonal_modulo(tonal_tuples):
    for x in tonal_tuples:
        for y in tonal_tuples:
            a = tonal_arithmetic._tonal_modulo((x[0]+y[0], x[1]+y[1]))
            b = omk.tonal_sum(x, y)
            assert a == b

def test_negative_tuple(tonal_tuples, tonal_oct_tuples):
    for x in tonal_tuples:
        neg_x = tonal_arithmetic._negative_tuple(x)
        assert omk.tonal_sum(x, neg_x) == (0,0)

    for x in tonal_oct_tuples:
        neg_x = tonal_arithmetic._negative_tuple(x)
        assert omk.tonal_sum(x, neg_x) == (0,0,0)