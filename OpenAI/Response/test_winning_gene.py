import unittest
import time
from collections import defaultdict

def count_candidates(N, S):
    result = [0] * (N + 1)

    for K in range(1, N + 1):
        for L in range(1, K + 1):
            P = set()
            for i in range(N - K + 1):
                k_mer = S[i:i+K]
                min_sub = min(k_mer[j:j+L] for j in range(K - L + 1))
                for j in range(K - L + 1):
                    if k_mer[j:j+L] == min_sub:
                        P.add(i + j)
                        break
            result[len(P)] += 1

    return result[1:]

class TestWinningGene(unittest.TestCase):
    def test_sample_cases(self):
        self.assertEqual(count_candidates(8, "AGTCAACG"), [11, 10, 5, 4, 2, 2, 1, 1])

    def test_case_1(self):
        self.assertEqual(count_candidates(3, "AAA"), [3, 2, 1])

    def test_case_2(self):
        self.assertEqual(count_candidates(5, "ABCDE"), [15, 14, 12, 9, 6])


def benchmark():
    N = 200
    S = "A" * N
    start = time.time()
    count_candidates(N, S)
    end = time.time()
    print(f"Benchmark completed in {end - start:.6f} seconds.")

if __name__ == "__main__":
    #unittest.main()
    benchmark()
