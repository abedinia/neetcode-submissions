class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check_list = {}

        for i, v in enumerate(nums):
            if v in check_list:
                if abs(check_list[v] - i) <= k:
                    return True
            check_list[v] = i

        
        return False
    
