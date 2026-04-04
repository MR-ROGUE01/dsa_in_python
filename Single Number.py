from aiohttp_retry import List
class Solution:
    def singlenumber(self, nums : List[int]) -> int:
        result = 0

        for num in nums:
            result = result ^ num

        return result