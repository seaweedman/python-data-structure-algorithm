'''
插入排序
'''

def insertionSort(arr):
    length = len(arr)

    for i in range(1, length):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

if __name__ == '__main__':
    test = [12, 8, 9, 10, 7, 6, 5, 4, 3, 2, 11]
    print(test)
    insertionSort(test)
    print(test)
