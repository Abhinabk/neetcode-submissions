# bucket sort 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0]*(max(nums)+1)

        for i in nums:
            bucket[i]+=1

        i = 0
        for b in range (len(bucket)):
            while bucket[b]>0:
                nums[i] = b
                i+=1
                bucket[b]-=1 
        