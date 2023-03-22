#tests twttr.py

from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten("abc") == ("bc")
    assert shorten("HELLO") ==("HLL")
    assert shorten("AAAAAaaaaaa") ==("")
    assert shorten(",abc123") ==(",bc123")

    if AssertionError:
        return 1
    else:
        return 0

if __name__ == "__main__":
    main()