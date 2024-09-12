class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        prev_word = ""
        for word in words:
            sorted_word = "".join(sorted(word))
            if sorted_word != prev_word:
                res.append(word)
            prev_word = sorted_word
        return res
