from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        elem_count = Counter(nums)
        size = len(nums)//2
        print(size)
        for item,count in elem_count.items():
            if count > size:
                return item