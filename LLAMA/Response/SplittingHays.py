def splitting_hay(n, hay, queries):
    """
    Solves the Splitting Hay problem for given haystack weights and queries.

    Parameters:
    n (int): Number of hay weights.
    hay (list): List of integers representing hay weights.
    queries (list): List of queries, each as (l, r, x).

    Returns:
    list: List of integers representing the result for each query.
    """
    results = []
    for l, r, x in queries:
        ans = 0
        for i in range(l - 1, r):
            ans += (hay[i] if hay[i] > x else x) - (hay[i] if hay[i] > 0 else 0)
            x += hay[i] * (1 if hay[i] > x else -1) * (1 if hay[i] > 0 else -1)
        results.append(ans)
    return results
