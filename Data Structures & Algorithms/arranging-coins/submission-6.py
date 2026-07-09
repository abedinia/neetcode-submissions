class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        num = 0
        for i in range(1, n+1):
            print(i)
            num += i
            if num <= n:
                rows += 1
            else:
                return rows
        return rows