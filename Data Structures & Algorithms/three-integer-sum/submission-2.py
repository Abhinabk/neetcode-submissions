class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i]>0:
                break
            left = i+1
            right = len(nums)-1

            while left<right:
                target = -nums[i]

                if nums[left] + nums[right] ==target:
                    triplets.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1 
                    while left < right and nums[left] ==  nums[left-1]:
                        left+=1

                elif nums[left] + nums[right] < target:
                    left+=1
                else:
                    right-=1


        return triplets
    

