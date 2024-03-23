    suite = unittest.TestSuite()
    suite.addTest(CircularArrayTests("test_resizing_array"))
    runner = unittest.TextTestRunner()
    runner.run(suite)