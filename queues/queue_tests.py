import queue
import unittest

class QueueTests(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = queue.Queue()

    def test_add_item(self):
        self.queue.enqueue(3)

        self.assertEqual(self.queue.size, 1)

    def test_remove_item(self):
        self.queue.enqueue(4)
        self.queue.enqueue(5)

        self.assertEqual(self.queue.dequeue, 4)
        self.assertEqual(self.queue.size, 1)

    def test_remove_when_empty(self):
        self.queue.dequeue()

        self.assertRaises(ValueError)

    def test_add_15_items(self):
        for i in range(15):
            self.queue.enqueue(i)

        self.assertEqual(self.queue.size, 15)
        self.assertEqual(self.queue.peek, 0)

    def test_random_enq_deq(self):
        for i in range(15):
            self.queue.enqueue(i)

        first_deq = self.queue.dequeue()
        self.queue.enqueue(3)
        self.queue.enqueue(4)

        second_deq = self.queue.dequeue()

        self.assertEqual(first_deq, 0)
        self.assertEqual(second_deq, 1)
        self.assertEqual(self.queue.size, 15)

if __name__ == '__main__':
    unittest.main()