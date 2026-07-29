class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(nums,low,high):
            i = low
            j = high
            pivot = nums[low]
            while i<j:
                while nums[i]<=pivot and i<high:
                    i+=1
                while nums[j]>pivot and j>low:
                    j-=1
                if i<j:
                    nums[i],nums[j] = nums[j],nums[i]
            
            nums[low],nums[j] = nums[j],nums[low]
            return j
        def quick_sort(nums,low,high):
            i = low
            j = high
            if i<j:
                index = partition(nums,low,high)
                quick_sort(nums,low,index-1)
                quick_sort(nums,index+1,high)
            return
        quick_sort(nums,0,len(nums)-1)