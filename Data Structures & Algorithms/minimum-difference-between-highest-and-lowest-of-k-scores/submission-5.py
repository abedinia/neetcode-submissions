class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        min_out = float('inf')
        nums.sort()
        l, r = 0, k - 1
        while r < len(nums):
            min_out = min(min_out, nums[r] - nums[l])
            l, r = l+1, r+1

        return min_out
