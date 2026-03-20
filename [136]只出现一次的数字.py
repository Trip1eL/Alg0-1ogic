
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num={}
        for i in nums:
            if i not in num:
                num[i]=1
            else:
                num[i]+=1
        for i in nums:
            if num[i]==1:
                return i
# leetcode submit region end(Prohibit modification and deletion)
