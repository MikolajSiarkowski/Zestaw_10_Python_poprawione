class Stack:

    def __init__(self, size = 10):
        self.items = size*[None]
        self.size = size
        self.count = 0

    def __str__(self):                  # podglądamy stos
        return str(self.items)

    def is_empty(self):
        return self.count == 0

    def is_full(self):                  # nigdy nie jest pełny
        return self.count==self.size

    def push(self, item):
        if self.is_full():
            raise Exception('The stack is full!')
        self.items[self.count] = item         # dodajemy na koniec
        self.count+=1
            
    def pop(self):                      # zwraca element
        if self.is_empty():
            raise Exception('The stack is empty!')
        else:
            self.count -=1
            pop = self.items[self.count]
            self.items[self.count] = None
            return pop         # zabieram od końca


import unittest

class TestStackMethods(unittest.TestCase):

    def test_push(self):
        astack = Stack()
        with self.assertRaises(Exception):
            for i in range(11):
                astack.push(i)

    def test_pop(self):
        astack = Stack()
        with self.assertRaises(Exception):
            astack.pop()

    
if __name__ == '__main__':
    unittest.main()




