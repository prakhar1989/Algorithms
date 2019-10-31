def egcd(a, b):
    if a==0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b%a, a)
        return gcd, y-(b//a)*x, x

if __name__ == '__main__':
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    gcd, x, y = egcd(a, b)
    print(egcd(a,b))
    if gcd!=1:
        print("M.I. doesn't exist")
    else:
        print('M.I. of b under modulo a is: ', (x%b + b)%b)
