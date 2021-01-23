import random
class RandomQueue:

    def __init__(self):
        self.items = []
        self.count = 0

    def insert(self, item):
        self.items.append(item)
        self.count += 1

    def remove(self):   # zwraca losowy element
        x = random.randrange(0,len(self.items))
        temp = self.items[self.count-1]
        self.items[self.count-1] = self.items[x]
        self.items[x] = temp
        self.count -= 1
        return self.items.pop()
        
    def is_empty(self):
        return not self.items

    def is_full(self):
        return False

    def clear(self):      # czyszczenie listy
        for i in range(len(self.items)):
            self.remove()


import unittest

class TestRandomQueueMethods(unittest.TestCase):

    def test_insert(self):
        aqueue = RandomQueue()
        aqueue.insert(2)
        self.assertEqual(aqueue.items, [2])

    def test_remove(self):
        aqueue = RandomQueue()
        for i in range(3):
            aqueue.insert(i)
        x = len(aqueue.items)
        aqueue.remove()
        self.assertEqual(len(aqueue.items), x-1)

    def test_is_empty(self):
        aqueue = RandomQueue()
        self.assertTrue(aqueue.is_empty())

    def test_is_full(self):
        aqueue = RandomQueue()
        self.assertFalse(aqueue.is_full())

    def test_clear(self):
        aqueue = RandomQueue()
        for i in range(3):
            aqueue.insert(i)
        aqueue.clear()
        self.assertEqual(len(aqueue.items), 0)
        
if __name__ == '__main__':
    unittest.main()

