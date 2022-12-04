p = 0
q = 1
n = int(input("Enter the number of terms: "))
i = 2
List = [p, q]
while i < n:
     fib = p + q
     List.append(fib)
     p = qq = fib
     i += 1
     print(List)