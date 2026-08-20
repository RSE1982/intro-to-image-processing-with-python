"""Tests for pyimage.utilities."""

import pytest

from pyimage.utilities import clamp_u8


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (-100, 0),
        (-1, 0),
        (0, 0),
        (1, 1),
        (100, 100),
        (254, 254),
        (255, 255),
        (256, 255),
        (1000, 255),
    ],
)
def test_clamp_u8(value: int, expected: int) -> None:
    """Values should be constrained to the unsigned 8-bit range."""
    assert clamp_u8(value) == expected


@pytest.mark.parametrize(
    "value",
    [
        1.5,
        "100",
        None,
        [100],
        (100,),
    ],
)
def test_clamp_u8_rejects_non_integers(value: object) -> None:
    """Non-integer input should raise TypeError."""
    with pytest.raises(TypeError, match="value must be an integer"):
        clamp_u8(value)
