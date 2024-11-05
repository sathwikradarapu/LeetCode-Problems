class Solution:
    def frequencySort(self, s: str) -> str:
        ans=""
        hash_map={}
        for i in s:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        sorted_by_values_desc = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))
        for i in sorted_by_values_desc:
            ans+=(i*hash_map[i])
        return ans