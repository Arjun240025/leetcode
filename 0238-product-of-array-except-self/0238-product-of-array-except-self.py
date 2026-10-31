class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # res=[]
        # for i in range(len(nums)):
        #     p=1
        #     for j in range(len(nums)):
        #          if i!=j:
        #             p*=nums[j]
        #     res.append(p)
        # return res(not optimal)
        res=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix#without * it overwrites prefix
            postfix*=nums[i]
        return res