
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
# leetcode submit region end(Prohibit modification and deletion)
