class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        a=set()
        b=[]
        i=0
        while i<n:
            j=i+1
            while j<n:
                k=j+1
                l=n-1
                while k<l:
                    c=nums[i]
                    d=nums[j]
                    e=nums[k]
                    f=nums[l]
                    if c+d+e+f==target:
                        g=[c,d,e,f]
                        g.sort()
                        g=tuple(g)
                        a.add(g)
                        k+=1
                        l-=1
                    elif c+d+e+f<target:
                        k+=1
                    else:
                        l-=1
                j+=1
            i+=1
        for h in a:
            h=list(h)
            b.append(h)
        return b