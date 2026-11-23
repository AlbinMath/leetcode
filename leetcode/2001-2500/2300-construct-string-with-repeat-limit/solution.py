class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
            
        ans = []
        curr = 25       # Largest available character ('z')
        next_char = 24  # Next largest available separator character
        
        while curr >= 0:
            if freq[curr] == 0:
                curr -= 1
                continue
                
            use = min(freq[curr], repeatLimit)
            ans.append(chr(curr + ord('a')) * use)
            freq[curr] -= use
            
            if freq[curr] > 0:
                next_char = min(next_char, curr - 1)
                while next_char >= 0 and freq[next_char] == 0:
                    next_char -= 1
                    
                if next_char < 0:
                    break
                    
                ans.append(chr(next_char + ord('a')))
                freq[next_char] -= 1
                
        return "".join(ans)
