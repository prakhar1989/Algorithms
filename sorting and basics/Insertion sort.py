# Insertion sort tutorial
a = [3, 2, 4, 8, 9, 1, 3, 98, -9, -5, -4, 6, 3, -45, 97, 74]
for i in range(len(a)):
    b = i
    while a[b + 1] < a[b]:
        c = a[b]
        a[b] = a[b + 1]
        a[b + 1] = c
        b = b - 1
        print(a)
        if b == -1:
            break
