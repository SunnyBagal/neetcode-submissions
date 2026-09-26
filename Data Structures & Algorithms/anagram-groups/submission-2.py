class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    


        res = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for t in word :
                count[ord(t) - 97] += 1

            res[tuple(count)].append(word)
        
        return list(res.values())