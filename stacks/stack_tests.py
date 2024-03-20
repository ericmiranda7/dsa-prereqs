import stack
import unittest

class StackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = stack.Stack()

    def test_add(self):
        original = 2
        self.stack.push(original)
        result = self.stack.peek()
        self.assertEqual(original, result)

    def test_remove(self):
        original = 2
        self.stack.push(original)
        result = self.stack.pop()

        self.assertEqual(original, result)
        self.assertEqual(self.stack.size, 0)

    def test_peek_does_not_remove(self):
        original = 2
        self.stack.push(original)
        self.stack.peek()

        self.assertEqual(self.stack.size, 1)

    def test_add_fifteen_items(self):
        for i in range(15):
            self.stack.push(i)

        self.assertEqual(self.stack.size, 15)

    def test_peek_with_15_items(self):
        for i in range(15):
            self.stack.push(i)

        self.assertEqual(self.stack.peek(), 14)

    def test_random_push_pops(self):
        for i in range(5):
            self.stack.push(i)
            
        first_pop = self.stack.pop()
        self.stack.push(3)
        self.stack.push(4)
        second_pop = self.stack.pop()
        third_pop = self.stack.pop()
        self.stack.push(67)

        self.assertEqual(first_pop, 4)
        self.assertEqual(second_pop, 4)
        self.assertEqual(third_pop, 3)
        self.assertEqual(self.stack.peek(), 67)
        self.assertEqual(self.stack.size, 5)
        
if __name__ == '__main__':
    unittest.main()