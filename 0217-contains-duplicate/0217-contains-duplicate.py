class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)
        freq = {}  # time complexity is 0[1] so thats why this is best and optimal code 

        for i in range(0,n):
            freq[nums[i]]=freq.get(nums[i],0)+1

            if freq[nums[i]]>=2:
                return True

        return False
       

        



        