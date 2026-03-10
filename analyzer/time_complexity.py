def estimate_time_complexity(depth):

    if depth == 0:
        return "O(1)"

    elif depth == 1:
        return "O(n)"

    elif depth == 2:
        return "O(n^2)"

    elif depth == 3:
        return "O(n^3)"

    else:
        return "O(n^k)"
