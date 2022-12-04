def knapsack(arr,m):
    n=len(arr)
    size=m
    for i in range(n):
        ppw=arr[i][1]/arr[i][2]
        ppw=round(ppw,2)
        arr[i].append(ppw)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j][3]<arr[j+1][3]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    x={}
    profit=0
    for i in range(n):
        if size>=arr[i][2]:
            size=size-arr[i][2]
            x[arr[i][0]]=1
            profit+=arr[i][2]*arr[i][3]
        elif size!=0:
            val=size/arr[i][2]
            x[arr[i][0]]=val
            profit+=size*arr[i][3]
            size=0
        else:
            x[arr[i][0]]=0
    print(profit)
    print(x)    
    print(arr)
if __name__ == '__main__':
    arr = [['o1', 10, 2],
              ['o2', 5, 3],
              ['o3', 15, 5],
              ['o4', 7, 7],
              ['o5', 6, 1],
              ['o6', 18, 4],
              ['o7', 3, 1]]
    print("Suriyaprakash- 20170 \n-------------")
    print("maximum profit sequence is :")
    knapsack(arr, 15)