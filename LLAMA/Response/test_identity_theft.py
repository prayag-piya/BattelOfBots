import unittest
from IdentityTheft import identity_theft
from timeit import timeit

class TestIdentityTheft(unittest.TestCase):
    def test_case1(self):
        result = identity_theft(3, ["abc", "abcd", "abcde"])
        self.assertEqual(result, 3)

    def test_case2(self):
        result = identity_theft(5, ["a", "aa", "aaa", "aaaa", "aaaaa"])
        self.assertEqual(result, 1)

    def test_case3(self):
        result = identity_theft(4, ["identity", "identityx", "id", "idx"])
        self.assertEqual(result, 2)

if __name__ == "__main__":
    print("IdentityTheft Benchmark:")
    print()
    print(timeit(lambda: identity_theft(1000, ["a" * i for i in range(1000)]), number=10))
    print()
    unittest.main()
    print()
