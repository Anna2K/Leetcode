class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_reversed = 0
        if x < 0:
            num = abs(x)
        else:
            num = x
        
        while num:
            remainder = num % 10
            x_reversed = (x_reversed * 10) + remainder
            num = num // 10
            
        if x == x_reversed:
            return True
        
        return False