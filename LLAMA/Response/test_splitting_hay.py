import unittest
from SplittingHays  import splitting_hay
import timeit

class TestSplittingHay(unittest.TestCase):
    def test_case1(self):
        n = 5
        hay = [3, 2, 1, 4, 5]
        queries = [(1, 3, 2), (2, 5, 3)]
        result = splitting_hay(n, hay, queries)
        self.assertEqual(result, [4, 10])  # Expected result based on the problem description

    def test_case2(self):
        n = 4
        hay = [1, 2, 3, 4]
        queries = [(1, 2, 0), (3, 4, 1)]
        result = splitting_hay(n, hay, queries)
        self.assertEqual(result, [2, 5])  # Expected output for this case

    def test_case3(self):
        n = 3
        hay = [5, 10, 15]
        queries = [(1, 3, 5), (1, 2, 10)]
        result = splitting_hay(n, hay, queries)
        self.assertEqual(result, [20, 15])  # Expected output based on this scenario

    def test_edge_case(self):
        n = 1
        hay = [5]
        queries = [(1, 1, 5)]
        result = splitting_hay(n, hay, queries)
        self.assertEqual(result, [0])  # Single haystack element case, edge scenario

if __name__ == "__main__":
    n = 1000
    hay = list(range(1, n + 1))
    queries = [(1, 500, 50), (500, 1000, 75), (1, 1000, 25)]

    print("SplittingHay Benchmark:")
    print(timeit.timeit(lambda: splitting_hay(n, hay, queries), number=10))
    print()
    unittest.main()
    print()