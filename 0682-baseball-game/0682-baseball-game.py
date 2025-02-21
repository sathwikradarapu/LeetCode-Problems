class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            if i!='C' and i!='D' and i!='+':
                stack.append(int(i))
            elif i=='C':
                stack.pop()
            elif i=='D':
                stack.append(2*(stack[-1]))
            else:
                stack.append(stack[-1]+stack[-2])
        if stack:
            return sum(stack)
        return 0