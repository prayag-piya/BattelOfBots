import unittest
import time

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def calculate_cow_distances(N, P, posts, cows):
    total_length = [0] * P
    for i in range(P):
        j = (i + 1) % P
        total_length[i] = manhattan_distance(posts[i], posts[j])
    
    prefix_sum = [0] * P
    prefix_sum[0] = total_length[0]
    for i in range(1, P):
        prefix_sum[i] = prefix_sum[i-1] + total_length[i]
    
    def shortest_walk(x1, y1, x2, y2):
        start_idx = None
        end_idx = None
        for i in range(P):
            if posts[i] == (x1, y1):
                start_idx = i
            if posts[i] == (x2, y2):
                end_idx = i
        if start_idx is None or end_idx is None:
            return -1
        
        if start_idx <= end_idx:
            clockwise = prefix_sum[end_idx] - (prefix_sum[start_idx-1] if start_idx > 0 else 0)
        else:
            clockwise = (prefix_sum[P-1] - (prefix_sum[start_idx-1] if start_idx > 0 else 0)) + prefix_sum[end_idx]
        
        counterclockwise = prefix_sum[P-1] - clockwise
        return min(clockwise, counterclockwise)

    result = []
    for cow in cows:
        x1, y1, x2, y2 = cow
        result.append(shortest_walk(x1, y1, x2, y2))
    
    return result

class TestCowWalks(unittest.TestCase):
    def test_example_case(self):
        N = 5
        P = 4
        posts = [(0, 0), (2, 0), (2, 2), (0, 2)]
        cows = [
            (0, 0, 0, 2),
            (0, 2, 1, 0),
            (2, 1, 0, 2),
            (1, 0, 1, 2),
            (1, 2, 1, 0)
        ]
        expected = [2, 3, 3, 4, 4]
        self.assertEqual(calculate_cow_distances(N, P, posts, cows), expected)

def benchmark():
    N = 1000
    P = 100
    posts = [(i, 0) for i in range(P)]
    cows = [(i, 0, (i+1) % P, 0) for i in range(N)]
    
    start = time.time()
    calculate_cow_distances(N, P, posts, cows)
    end = time.time()
    
    print(f"Benchmark completed in {end - start:.6f} seconds.")

if __name__ == "__main__":
    benchmark()
    unittest.main()
