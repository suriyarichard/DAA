def printJobScheduling(arr):
    l = []
    for i in range(len(arr)):
        l.append(arr[i][1])
    t = 0
    for i in l:
        if i > t:
            t = i
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    result = [False] * t
    job = ['N'] * t
    p=[]
    for i in range(len(arr)):
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                p.append(arr[i][2])
                break
    print(job)
    print(sum(p))

if __name__ == '__main__':
    arr = [['J1', 5, 85],
           ['J2', 4, 25],
           ['J3', 3, 16],
           ['J4', 3, 40],
           ['J5', 4, 55],
           ['J6', 5, 19],
           ['J7', 2, 92],
           ['J8', 3, 80],
           ['J9', 7, 15]]
    print("Max Profit sequence of jobs:  ")
    printJobScheduling(arr)