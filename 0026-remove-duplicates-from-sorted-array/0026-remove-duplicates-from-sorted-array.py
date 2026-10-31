class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        res=[]
        for i in nums:
            if i not in res:
                res.append(i)
            
        nums[:len(res)] = res  # Replace the beginning of nums with unique elements
        return len(res)

#     For my understanding 
# - len(res) determines how many unique elements there are.
# - nums[:len(res)] selects that many elements from the beginning of nums.
# - = res replaces those selected elements with the elements in res.
# - The original nums list is modified; a new list is not assigned to nums.
        

