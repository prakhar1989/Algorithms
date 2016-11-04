#Time Complexity O(n)
#Limitations Only Upto Certain No. Sorting can be done.
count=[0]*1000
inp=[int(i) for i in raw_input("Enter Elements Below 1000:\n").split()]
B=[0]*(len(inp)+1)
for i in inp:
	count[i]+=1 #At this Stage Array count stores number of occurences of i
#print count
for i in range(max(inp)+1):
	count[i]=count[i]+count[i-1]
	# At this Stage Count contains number of elements less than i 
#print count
#print inp
for i in range(len(inp)):
	#print inp[i]
	B[count[inp[i]]]=inp[i]
	count[inp[i]]-=1
print B[1:]
	
