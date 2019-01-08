'''
冒泡排序
'''

'''
无限循环
每次都从第一个元素比较到最后一个元素
当某一次没有任何两个元素之间发生交换
说明排序完成
'''
def bubbleSort(arr):
    length = len(arr)

    flag = True
    while flag:
        flag = False
        for i in range(length - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = True

if __name__ == '__main__':
    test = [1, 12, 6, 3, 4, 2, 1]
    bubbleSort(test)
    print(test)