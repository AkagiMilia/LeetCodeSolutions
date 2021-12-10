'''

    插入排序
    O(n^2)


'''

array = [7, 6, 5, 3, 4, 1, 2]

for i in range(1, len(array)):
    for j in range(i-1, -1, -1):
        if array[j+1] < array[j]:
            array[j+1], array[j] = array[j], array[j+1]
print('result:', array)