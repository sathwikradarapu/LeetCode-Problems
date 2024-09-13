class Solution:
    def countValidWords(self, sentence: str) -> int:
        sentence_list = sentence.split()
        count = 0
        for i, word in enumerate(sentence_list):
            valid = True
            hyphen_count = 0  
            for j, letter in enumerate(word):
                if letter.isdigit():
                    valid = False 
                    break
                if letter in ("!",".",",") and j != len(word)-1:
                    valid = False 
                    break
                if (letter == "-" and (j == len(word)-1 or j == 0)) or (letter == "-" and (not word[j-1].isalpha() or not word[j+1].isalpha())):
                    valid = False 
                    break
                if letter == "-":
                    hyphen_count +=1
                    if hyphen_count >1:
                        valid = False 
                        break
            if valid:
                count +=1
        return count