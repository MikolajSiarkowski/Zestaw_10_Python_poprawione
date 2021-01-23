class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None] 
        self.head = 0           # pierwszy do pobrania 
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise Exception('Queue is full!')
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise Exception('Queue is empty!')
        data = self.items[self.head]
        self.items[self.head] = None      # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data


import unittest

class TestQueueMethods(unittest.TestCase):

    def test_push(self):
        aqueue = Queue()
        with self.assertRaises(Exception):
            for i in range(11):
                aqueue.put(i)

    def test_pop(self):
        aqueue = Queue()
        with self.assertRaises(Exception):
            aqueue.get()

    
if __name__ == '__main__':
    unittest.main()

