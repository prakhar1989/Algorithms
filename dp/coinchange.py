"""
Problem: http://www.algorithmist.com/index.php/Coin_Change
"""
def coinchange(total, coins):
    M = len(coins)
    table = [[0]*M for i in range(total+1)]
    for i in range(M):
        table[0][i] = 1

    for i in range(1, total+1):
        for j in range(M):
            # count of solutions excluding coin
            x = table[i][j-1] if j > 0 else 0

            # count of solutions including coin
            y = table[i-coins[j]][j] if i - coins[j] >= 0 else 0
            table[i][j] = x + y

    return table[total][M-1]

if __name__ == "__main__":
    print coinchange(10, [2, 3, 5, 6]) # 5
    print coinchange(5, [2, 3, 5])     # 2
    print coinchange(4, [1, 2, 3])     # 4
