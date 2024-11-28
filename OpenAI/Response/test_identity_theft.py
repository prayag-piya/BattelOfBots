import unittest
import time

def min_time_to_prevent_lockdown(farm_ids):
    def add_unique_suffix(farm_ids):
        farm_ids.sort()
        total_time = 0
        for i in range(1, len(farm_ids)):
            if farm_ids[i].startswith(farm_ids[i-1]):
                prefix_length = len(farm_ids[i-1])
                while farm_ids[i].startswith(farm_ids[i-1]):
                    farm_ids[i] += '0'
                    total_time += 1
            else:
                farm_ids[i] += '0'
                total_time += 1
        return total_time

    return add_unique_suffix(farm_ids)

class TestFarmID(unittest.TestCase):
    def test_sample_cases(self):
        self.assertEqual(min_time_to_prevent_lockdown(['1', '1', '1']), 5)
        self.assertEqual(min_time_to_prevent_lockdown(['1', '11', '111']), 2)
        self.assertEqual(min_time_to_prevent_lockdown(['1', '1', '11']), 4)
        self.assertEqual(min_time_to_prevent_lockdown(['0', '01', '0011', '010', '01']), 6)
        self.assertEqual(min_time_to_prevent_lockdown([
            '0', '1', '1', '0', '1', '0', '1', '1', '1', '1', '1', '0', '0', '1'
        ]), 41)

def benchmark():
    farm_ids = ['0', '1'] * 50  # 100 farm IDs for benchmarking
    start = time.time()
    min_time_to_prevent_lockdown(farm_ids)
    end = time.time()
    print(f"Benchmark completed in {end - start:.6f} seconds.")

if __name__ == "__main__":
    unittest.main()
    #benchmark()