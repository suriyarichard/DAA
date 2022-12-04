FibArray = [0, 1]
 
def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n < len(FibArray):
        return FibArray[n]
    else:
        for i in range(2,n):
            FibArray.append(fibonacci(i - 1) + fibonacci(i - 2))
    print(FibArray)
fibonacci(25)