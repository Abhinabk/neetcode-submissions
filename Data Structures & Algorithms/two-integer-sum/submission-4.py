class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final={}
        for i,n in enumerate(nums):
           final[n]=i
        for i,n in enumerate(nums):
            diff=target-n
            if diff in final and final[diff]!=i:
                return [i,final[diff]]
    