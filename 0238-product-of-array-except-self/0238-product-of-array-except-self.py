class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix,suffix,output=[],[],[]
        for i in range(n):
            prefix.append(0)
            suffix.append(0)
            output.append(0)
        prefix[0],suffix[-1]=nums[0],nums[-1]
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i]
        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i]
        nums=prefix
        output=suffix
        for i in range(n):
            if i!=0 and i!=(n-1):
                output[i]=nums[i-1]*output[i+1]
            elif i==0:
                output[i]=output[i+1]
            else:
                output[i]=nums[i-1]
        return output
                