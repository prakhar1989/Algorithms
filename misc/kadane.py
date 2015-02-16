# The maximum subarray problem is the task of finding the contiguous subarray within a one-dimensional array of numbers which has the largest sum. Kadane's algorithm finds the maximum subarray sum in linear time.
# For example, in the array { -1, 3, -5, 4, 6, -1, 2, -7, 13, -3 }, the maximum subarray sum is 17 (from the highlighted subarray).

def find_max_subarray(numbers):
    max_till_here = [0]*len(numbers)
    max_value = 0
    for i in range(len(numbers)):
        max_till_here[i] = max(numbers[i], max_till_here[i-1] + numbers[i])
        max_value = max(max_value, max_till_here[i])
    return max_value

# another version
def find_max_subarray2(numbers):
    max_till_here = [numbers[0]]
    for n in numbers[1:]:
        max_till_here.append(max(n, max_till_here[-1] + n))
    return max(max_till_here)

print find_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) # 6
print find_max_subarray([ -1, 3, -5, 4, 6, -1, 2, -7, 13, -3 ]) # 17
