
# leetcode submit region begin(Prohibit modification and deletion)
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None
class MyLinkedList(object):
    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.pre = self.tail
        self.head.next = self.tail
        self.tail.pre = self.head
        self.tail.next = self.head
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for i in range(index + 1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newnode = ListNode(val)
        newnode.next = self.head.next
        newnode.pre = self.head
        self.head.next.pre = newnode
        self.head.next = newnode
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        newnode = ListNode(val)
        newnode.next = self.tail
        newnode.pre = self.tail.pre
        self.tail.pre.next = newnode
        self.tail.pre = newnode
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.size:
            return
        cur = self.head
        for i in range(index):
            cur = cur.next
        new_node = ListNode(val)
        new_node.next = cur.next
        new_node.pre = cur
        cur.next.pre = new_node
        cur.next = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        cur = self.head
        for i in range(index):
            cur = cur.next
        delete_node = cur.next
        cur.next = delete_node.next
        delete_node.next.pre = cur
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# leetcode submit region end(Prohibit modification and deletion)
