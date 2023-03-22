#tests plates.py
import string

from plates import is_valid

def main():
    test_first_digits()
    test_min_max_chars()
    test_no_nums_middle()
    test_no_periods_spaces_punctuation()


#first two digits must be letters from the alphabet
def test_first_digits():
    assert is_valid("AB") == True
    assert is_valid("ABCD12") == True
    assert is_valid("123C") == False
    assert is_valid("12") == False

    if AssertionError:
        return 1
    else:
        return 0

#plate must contain minimum of 2 and max of 6 characters
def test_min_max_chars():
    assert is_valid("AB") == True
    assert is_valid("AB1") == True
    assert is_valid("AAAAAAAAAAAAAAAAAAAAAA") == False
    assert is_valid("A") == False

    if AssertionError:
        return 1
    else:
        return 0

#plate may not contain numbers in its middle
def test_no_nums_middle():
    assert is_valid ("ABC1") == True
    assert is_valid("ABCDE1") == True
    assert is_valid("ABCD11") == True
    assert is_valid("ABC1D11") == False
    assert is_valid("AB12AB") == False

    if AssertionError:
        return 1
    else:
        return 0

def test_no_periods_spaces_punctuation():
    assert is_valid(", C1") == False
    assert is_valid(" BCDE1") == False
    assert is_valid("ABC.11") == False

    if AssertionError:
        return 1
    else:
        return 0

if __name__ == "__main__":
    main()