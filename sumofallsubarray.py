def subarraySum(arr):
    n = len(arr)                    # length of the array
    total_sum = 0                   # final result
    for i in range(n):             # iterate over each index
        # each element's contribution is its value times the number of ways
        # to choose a start (i+1) and an end (n-i)
        contribution = arr[i] * (i + 1) * (n - i)
        total_sum += contribution  # accumulate result
    return total_sum               # return total
