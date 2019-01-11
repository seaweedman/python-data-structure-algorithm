'''
希尔排序
'''

'''
可以理解为通过步长优化的插入排序
'''

def shellSort(arr):
    length = len(arr)
    # 步长
    gap = length // 2

    while gap >= 1:
        for k in range(0, gap):
            for i in range(k+gap, length, gap):
                for j in range(i, 0, -gap):
                    if arr[j] < arr[j-gap]:
                        arr[j], arr[j-gap] = arr[j-gap], arr[j]
                    else:
                        break
        gap = gap // 2

if __name__ == '__main__':
    test = [9, 8, 7, 6, 5, 4, 3, 1, 2, 10, 18, 100, 60, 50, 40]
    shellSort(test)
    print(test)