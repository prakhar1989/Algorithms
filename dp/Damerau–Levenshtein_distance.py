def distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in xrange(0,lenstr1+1):
        d[(i,0)] = i
    for j in xrange(0,lenstr2+1):
        d[(0,j)] = j
 
    for i in xrange(1 , lenstr1+1):
        for j in xrange(1 ,lenstr2+1):
            if s1[i-1] == s2[j-1]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, 
                           d[(i,j-1)] + 1, 
                           d[(i-1,j-1)] + cost, 
                          )
            if i>1 and j>1 and s1[i-1]==s2[j-2] and s1[i-2] == s2[j-1]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost)
 
    return d[lenstr1,lenstr2]
