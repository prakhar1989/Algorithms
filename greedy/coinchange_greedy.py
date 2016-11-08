# This is a greedy version of Coinchange Algorithm. 
# It should be noted that this algorithm will produce the 
# optimal amount of coins only in the , so called, canocical 
# coin systems (like the one used in the US).

def coinchange(coins, amount):
	coins = sorted(coins,reverse=True)
	c = 0 
	for i in coins:
		c = c + amount // i
		amount = amount % i
	return c

# Below is a test case for that algorithm
coins = [1, 2, 10, 5]


print coins

print coinchange(coins,15)
	
