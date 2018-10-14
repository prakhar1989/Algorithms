import time
def naive():
    txt=raw_input("Enter the input string ")
    find=raw_input("Enter the string to be found ")
    a=time.clock()
    flag=0
    for i in range(len(find),len(txt)+1):
        if txt[i-len(find):i]==find:
            print"Found at "+ str(i)
            flag=1

    if flag==0:
        print "Not found"
    print "Time taken is "+str(time.clock()-a)

naive()
