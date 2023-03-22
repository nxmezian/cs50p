#calculates how many cookies there are in the jar

#jar class definition
class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0
        if capacity < 0:
            print("Cannot have fewer than 0 cookies")
            raise ValueError(1)

#jar contains 🍪s
    def __str__(self):
        return self.size * ("🍪")
#add n * 🍪
    def deposit(self, n):
        if n > jar.capacity:
            print("Jar cannot contain more than 12 cookies")
            raise ValueError
        else:
            self._size = self.size + n

#take n * 🍪
    def withdraw(self, n):
        if self._size < n:
            print("Jar cannot contain fewer than 0 cookies!")
            raise ValueError
        else:
            self._size = self._size - n
#setters for capacity and size
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

#main program, change the contents of the jar
jar = Jar()
jar.deposit(2)
jar.withdraw(1)
print(jar)