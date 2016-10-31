# Compute a temporary array to find size of suffix same as prefix
# Time/space complexity is O(m) m:size of the pattern. 
def temporary_array(pattern):
    l = len(pattern)
    lsp = [0 for j in range(l)]
    index = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[index]:
            lsp[i] = index + 1
            index += 1
            i += 1
        else:
            if index != 0:
                index = lsp[index - 1]
            else:
                lsp[i] = 0
                i += 1
    return lsp


# KMP algorithm of pattern matching.
# above function will be used here.
def kmp(giventext, pattern):
    lsp = temporary_array(pattern)
    i = 0
    j = 0
    while i < len(giventext) and j < len(pattern):
        if giventext[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lsp[j - 1]
            else:
                i += 1
    if j == len(pattern):  #here,i have taken 1 as True and 0 as false.U can modify as per the requirement.
        print 1
    else:
        print 0
        
