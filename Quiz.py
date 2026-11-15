import random
import time

def direct_access(scores, index):
    """
    O(1) - Constant Time
    Retrieves a score directly using its list index.
    """
    operations = 1
    if 0 <= index < len(scores):
        return scores[index], operations
    return None, operations


def linear_search(scores, target_score):
    """
    O(n) - Linear Time
    Scans through the list one item at a time to find a target score.
    """
    operations = 0
    for index, score in enumerate(scores):
        operations += 1
        if score == target_score:
            return index, operations
    return -1, operations


def find_duplicate_pairs(scores):
    """
    O(n^2) - Quadratic Time
    Compares every score against every other score to find matching pairs.
    """
    operations = 0
    pairs = []
    n = len(scores)
    
    for i in range(n):
        for j in range(i + 1, n):
            operations += 1
            if scores[i] == scores[j]:
                pairs.append((i, j, scores[i]))
                
    return pairs, operations


def run_benchmark(dataset_size):
    print(f"\n--- Benchmarking with {dataset_size} Quiz Scores ---")
    # Generate random quiz scores between 0 and 1000
    scores = [random.randint(0, 1000) for _ in range(dataset_size)]
    
    # 1. Direct Access (Constant Time)
    start = time.perf_counter()
    _, ops_direct = direct_access(scores, dataset_size // 2)
    time_direct = (time.perf_counter() - start) * 1000
    print(f"Direct Access    | Operations: {ops_direct:<10} | Time: {time_direct:.5f} ms")

    # 2. Linear Search - Worst Case (Searching for a score not in the list)
    start = time.perf_counter()
    _, ops_linear = linear_search(scores, -1)
    time_linear = (time.perf_counter() - start) * 1000
    print(f"Linear Search    | Operations: {ops_linear:<10} | Time: {time_linear:.5f} ms")

    # 3. Pair Comparison (Quadratic Time)
    start = time.perf_counter()
    _, ops_pairs = find_duplicate_pairs(scores)
    time_pairs = (time.perf_counter() - start) * 1000
    print(f"Pair Comparison  | Operations: {ops_pairs:<10} | Time: {time_pairs:.5f} ms")


if __name__ == "__main__":
    # Test scaling across three input sizes
    for size in [5, 10, 50]:
        run_benchmark(size)
