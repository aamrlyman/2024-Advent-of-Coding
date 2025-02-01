import pytest
from day_2 import *

test_list1 = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]

test_list2 = [
    [0, 8, 7, 6, 5],
    [8, 0, 7, 6, 5],
    [8, 7, 0, 6, 5],
    [8, 7, 6, 0, 5],
    [8, 7, 6, 5, 0],
    [1, 8, 9, 10, 11],
    [8, 1, 9, 10, 11],
    [8, 9, 1, 10, 11],
    [8, 9, 10, 1, 11],
    [8, 9, 10, 11, 1],
]


@pytest.mark.parametrize(
    "sublist, expected",
    [
        (test_list1, 2),
        #   (get_input(), 379),
        (test_list2, 0),
    ],
)
def test_get_safe_count(sublist, expected):
    assert get_safe_count(sublist) == expected


@pytest.mark.parametrize(
    "sublist, expected",
    [
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], True),
        ([8, 6, 4, 4, 1], True),
        ([1, 3, 6, 7, 9], True),
        ([], True),
    ],
)
def test_is_stepping_by_3_with_recursion(sublist, expected):
    print(sublist, expected)
    assert is_stepping_by_3_with_recursion(sublist, 1) == expected


@pytest.mark.parametrize("sublist, expected", [(test_list1, 4), (test_list2, 10)])
def test_get_safe_count_with_retries(sublist, expected):
    assert get_safe_count(sublist, 1) == expected
