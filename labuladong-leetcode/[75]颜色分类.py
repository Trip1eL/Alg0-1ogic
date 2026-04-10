
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0] * 3
        for i in nums:
            arr[i] += 1
        index = 0
        for i in range(3):
            for _ in range(arr[i]):
                nums[index] = i
                index += 1

# leetcode submit region end(Prohibit modification and deletion)
