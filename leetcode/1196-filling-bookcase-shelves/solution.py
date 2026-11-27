class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            curr_width = 0
            max_height = 0
            
            for j in range(i, 0, -1):
                thickness, height = books[j - 1]
                curr_width += thickness
                if curr_width > shelfWidth:
                    break
                max_height = max(max_height, height)
                dp[i] = min(dp[i], dp[j - 1] + max_height)
                
        return dp[n]
