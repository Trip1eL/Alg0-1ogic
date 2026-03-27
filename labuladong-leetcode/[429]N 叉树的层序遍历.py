
# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        queue = [root]
        res = []
        if not root:
            return []
        while queue:
            sz = len(queue)
            cur_level = []
            for i in range(sz):
                node = queue.pop(0)
                cur_level.append(node.val)
                queue.extend(node.children)
            res.append(cur_level)
        return res
# leetcode submit region end(Prohibit modification and deletion)
