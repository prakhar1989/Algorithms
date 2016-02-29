from heapq import heappush, heappop, heapify
from collections import defaultdict
 

def codes(f):
	h = [[wt, [sym, ""]] for sym, wt in f.items()]
	heapify(h)
	while len(h) > 1:
		lo = heappop(h)
		hi = heappop(h)
		for pair in hi[1:]:
			pair[1] = '1' + pair[1]
		for pair in lo[1:]:
			pair[1] = '0' + pair[1]
		heappush(h, [lo[0] + hi[0]] + lo[1:] + hi[1:])
	return sorted(heappop(h)[1:])
 


def encode(stri, huff):
	ans=''
	ec={}
	for i in huff:
		ec[i[0]]=i[1]
	for ch in stri:
		ans+=ec[ch]
	return ans


def decode(stri, huff):
	dc={}	
	for p in huff:
		dc[p[1]]=p[0]
	si=''
	ans=''
	for ch in stri:
		si+=ch
		if si in dc:
			ans+=dc[si]
			si=''
	return ans
	

f = defaultdict(int)
f={'a':3,'b':0,'c':2,'d':1}
huff = codes(f)
for ch, code in huff:
	print ch, code
print encode('aaadc', huff)
print decode(encode('aaadc',huff),huff)

