'''
队列
'''

class Queue:
    def __init__(self):
        self.__list = []

    # 入队
    def enqueue(self, item):
        self.__list.append(item)

    # 出队
    def dequeue(self):
        return self.__list.pop(0)

    # 判断是否为空
    def is_empty(self):
        return self.__list == []

    # 返回队列大小
    def size(self):
        return len(self.__list)

'''
测试执行
'''
if __name__ == '__main__':
    qu = Queue()

    # 入队
    qu.enqueue(1)
    qu.enqueue(3)
    qu.enqueue(5)

    # 出队
    print(qu.dequeue())
    print(qu.dequeue())
    print(qu.dequeue())