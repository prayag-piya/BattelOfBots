import unittest
from ActivatingRobot import activating_robot
from timeit import timeit


class TestActivatingRobot(unittest.TestCase):
    def test_case1(self):
        result = activating_robot(10, 2, 3, 1, [1, 2, 3, 4, 5])
        self.assertEqual(result, 3)

    def test_case2(self):
        result = activating_robot(5, 1, 1, 2, [1, 2, 3, 4, 5])
        self.assertEqual(result, 2)

    def test_case3(self):
        result = activating_robot(15, 5, 3, 3, [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(result, 9)

if __name__ == "__main__":
    print("ActivatingRobot Benchmark:")
    print(timeit(lambda: activating_robot(100000, 1000, 50000, 100, list(range(100000))), number=10))
    print()
    unittest.main()
    print()