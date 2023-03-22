#tests jar.py
from jar import Jar

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()

def test_init():
    jar =Jar()
    assert jar.capacity == 12

def test_str():
    jar =Jar()
    jar.deposit(5)
    assert str(jar) == ("🍪🍪🍪🍪🍪")
    jar.deposit(1)
    assert str(jar) == ("🍪🍪🍪🍪🍪🍪")
    jar.deposit(6)
    assert str(jar) == ("🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪")


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(6)
    assert jar.size == 7
    jar.deposit(5)
    assert jar.size == 12


def test_withdraw():
    jar = Jar()
    jar.withdraw(0)
    assert jar.size == 0


if __name__ == "__main__":
    main()



