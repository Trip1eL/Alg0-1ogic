
# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    # def postorder(self, root):
    #     """
    #     :type root: Node
    #     :rtype: List[int]
    #     """
    #     rlist = []
    #     if root is None:
    #         return[]
    #     for child in root.children:
    #         rlist.extend(self.postorder(child))
    #     rlist.append(root.val)
    #     return  rlist
    # 迭代（非递归法）
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        rlist = [(root, False)]
        res = []
        if not root:
            return []
        while rlist:
            node, visited = rlist.pop()
            if visited:
                res.append(node.val)
            else:
                rlist.append((node, True))
                for child in node.children[::-1]:
                    rlist.append((child, False))
        return res
# leetcode submit region end(Prohibit modification and deletion)
