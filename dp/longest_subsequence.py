def longest_seq(seq):
    """ returns the longest increasing subseqence 
    in a sequence """
    count = [1] * len(seq)
    prev = [0] * len(seq)
    for i in range(1, len(seq)):
        dist = []
        temp_prev = {}
        for j in range(i):
            if seq[j] < seq[i]:
                dist.append(count[j])
                temp_prev[count[j]] = j
            else:
                temp_prev[0] = j
                dist.append(0)
        count[i] = 1 + max(dist)
        prev[i] = temp_prev[max(dist)]
    
    # path
    path = [seq[prev.index(max(prev))]]
    i = prev.index(max(prev))
    while i>1:
        path.append(seq[prev[i]])
        i = prev[i]
    return max(count), path[::-1]

if __name__ == "__main__":
    seq = [5, 2, 8, 10, 3, 6, 9, 7]
    seq2 = [0, 8, 3, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print longest_seq(seq2)

