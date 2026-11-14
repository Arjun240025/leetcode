class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        res=sorted(freq,key=freq.get,reverse=True)
        return res[:k]

# sorted(freq) → Sort dictionary keys.
# key=freq.get → Sort based on frequency values.
# reverse=True → Highest frequency first.
# res[:k] → Select the top K elements.