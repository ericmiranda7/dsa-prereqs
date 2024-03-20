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

if __name__ == '__main__':
    unittest.main()