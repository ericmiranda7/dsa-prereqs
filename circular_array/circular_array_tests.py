import circular_array
import unittest

class CircularArrayTests(unittest.TestCase):

    def setUp(self) -> None:
        self.ca = circular_array.CircularArray(10)

    def test_insert_one_item(self):
        self.ca.insert(1)
        self.assertEqual(self.ca.size, 1)

    def test_insert_two_items(self):
        self.ca.insert(1)
        self.ca.insert(2)

        self.assertEqual(self.ca.size, 2)
        self.assertEqual(self.ca.peek_head(), 2)
        self.assertEqual(self.ca.peek_tail(), 1)

    def test_append_one_item(self):
        self.ca.append(1)
        self.assertEqual(self.ca.size, 1)

    def test_append_two_items(self):
        self.ca.append(1)
        self.ca.append(2)

        self.assertEqual(self.ca.size, 2)
        self.assertEqual(self.ca.peek_tail(), 2)
        self.assertEqual(self.ca.peek_head(), 1)


    def test_insert_adds_item_at_beginning(self):
        self.ca.insert(1)
        self.ca.insert(2)

        self.assertEqual(self.ca.peek_head(), 2)
        self.assertEqual(self.ca.peek_tail(), 1)

    def test_append_adds_item_at_end(self):
        self.ca.append(1)
        self.ca.append(2)

        self.assertEqual(self.ca.peek_head(), 1)
        self.assertEqual(self.ca.peek_tail(), 2)

    def test_resizing_array(self):
        for i in range(15):
            self.ca.insert(i)

        self.assertEqual(self.size, 15)

    def test_peek_head(self):
        self.ca.insert(1)

        self.assertEqual(self.ca.peek_head(), 1)

    def test_peek_tail(self):
        self.ca.insert(1)

        self.assertEqual(self.ca.peek_tail(), 1)

    def test_random_append_inserts(self):
        self.ca.insert(1)
        self.ca.insert(0) # 0 1
        self.ca.insert(3) # 3 0 1
        self.ca.append(8) # 3 0 1 8
        self.ca.insert(4) # 4 3 0 1 8
        self.ca.append(7) # 4 3 0 1 8 7
        self.ca.append(69) # 4 3 0 1 8 7 69

        self.assertEqual(self.ca.print_items(), "4 3 0 1 8 7 69")

    def test_print_items(self):
        self.ca.insert(1)
        self.ca.append(2)
        self.ca.append(3)

        self.assertEqual(self.ca.print_items(), "1 2 3")


if __name__ == '__main__':
    unittest.main()
    
    