def min_string_factor(X, Y, S, R):
    n = len(X)
    m = len(Y)
    rev_Y = Y[::-1]

    # dp[i] will hold the minimum number of substrings needed to form X[0:i]
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: 0 substrings to form empty string

    # Create a set of substrings for quick lookup
    substrings_Y = set()
    substrings_rev_Y = set()

    # Generate all substrings of Y
    for start in range(m):
        for end in range(start + 1, m + 1):
            substrings_Y.add(Y[start:end])

    # Generate all substrings of reversed Y
    for start in range(m):
        for end in range(start + 1, m + 1):
            substrings_rev_Y.add(rev_Y[start:end])

    # Fill the dp array
    for i in range(1, n + 1):
        for j in range(i):
            if X[j:i] in substrings_Y:
                dp[i] = min(dp[i], dp[j] + 1)
            if X[j:i] in substrings_rev_Y:
                dp[i] = min(dp[i], dp[j] + 1)

    # If we cannot form X
    if dp[n] == float('inf'):
        return "Impossible"

    # Calculate the minimum string factor
    min_substrings = dp[n]
    min_factor = float('inf')

    # We need to find the exact count of substrings from Y and reversed Y
    for i in range(n + 1):
        if dp[i] == min_substrings:
            count_Y = 0
            count_rev_Y = 0
            # Check how many substrings are selected from Y and rev_Y
            for j in range(i):
                if X[j:i] in substrings_Y:
                    count_Y += 1
                if X[j:i] in substrings_rev_Y:
                    count_rev_Y += 1
            min_factor = min(min_factor, count_Y * S + count_rev_Y * R)

    return min_factor

# Example usage
X = input().strip()
Y = input().strip()
S, R = map(int, input().strip().split())

result = min_string_factor(X, Y, S, R)
print(result)