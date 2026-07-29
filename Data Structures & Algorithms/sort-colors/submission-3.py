#dnf algo
class Solution:
    
    def sortColors(self, nums: List[int]) -> None:
        def swap_list(nums,a,b):
            nums[a],nums[b] = nums[b],nums[a]
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        mid = 0
        end = len(nums)-1

        while mid <= end:
            if nums[mid]==0:
                swap_list(nums,start,mid)
                mid+=1
                start+=1

            elif nums[mid] ==1:
                mid+=1

            else:
                swap_list(nums,mid,end)
                end-=1