'''
栈
'''

class Stack:
    def __init__(self):
        self.__list = []

    # 入栈
    def push(self, item):
        self.__list.append(item)

    # 出栈
    def pop(self):
        return self.__list.pop()

    # 返回栈顶元素
    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None

    # 判断栈是否为空
    def is_empty(self):
        return self.__list == []

    # 返回栈大小
    def size(self):
        return len(self.__list)

'''
测试执行
'''
if __name__ == '__main__':
    st = Stack()

    # 入栈
    st.push(1)
    st.push(3)
    st.push(5)

    # 出栈
    print(st.pop())
    print(st.pop())
    print(st.pop())