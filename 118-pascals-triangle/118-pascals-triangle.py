class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        
        prev = self.generate(n - 1)
        curr = [1]
        
        for i in range(len(prev[-1]) - 1):
            curr.append(prev[-1][i] + prev[-1][i + 1])
            
        curr.append(1)
        prev.append(curr)
        
        return prev