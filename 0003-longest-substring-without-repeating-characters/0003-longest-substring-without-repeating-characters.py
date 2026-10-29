class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''#bruteforce
        length=len(s)
        if length==1:
            return length
        max_length=float("-inf")
        for index1 in range(length-1):
            for index2 in range(index1+1,length+1):
                sub_string=s[index1:index2]
                set_sub_string=set(sub_string)
                if len(sub_string)==len(set_sub_string):
                    max_length=max(max_length,len(sub_string))
        return max_length'''

        #optimise
        length=len(s)
        if length==0:
            return length
        left=0
        temp=""
        max_length=float("-inf")
        for right in range(length):
            temp+=s[right]
            while len(temp)!=len(set(temp)):
                temp=temp[1:]
                left+=1
            if len(temp)==len(set(temp)):
                max_length=max(max_length,len(temp))
        return max_length