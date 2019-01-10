'''
选择排序
'''

def selectionSort(arr):
    length = len(arr)

    for j in range(length-1):
        for i in range(j, length-1):
            if arr[j] > arr[i+1]:
                arr[j], arr[i+1] = arr[i+1], arr[j]

if __name__ == '__main__':
    test = [100, 40, 45, 60, 50, 49, 42, 30, 28, 6, 5, 5, 5, 5, 4, 3, 1]
    selectionSort(test)
    print(test)