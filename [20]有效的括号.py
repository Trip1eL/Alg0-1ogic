
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        templist = []
        for i in s:
            if i in ['(', '[', '{']:
                templist.append(i)
            elif i in [')', ']', '}']:
                if len(templist) == 0:
                    return False
                if i == ')' and templist[-1] == '(':
                    templist.pop()
                elif i == ']' and templist[-1] == '[':
                    templist.pop()
                elif i == '}' and templist[-1] == '{':
                    templist.pop()
                else:
                    return False
        return not templist
        #not templist空时返回 True，非空时返回 False
# leetcode submit region end(Prohibit modification and deletion)
