from bank import value

def main():
    test_value()


def test_value():
    assert value ("hello, how are you?") == (0)
    assert value ("HELLO") == (0)
    assert value ("hi") == (20)
    assert value ("ow are you?") == (100)

if __name__ == "__main__":
    main()


        #if AssertionError:
        #return 1
    #else:
     #   return 0
