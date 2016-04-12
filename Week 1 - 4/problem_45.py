def triangle(n):
    return n*(n+1)/2
def pentagonal(n):
    return n*(3*n - 1) / 2
def hexagonal(n):
    return n * (2 * n - 1)

values = {}
for num in range(142, 100000):
    tri = triangle(num)
    pent = pentagonal(num)
    hex = hexagonal(num)
    if tri in values:
        values[tri].append(("T", num))
    if pent in values:
        values[pent].append(("P", num))
    else:
        values[pent] = [("P", num)]
    if hex in values:
        values[hex].append(("H", num))
    else:
        values[hex] = [("H", num)]

for val in values:
    if len(values[val]) > 2:
         print val, values[val]