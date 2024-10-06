class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph).split()
        banned=set(banned)
        hash_map={}
        for i in paragraph:
            j=i.lower()
            if j not in banned:
                if j in hash_map:
                    hash_map[j]+=1
                else:
                    hash_map[j]=1
        sorted_dict = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_dict.keys())[0]
                