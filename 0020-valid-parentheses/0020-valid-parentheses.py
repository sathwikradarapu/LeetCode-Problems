class Solution:
    def isValid(self, s: str) -> bool:
        dici={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack=[]
        for i in s:
            if i not in dici:
                stack.append(i)
            else:
                if not stack or stack[-1]!=dici[i]:
                    return False
                else:
                    stack.pop()
        if not stack:
            return True
        return False