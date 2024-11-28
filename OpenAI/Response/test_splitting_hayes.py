import unittest
import time
from io import StringIO
import sys

def process_queries(N, haybales, queries):
    prefix_sums = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sums[i] = prefix_sums[i - 1] + haybales[i - 1]

    results = []
    for l, r, x in queries:
        bessie_hay = 0
        elsie_hay = 0
        bessie_hay += x 
        
        for i in range(l-1, r):
            if bessie_hay <= elsie_hay:
                bessie_hay += haybales[i]
            else:
                elsie_hay += haybales[i]
        
        final_difference = bessie_hay - elsie_hay
        results.append(final_difference)

    return results

class TestHaybales(unittest.TestCase):

    def test_case_1(self):
        N = 2
        haybales = [3, 1]
        queries = [
            (1, 1, -2),
            (1, 1, -1),
            (1, 1, 0),
            (1, 1, 1),
            (1, 1, 2),
            (1, 2, -2),
            (1, 2, -1),
            (1, 2, 0),
            (1, 2, 1),
            (1, 2, 2),
            (2, 2, -2),
            (2, 2, -1),
            (2, 2, 0),
            (2, 2, 1),
            (2, 2, 2)
        ]
        expected_result = [1, 2, 3, -2, -1, 0, 1, 2, -1, 0, -1, 0, 1, 0, 1]
        self.assertEqual(process_queries(N, haybales, queries), expected_result)

    def test_case_2(self):
        N = 5
        haybales = [4, 4, 3, 1, 1]
        queries = [
            (1, 1, 20),
            (1, 2, 20),
            (1, 5, 20),
            (1, 1, 0),
            (1, 5, 0),
            (1, 4, 0),
            (3, 5, 2)
        ]
        expected_result = [16, 12, 7, 4, 1, 2, 1]
        self.assertEqual(process_queries(N, haybales, queries), expected_result)

    def test_case_3(self):
        N = 3
        haybales = [10, 5, 2]
        queries = [
            (1, 1, 0),
            (1, 2, 0),
            (1, 3, 0),
            (2, 2, 0),
            (2, 3, 0),
            (1, 2, 5)
        ]
        expected_result = [10, 15, 17, 5, 7, 15]
        self.assertEqual(process_queries(N, haybales, queries), expected_result)

def benchmark():
    N = 200000
    haybales = [i for i in range(N, 0, -1)]
    queries = [(1, N, 0)] * 1000
    start_time = time.time()
    process_queries(N, haybales, queries)
    end_time = time.time()
    print(f"Benchmark Time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    benchmark()
    unittest.main()
