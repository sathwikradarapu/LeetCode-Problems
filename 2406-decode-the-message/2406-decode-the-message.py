class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hash_map={}
        alpha="abcdefghijklmnopqrstuvwxyz"
        index=0
        new_msg=""
        for i in key:
            if i!=' ' and i not in hash_map:
                hash_map[i]=alpha[index]
                index+=1
        for i in message:
            if i!=' ':
                new_msg+=hash_map[i]
            if i==' ':
                new_msg+=' '
        return new_msg