"""
Problem: http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/
"""
def longest_increasing_subsequence(nums):
    # array used to store the length of the longest subsequence found
    cache = [1] * len(nums)

    # array used to store the location of the predecessor in the longest
    # subsequence. -1 by default
    location = [-1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                if cache[j] + 1 > cache[i]:
                    cache[i] = cache[j] + 1
                    location[i] = j

    # finding the max in the cache gives us the 
    # answer - i.e. length of the LIS
    max_value = max(cache)

    # with the answer in hand, we need to build the solution
    # using the locations stored
    solution = []
    i = cache.index(max_value)

    # we start with the max value i.e. the index of the 
    # location where the max LIS exists and then
    # keep backtracking to build up the solution
    while location[i] > -1:
        solution.append(nums[i])
        i = location[i]

    # when the loop ends, just append the starting element
    solution.append(nums[i])

    # return the length of the LIS and the solution (in reverse)
    return max_value, solution[::-1]

if __name__ == "__main__":
    assert longest_increasing_subsequence([3, 4, -1, 0, 6, 2, 3]) == (4, [-1, 0, 2, 3])
    assert longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]) == (6, [10, 22, 33, 50, 60, 80])
    assert longest_increasing_subsequence([5,0,1,2,3,4,5,6,7,8,9,10,11,12, 2, 8, 10, 3, 6, 9, 7]) == (13, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

