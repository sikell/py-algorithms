def naive_multiplication(n, a, b):
    c = []
    i = 0
    while i < n:
        c.insert(i, [])
        j = 0
        while j < n:
            c[i].insert(j, 0)
            k = 0
            while k < n:
                c[i][j] += a[i][k] * b[k][j]
                k += 1
            j += 1
        i += 1
    return c


m1 = [[1, 3, 4], [4, 6, 0], [1, 1, 2]]
m2 = [[4, 2, 1], [5, 5, 2], [0, 0, 1]]
m = naive_multiplication(3, m1, m2)
print(m)