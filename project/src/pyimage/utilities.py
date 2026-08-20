"""Utility functions used by the pyimage package."""

__all__ = ["clamp_u8"]


def clamp_u8(value: int) -> int:
    """Clamp an integer to the unsigned 8-bit range.

    Parameters
    ----------
    value:
        Integer value to clamp.

    Returns
    -------
    int
        The value constrained to the range 0 to 255.

    Raises
    ------
    TypeError
        If ``value`` is not an integer.

    Examples
    --------
    >>> clamp_u8(-20)
    0
    >>> clamp_u8(100)
    100
    >>> clamp_u8(300)
    255
    """
    if not isinstance(value, int):
        raise TypeError("value must be an integer")

    if value < 0:
        return 0

    if value > 255:
        return 255

    return value
