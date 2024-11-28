import unittest
from winningGene import process_dna
import timeit

class TestProcessDNA(unittest.TestCase):
    
    def test_case1(self):
        N = 4
        S = "ATCG"
        result = process_dna(N, S)
        self.assertEqual(result, [4, 6, 4, 1])  # Based on the logic for input "ATCG"
    
    def test_case2(self):
        N = 5
        S = "AAAAA"
        result = process_dna(N, S)
        self.assertEqual(result, [1, 1, 1, 1, 1])  # Expected results for repetitive string "AAAAA"
    
    def test_case3(self):
        N = 6
        S = "GATTAC"
        result = process_dna(N, S)
        self.assertEqual(result, [4, 10, 15, 20, 15, 1])  # Unique subsequences for "GATTAC"
    
    def test_edge_case(self):
        N = 1
        S = "A"
        result = process_dna(N, S)
        self.assertEqual(result, [1])  # Single character edge case

if __name__ == "__main__":
    print("WinningGene Benchmark:")
    N = 200
    S = "ATCG" * 250 
    print(timeit.timeit(lambda: process_dna(N, S), number=10))
    print()
    unittest.main()
    print()
