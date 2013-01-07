def read_data(data):
    weights = []
    values = []
    for d in data:
        weights.append(int(d.split()[1]))
        values.append(int(d.split()[0]))
    return (weights, values)

def knapsack_rep(weights, values, W):
    """ knapsack with repetition """
    k = [0]*(W + 1)
    for w in range(1, W+1):
        k[w] = max([k[w-i] + values[i] if weights[i]<=w else 0 for i in range(len(weights))])
    return k[-1]

def knapsack(weights, values, W):
    """ knapsack without repetition. Takes O(w) space 
    Reference - http://books.google.co.in/books?id=u5DB7gck08YC&printsec=frontcover&dq=knapsack+problem&hl=en&sa=X&ei=1sbmUJSwDYWGrAeLi4GgCQ&ved=0CDUQ6AEwAA#v=onepage&q&f=true
    """
    optimal_vals = [0]*(W+1)
    for j in range(0, len(weights)):
        for w in range(W, weights[j]-1, -1):
            if optimal_vals[w-weights[j]] + values[j] > optimal_vals[w]:
                optimal_vals[w] = optimal_vals[w-weights[j]] + values[j]
    return optimal_vals[-1]

with open("kpdata2.txt") as f:
    (weights, values) = read_data(f)
# print knapsack_rep(weights, values, 10000)
#print knapsack(weights, values, 2000000)
