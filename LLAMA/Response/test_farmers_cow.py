import unittest
from FarmersCow import farmers_cow_main
from timeit import timeit

class TestFarmersCow(unittest.TestCase):
    def test_case1(self):
        result = farmers_cow_main(2, 1, [(0, 0), (10, 0)], [(0, 5, 10, 5)])
        self.assertEqual(result, [5.0])

    def test_case2(self):
        result = farmers_cow_main(3, 2, [(0, 0), (5, 5), (10, 0)], [(0, 5, 5, 10), (5, 5, 10, 0)])
        self.assertEqual(result, [5.0, 5.0])

if __name__ == "__main__":
    print("FarmersCow Benchmark:")

    large_polygon = [(i, i) for i in range(1000)]
    large_lines = [(i, i+1, i+2, i+3) for i in range(999)]
    print(timeit(lambda: farmers_cow_main(1000, 100, large_polygon, large_lines), number=10))
    print()
    unittest.main()
    print()

