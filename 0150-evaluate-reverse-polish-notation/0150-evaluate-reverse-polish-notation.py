class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i.isdigit() or (i.startswith("-") and i[1:].isdigit()):
                stack.append(int(i))
            else:
                b=stack.pop()
                a=stack.pop()
                if i=='+':
                    c=b+a
                elif i=='-':
                    c=a-b
                elif i=='*':
                    c=b*a
                else:
                    c=int(a/b)
                stack.append(c)
        return stack[-1]