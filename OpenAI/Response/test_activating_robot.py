import time
import unittest

def minimum_time_to_place_robots(L, R, N, K, activation_points):
    activation_points.sort()
    current_position = 0
    total_time = 0
    
    for point in activation_points:

        travel_time = min((point - current_position) % L, (current_position - point) % L)
        total_time += travel_time
        current_position = point

        remaining_time = (K - travel_time % K) % K
        total_time += remaining_time
        current_position = (current_position + remaining_time) % L
    
    return total_time

class TestMinimumTimeToPlaceRobots(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual(minimum_time_to_place_robots(10, 2, 1, 2, [6]), 22)

    def test_case_2(self):
        self.assertEqual(minimum_time_to_place_robots(10, 2, 1, 2, [7]), 4)

    def test_case_3(self):
        self.assertEqual(minimum_time_to_place_robots(32, 4, 5, 2, [0, 23, 12, 5, 11]), 48)

    def test_case_4(self):
        self.assertEqual(minimum_time_to_place_robots(24, 3, 1, 2, [16]), 48)

def benchmark():
    start = time.time()
    minimum_time_to_place_robots(1000000000, 20, 1, 2, [i for i in range(1, 50)])
    end = time.time()
    print(f"Benchmark Time: {end - start} seconds")

if __name__ == "__main__":
    benchmark()
    unittest.main(argv=[''], exit=False)
