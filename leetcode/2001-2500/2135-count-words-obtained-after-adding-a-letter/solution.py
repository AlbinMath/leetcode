from typing import List


class Solution:

  def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
    def get_mask(word: str) -> int:
      mask = 0
      for ch in word:
        mask |= 1 << (ord(ch) - ord('a'))
      return mask

    # Step 1: Store bitmasks of all startWords
    start_masks = {get_mask(w) for w in startWords}

    # Step 2: For each targetWord, try removing one character at a time
    ans = 0
    for w in targetWords:
      t_mask = get_mask(w)
      for ch in w:
        candidate = t_mask ^ (1 << (ord(ch) - ord('a')))
        if candidate in start_masks:
          ans += 1
          break

    return ans
