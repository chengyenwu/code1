# 219. Contains duplicate II
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # two pointer method
        s= set()
        i = 0
        j = 0
        while j < len(nums):
            if j-i <= k:
                if nums[j] not in s:
                    s.add(nums[j])
                    j+=1
                else:
                    return True
            else:
                s.remove(nums[i])
                i+=1
        return False