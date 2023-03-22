#tests working.py
from working import convert
import pytest

def main():
    test_value_error()
    test_input()
    test_hour()
    test_format()

def test_value_error():
    with pytest.raises(ValueError):
        convert("a")
    with pytest.raises(ValueError):
        convert(".")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")

def test_input():
    assert convert("9 AM to 5 PM") ==("09:00 to 17:00")
    assert convert("9:00 AM to 5:00 PM") ==("09:00 to 17:00")
    assert convert("8 PM to 8 AM") == ("20:00 to 08:00")
    assert convert("8:00 PM to 8:00 AM") ==("20:00 to 08:00")

def test_hour():
    with pytest.raises(ValueError):
        convert("15 PM to 16 AM")
    with pytest.raises(ValueError):
        convert("20 PM to 1 AM")
    with pytest.raises(ValueError):
        convert("100 PM to 1:30 AM")

def test_format():
    with pytest.raises(ValueError):
        convert("nine AM to five PM")
    with pytest.raises(ValueError):
        convert("nine thirty PM  one thirty AM")


#9:30 AM to 5:55 PM