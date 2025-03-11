M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(M[0])
print(M[1])
print(M[2], '\n')

diag = [M[i][i] for i in [0, 1, 2]]
print(diag, '\n')

G = (sum(row) for row in M)
print(next(G))
print(next(G))
print(next(G))
