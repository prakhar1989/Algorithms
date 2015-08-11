"""
Greatest common divisor(GCD) of two integers X and Y is the largest integer that divides both X and Y.

References : 
https://en.wikipedia.org/wiki/Euclidean_algorithm
https://proofwiki.org/wiki/Euclidean_Algorithm
http://stackoverflow.com/questions/6005582/how-does-the-euclidean-algorithm-work


Algorithm :
* If X = 0 then GCD(X,Y) = Y, as GCD(0,Y) = Y.
* If Y = 0 then GCD(X,Y) = X, as GCD(X,0) = X.
* Write X in quotient remainder form (X = Y * Q + R).
* Find GCD(Y,R) using the Euclidean algorithm since GCD(X,Y) = GCD(Y,R).
"""

def greatest_common_divisor(x,y):
    return x if y == 0 else greatest_common_divisor(y,x%y)

if __name__ == "__main__":
    print(greatest_common_divisor(20,25))
