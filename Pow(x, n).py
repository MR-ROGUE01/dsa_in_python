class Solution:
    def myPow(self,x : float,n : int) -> float:
        binform = n
        if(binform < 0):
            x = 1/x
            binform = -binform
        ans = 1
        while binform > 0 :
            if binform % 2 == 1:
                ans = ans * x
            x = x * x
            binform = binform // 2
        return ans