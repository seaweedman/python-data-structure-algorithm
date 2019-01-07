'''
双链表
'''

# 节点
class Node:
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.pre = None