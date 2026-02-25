class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = []
        for elem in str(x):
            l.append(elem)

        return l == l[::-1]
