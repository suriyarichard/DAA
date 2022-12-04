n=int(input("Enter No.of Elements: "))
arr=[]
print("Enter the elements: ")
for i in range(n):
    arr.append(int(input()))
    
print("Array after sorting is: ")
for i in range(len(arr)):   
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print(arr)
k=int(input("Enter the value to search: "))
def bs(arr, l, r, x):   
    if r >= l: 
        mid = l + (r - l) // 2         
        if arr[mid] == x:
            return mid 
        elif arr[mid] > x:
            return bs(arr, l, mid-1, x) 
        else:
            return bs(arr, mid + 1, r, x) 
    else:
        return -1
ans = bs(arr, 0, len(arr)-1, k) 
if ans!=-1:
    print("Element is at index % d" % ans)
else:
    print("Not in the array")