
# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    # def preorder(self, root):
    #     """
    #     :type root: Node
    #     :rtype: List[int]
    #     """
    #     rlist = []
    #     if root is None:
    #         return[]
    #     rlist.append(root.val)
    #     for child in root.children:
    #         rlist.extend(self.preorder(child))
    #     return rlist
    # 迭代法（非递归法）
    def preorder(self, root):
        """
            :type root: Node
            :rtype: List[int]
        """
        rlist = [root]
        res = []
        if not root:
            return []
        while rlist:
            node = rlist.pop()
            res.append(node.val)
            rlist.extend(node.children[::-1])
        return res
# leetcode submit region end(Prohibit modification and deletion)
