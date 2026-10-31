class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res=[]
        count=0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
        for i in range(len(nums)):
            if nums[i]!=0:
                res.append(nums[i])
        nums[:]=res+count*[0]