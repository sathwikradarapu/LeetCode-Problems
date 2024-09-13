class Solution:
    def countValidWords(self, sentence: str) -> int:
        # time 51 ms, faster than 85.11% effiecent, space inefficent 16.7 MB, less than 14.18%
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        digits = '0123456789'
        punctuations = '!.,'
        hyphens = '-'
        
        # remove any spaces at the beginning or end of the sentence if there any.
        
        tokens= []
        word = ''
        # make an array of tokens to make that 
        for i in sentence:
            if i != ' ':
                word+=i
            else:
                if word != '':
                    tokens.append(word)
                word=''
        if word != '':
            tokens.append(word) #appends the last word in the senctence
        
        print(tokens)
        
        validWords = 0
        
        
        for word in tokens:
            hyphenCounter = 0
            y =  word[:len(word)-1]
            #There is at most one punctuation mark. If present, it must be at the end of the token
            if '!' in y or '.' in y or ',' in y:
                continue
            # if haphen come at the begining or end continue
            if word[0] == '-' or word[-1] =='-':
                continue
                
            # test the validity of each charcter separately 
            for i in range(len(word)):
                if word[i] in digits:   # if there is a digit break
                    break
                    
                
                if word[i] == '-':
                    # If present, it must be surrounded by lowercase characters
                    if word[i-1] not in alphabets or word[i+1] not in alphabets:
                        break
                    hyphenCounter +=1
                
                    
                # There is at most one hyphen '-'
                if hyphenCounter >1:
                    break
                    
                # if you have reached the end of word increament validwords  
                if i == len(word)-1:
                    validWords +=1
        return validWords