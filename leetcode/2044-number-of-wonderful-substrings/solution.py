class Solution:

  def wonderfulSubstrings(self, word: str) -> int:
    count = [0] * 1024
    count[0] = 1
    mask = 0
    ans = 0

    for ch in word:
      mask ^= 1 << (ord(ch) - ord('a'))
      # Case 1: All characters have even frequencies
      ans += count[mask]
      # Case 2: Exactly one character has an odd frequency
      for bit in range(10):
        ans += count[mask ^ (1 << bit)]
      count[mask] += 1

    return ans
