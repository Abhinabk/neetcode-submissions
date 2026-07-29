class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            l = 0
            r = 0
            sorted_arr = []
            while l < len(left) and r <len(right):
                if left[l] <= right[r]:
                    sorted_arr.append(left[l])
                    l+=1
                else:
                    sorted_arr.append(right[r])
                    r+=1

            while l < len(left):
                sorted_arr.append(left[l])
                l+=1

            while r < len(right):
                sorted_arr.append(right[r])
                r+=1

            return sorted_arr

        def merge_sort(nums):
            if len(nums)<=1:
                return nums

            mid = len(nums)//2
            left_arr = nums[:mid]
            right_arr = nums[mid:]

            left = merge_sort(left_arr)
            right = merge_sort(right_arr)

            return merge(left,right)
        
        return merge_sort(nums)


        