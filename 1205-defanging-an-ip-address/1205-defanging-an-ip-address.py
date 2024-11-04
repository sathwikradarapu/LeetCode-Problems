class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_str=""
        for i in address:
            if i=='.':
                new_str+="[.]"
            else:
                new_str+=i
        return new_str