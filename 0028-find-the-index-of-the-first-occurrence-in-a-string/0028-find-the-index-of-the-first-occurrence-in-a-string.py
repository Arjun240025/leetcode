class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

#  If found, .find() returns the first occurrence's index.
# If not found, it returns -1.