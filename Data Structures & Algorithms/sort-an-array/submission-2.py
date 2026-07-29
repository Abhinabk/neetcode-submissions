import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums,low,high):
            pivot_index = random.randint(low,high)
            nums[low],nums[pivot_index] = nums[pivot_index],nums[low]
            i = low
            j = high
            pivot = nums[i]

            while i<j:
                while nums[i]<= pivot and i<high:
                    i+=1
                while nums[j]> pivot and j>low:
                    j-=1
                if i<j:
                    nums[i],nums[j] = nums[j],nums[i]
            
            nums[j],nums[low] = nums[low],nums[j]
            return j

        def quick_sort(nums,low,high):
            if low<high:
                index = partition(nums,low,high)
                quick_sort(nums,low,index-1)
                quick_sort(nums,index+1,high)

            return nums

        return quick_sort(nums,0,len(nums)-1)