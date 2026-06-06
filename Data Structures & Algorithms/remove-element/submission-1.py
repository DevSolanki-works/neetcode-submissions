class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lp = 0
        while lp < len(nums):
            if nums[lp] == val:
                nums.remove(nums[lp])
            else:
                lp += 1
        return lp