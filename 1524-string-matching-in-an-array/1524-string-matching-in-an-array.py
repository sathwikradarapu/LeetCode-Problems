class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[j] in words[i]:  # Check if words[j] is a substring of words[i]
                    res.append(words[j])
        return(list(set(res)))
