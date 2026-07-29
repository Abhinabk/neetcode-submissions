#bucket sort approach
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[]for _ in range(len(nums)+1)]
        result = []
        for i in nums:
            freq[i] = freq.get(i,0)+1

        for i,j in freq.items():
            bucket[j].append(i)
        
        for i in range(len(bucket)-1,0,-1):

            for item in bucket[i]:
                result.append(item)
                if len(result)==k:
                    return result