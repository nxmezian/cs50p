#tests fuel.py
from fuel import convert, gauge

import pytest


def main():
    test_convert()


def test_convert():
    assert convert("1/4") == 25

    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("cat/dog")

    with pytest.raises(ZeroDivisionError):
        convert("10/0")

def test_gauge():
    assert gauge(25) == ("25%")
    assert gauge(99) == ("F")
    assert gauge(1) == ("E")


if __name__ == "__main__":
    main()