class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        original = x
        reverse = 0
    
        while (x != 0):
            remainder = x % 10
            reverse = reverse * 10 + remainder
            x = x// 10
        return original == reverse
obj = Solution()

print(obj.isPalindrome(121))   # True
print(obj.isPalindrome(123))   # False
print(obj.isPalindrome(-121))  # False
