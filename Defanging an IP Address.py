class Solution:
    def defangIPaddr(self, address: str) -> str:
        new_string=""
        for i in address:
            if i==".":
                new_string+="[.]"
            else:
                new_string+=i
        return new_string
