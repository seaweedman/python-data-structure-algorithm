'''
单链表
'''

# 节点
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

# 单链表
class SingleLinkList:
    def __init__(self, node=None):
        self.__head = node

    # 链表是否为空
    def is_empty(self):
        return self.__head == None
    
    # 链表长度
    def length(self):
        # 游标
        cur = self.__head
        # 统计
        count = 0

        while cur != None:
            count += 1
            cur = cur.next

        return count

    # 遍历整个链表
    def travel(self):
        cur = self.__head

        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next

        print('')

    # 在头部添加元素
    def add(self, item):
        node = Node(item)
        node.next = self.__head
        self.__head = node

    # 链表尾部添加元素
    def append(self, item):
        node = Node(item)

        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head

            while cur.next != None:
                cur = cur.next

            cur.next = node

    # 指定位置添加元素
    def insert(self, pos, item):
        node = Node(item)
        pre = self.__head

        if pos < 1:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            count = 0
            while count < pos - 1:
                count += 1
                pre = pre.next

            node.next = pre.next
            pre.next = node

    # 删除节点
    def remove(self, item):
        pre = None
        cur = self.__head

        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next

                break
            else:
                pre = cur
                cur = cur.next

    # 查找节点是否存在
    def search(self, item):
        cur = self.__head

        while cur != None:
            if cur.elem == item:
                return True

            cur = cur.next

        return False

if __name__ == '__main__':
    sll = SingleLinkList()

    sll.travel()

    print(sll.is_empty())
    print(sll.length())

    sll.append(10)
    print(sll.is_empty())
    print(sll.length())

    sll.append(12)
    sll.append(14)
    sll.append(16)
    sll.append(17)
    
    sll.travel()

    print('-------------- add test -------------------')

    sll.add(8)
    sll.travel()

    print('-------------- insert test -----------------')

    sll.insert(3, 13)
    sll.travel()

    print('-------------- delete test -----------------')
    sll.remove(10)
    sll.travel()