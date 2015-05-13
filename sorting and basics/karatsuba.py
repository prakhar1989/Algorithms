def karatsuba(x, y, b=10):
    """ returns product of x, y. Uses base b
    in karatsuba algorithm
    Gives running time of O(n^1.585) as opposed to
    O(n^2) of naive multiplication
    >>> karatsuba(1234223123412323, 1234534213423333123)
    1523690672850721578619752112274729L
    """

    if x < 1000 or y < 1000:
        return x * y
    m = min(len(str(x)) / 2, len(str(y)) / 2)
    bm = b**m
    x1, x0 = x / bm, x % bm
    y1, y0 = y / bm, y % bm
    z1 = karatsuba(x1, y1, b)
    z3 = karatsuba(x0, y0, b)
    z2 = karatsuba(x1 + x0, y1 + y0, b) - z1 - z3
    return (bm**2)*z1 + bm*z2 + z3

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
