def fibo(n):
    arr = [None for _ in range(n)]
    arr[0] = 1
    arr[1] = 2
    for i in range(2, n):
        arr[i] = arr[i - 1] + arr[i -2 ]
    return arr[-1]

def fibo_n(n):
    if n == 1: return 1
    if n == 2: return 2
    return fibo_n(n - 1) + fibo_n(n - 2)

aList = [20, 10, 16, 6, 89, 9, 1, 5, 100]
for i in range(len(aList)):
    for j in range(i+1, len(aList)):
        if aList[j] < aList[i]:
            aList[j], aList[i] = aList[i], aList[j]
print(aList)

print(fibo(50))

def divide(i, j, aList):
    if i == j:
        return [aList[i]]
    mid = (i + j) // 2
    print(i, mid)
    print(mid + 1, j)
    print('-----------')
    divide(i, mid, aList) 
    divide(mid + 1, j, aList)
divide(0, len(aList) - 1, aList)

def conquer(left_nums, right_nums):
    i = 0
    j = 0
    new_nums = []
    while i < len(left_nums) and j < len(right_nums):
        if left_nums[i] < right_nums[j]:
            new_nums.append(left_nums[i])
            i += 1
        else:
            new_nums.append(right_nums[j])
            j += 1
    new_nums += left_nums[i:]
    new_nums += right_nums[j:]
    return new_nums

final = divide(0, len(aList) - 1, aList)
print(final)