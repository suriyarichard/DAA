def LCS(A, B, n, m):
    p = []
    LCS = [[0 for col in range(0, n+1)] for row in range(0, m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
         if A[j-1] == B[i-1]:
            LCS[i][j] = 1 + LCS[i-1][j-1]
            p.append(A[j-1])
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
    print("\nLCS Table: ")
    for i in range(0, m+1):
        for j in range(0, n+1):
            print(LCS[i][j], end=" ")
        print("")
    return p

A = list(input("First string: "))
B = list(input("Second string: "))
n = len(A)
m = len(B)
if n > m:
 result = LCS(A, B, n, m)
else:
 result = LCS(B, A, m, n)
print("\nLongest Common Subsequence: ", result)