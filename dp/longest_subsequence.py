def longest_seq(seq):
    """ returns the longest increasing subseqence
    in a sequence """
    cache = [1] * len(nums)
    solution = [0] * len(nums)

    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                if cache[j] + 1 > cache[i]:
                    cache[i] = cache[j] + 1
                    solution[i] = j
    return max(cache), solution

if __name__ == "__main__":
    seq = [5, 2, 8, 10, 3, 6, 9, 7]
    seq2 = [0, 8, 3, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    seq3 = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    print longest_seq(seq3)

