class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count_T = count_F = max_freq = left = 0
        
        for right, ch in enumerate(answerKey):
            if ch == 'T':
                count_T += 1
                if count_T > max_freq:
                    max_freq = count_T
            else:
                count_F += 1
                if count_F > max_freq:
                    max_freq = count_F
                    
            if (right - left + 1) - max_freq > k:
                if answerKey[left] == 'T':
                    count_T -= 1
                else:
                    count_F -= 1
                left += 1
                
        return len(answerKey) - left
