def min_niza(A):
    najmanji = A[0]
    for i in range(len(A)):
        if A[i] < najmanji: najmanji = A[i]
    return najmanji

print(min_niza([3,1,5,-1,2]))
