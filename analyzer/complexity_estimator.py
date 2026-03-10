def estimate_complexity(depth):

    if depth == 0:
        return "O(1)"

    elif depth == 1:
        return "O(n)"

    else:
        return f"O(n^{depth})"
