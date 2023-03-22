#tests numb3rs

from numb3rs import validate

def main():
    test_positive()
    test_negative()

#tests postive input
def test_positive():
    assert validate("266.266.266.266") == False
    assert validate("10000000") == False
    assert validate("01.300.243.300") == False
    assert validate("0") == False
    assert validate("22.01.150.200") == True

#tests postive input
def test_negative():
    assert validate("-1") == False
    assert validate("-256.232.01.02") == False



if __name__ == "__main__":
    main()