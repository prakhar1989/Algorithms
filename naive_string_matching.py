def naive(word, text):
    m = len(word)
    n = len(text)

    counter = 0

    for i in range(0,n-m+1):
        found = True
        for j in range(0, m):
            if word[j] != text[i+j]:
                found = False
                break
        if found: 
            counter += 1

    if counter == 0:
        print "No match"
    else:
        print "The word appears: ",counter, "times!"

naive("ata","ata")
naive("ata","atata")
naive("ata","aaaaaaa")
naive("ata","")
naive("125","1259784651887125987894125")