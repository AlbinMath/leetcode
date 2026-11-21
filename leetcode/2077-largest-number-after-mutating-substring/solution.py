class Solution:
    def maximumNumber(self, num: str, change: list[int]) -> str:
        digits = list(num)
        mutated = False
        
        for i, ch in enumerate(digits):
            d = int(ch)
            
            if change[d] > d:
                # Start or continue mutating on a strictly better digit
                digits[i] = str(change[d])
                mutated = True
            elif change[d] == d:
                # Neutral digit: keep going if we've already started, otherwise ignore
                continue
            else:
                # change[d] < d: if we already started mutating, we must stop here
                if mutated:
                    break
                    
        return "".join(digits)
