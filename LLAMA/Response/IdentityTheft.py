
def identity_theft(n, inputs):
    """
    Calculates the minimal unique length prefix for each input string.
    
    Parameters:
    n (int): Number of input strings.
    inputs (list): List of input strings.
    
    Returns:
    int: The minimal length of a unique prefix across the strings.
    """
    max_len = max(len(a) for a in inputs) - 1
    ans = max_len
    for i in range(1, n):
        a = inputs[i]
        for j in range(len(a), -1, -1):
            prefix = a[:j]
            for k in range(i):
                if prefix == inputs[k]:
                    break
            else:
                ans = min(ans, j)
    return ans
