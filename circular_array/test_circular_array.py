def test_list_items():
    # Test case 1: Empty circular array
    arr = CircularArray(5)
    assert arr.list_items() == []

    # Test case 2: Circular array with one item
    arr = CircularArray(5)
    arr.enqueue(10)
    assert arr.list_items() == [10]

    # Test case 3: Circular array with multiple items
    arr = CircularArray(5)
    arr.enqueue(10)
    arr.enqueue(20)
    arr.enqueue(30)
    assert arr.list_items() == [10, 20, 30]

    # Test case 4: Circular array with capacity reached
    arr = CircularArray(3)
    arr.enqueue(10)
    arr.enqueue(20)
    arr.enqueue(30)
    assert arr.list_items() == [10, 20, 30]

    # Test case 5: Circular array with wrap-around
    arr = CircularArray(5)
    arr.enqueue(10)
    arr.enqueue(20)
    arr.enqueue(30)
    arr.dequeue()
    arr.enqueue(40)
    arr.enqueue(50)
    assert arr.list_items() == [20, 30, 40, 50]

    print("All test cases passed!")

test_list_items()