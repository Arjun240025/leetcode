class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={0:1}
        curr_sum=0
        count=0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            
            need=curr_sum-k
            
            count+=freq.get(need,0)#if the current need already exists in the dict this method increases the value of count by 
        #Yes! Exactly. It uses the existing frequency (number of occurrences) of the need value in the dictionary
            freq[curr_sum]=freq.get(curr_sum,0)+1
        return count