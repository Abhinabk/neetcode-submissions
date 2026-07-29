from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        visited=set()
        for i in range(len(strs)):
            if strs[i] in visited:
                continue

            item = Counter(strs[i])
            temp=[strs[i]]
            visited.add(strs[i])

            for j in range(i+1,len(strs)):
                compare = Counter(strs[j])
                if item == compare:
                    temp.append(strs[j])
                    visited.add(strs[j])
            result.append(temp)
        return result
            