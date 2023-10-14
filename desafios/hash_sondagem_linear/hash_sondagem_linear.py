
class Vector:

    def __init__(self, capacity=10):
        self._size = 0
        self._capacity = capacity
        self._data = []
        self._create_data(-2)

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity

    def empty(self):
        return self._size == 0

    def data(self):
        return self._data

    def at(self, index):
        return self.data()[index % self.capacity()]

    def _create_data(self, value):
        for i in range(self._capacity):
            self._data.append(value)
        self._size = self._capacity


class HashTable(Vector):

    def __init__(self, capacity=10):
        super().__init__(capacity)

    def __hash__(self, str) -> int:
        return len(str) % self.capacity()

    def insert(self, key):
        index = self.__hash__(key)
        if self.at(index) == -2:
            self.data()[index] = key
        else:
            while self.at(index) != -2:
                index += 1
            self.data()[index % self.capacity()] = key

    def remove(self, key):
        index = self.__hash__(key)
        if self.at(index) == key:
            self.data()[index] = -2
        else:
            while self.at(index) != key:
                index += 1
            self.data()[index % self.capacity()] = -2

    def print(self):
        for i in range(self.size()):
            print(self.at(i))


size = int(input())
hashtable = HashTable(size)
action = int(input())

while action != -1:

    if action == 0:
        key = input()
        hashtable.insert(key)
    elif action == 1:
        key = input()
        hashtable.remove(key)

    action = int(input())

hashtable.print()

"""
10
0
Teste
0
Ideia
0
universidade
0
computacao
0
abdc
0
abc
1
abc
0
blablablabla
-1

"""
