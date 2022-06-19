class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b
        if not b:
            return a
        
        if len(a) < len(b):
            a, b = b, a
        a = a[::-1]
        b = b[::-1]
        carry = 0
        res = []
        
        for i in range(len(a)):
            if i < len(b):
                curr_sum = int(a[i]) + int(b[i]) + carry
            else:
                curr_sum = int(a[i]) + carry
                
            carry = curr_sum // 2
            res.append(str(curr_sum % 2))
        
        if carry:
            res.append(str(carry))
            
        return ''.join(res)[::-1]