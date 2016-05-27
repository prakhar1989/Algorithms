"""
Given two strings s1 and s2, edit distance is the minimum
number of operations needed to convert s1 to s2.

>>> Edit distance is also known as Levenshtein distance
>>> Allowed Operations are Insert, Remove and Replace.

Problem : https://en.wikipedia.org/wiki/Levenshtein_distance
"""

def edit_distance(s1,s2):
    # lengths of strings s1 and s2
    m, n = len(s1), len(s2)
    # to cache the results
    cache = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0:
               cache[i][j]=j
            elif j==0:
               cache[i][j]=i
            elif s1[i-1] == s2[j-1]:
               cache[i][j] = cache[i-1][j-1]
            else:
               cache[i][j] = 1+min([ cache[i-1][j], cache[i][j-1], cache[i-1][j-1] ])

    # return edit distance between given strings s1 and s2
    return cache[m][n]

if __name__ == "__main__":
    print(edit_distance("ABCXYZ","ACBCXZ"))
