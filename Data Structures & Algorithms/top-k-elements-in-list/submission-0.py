class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        result = []
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i] = 1
        sorted_map = sorted(hash_map.items(),
        key = lambda x : x[1],
        reverse = True
        )

        for i,j in sorted_map[:k]:
            result.append(i)
        return result
