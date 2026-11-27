# LeetCode 691: Stickers to Spell Word

**LeetCode Problem #691 — Stickers to Spell Word**
Solve LeetCode Stickers to Spell Word using JavaScript and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Stickers to Spell Word |
| LeetCode | #691 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
We are given `n` different types of `stickers`. Each sticker has a lowercase English word on it.

You would like to spell out the given string `target` by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

Return *the minimum number of stickers that you need to spell out *`target`. If the task is impossible, return `-1`.

**Note:** In all test cases, all words were chosen randomly from the `1000` most common US English words, and `target` was chosen as a concatenation of two random words.

## Constraints
- `n == stickers.length`
- `1 <= n <= 50`
- `1 <= stickers[i].length <= 10`
- `1 <= target.length <= 15`
- `stickers[i]` and `target` consist of lowercase English letters.

## Examples
### Example 1
- **Input:** `stickers = ["with","example","science"], target = "thehat"`
- **Output:** `3`
- **Explanation:** We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.

### Example 2
- **Input:** `stickers = ["notice","possible"], target = "basicbasic"`
- **Output:** `-1`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Stickers to Spell Word**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `stickers = ["with","example","science"], target = "thehat"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
/**
 * @param {string[]} stickers
 * @param {string} target
 * @return {number}
 */
var minStickers = function (stickers, target) {
  const m = target.length;
  const full = (1 << m) - 1;

  const counts = stickers.map((s) => {
    const c = new Array(26).fill(0);
    for (const ch of s) c[ch.charCodeAt(0) - 97]++;
    return c;
  });

  const dp = new Array(1 << m).fill(Infinity);
  dp[0] = 0;

  for (let mask = 0; mask < full; mask++) {
    if (dp[mask] === Infinity) continue;

    let p = 0;
    while (mask & (1 << p)) p++;
    const need = target.charCodeAt(p) - 97;

    for (const cnt of counts) {
      if (cnt[need] === 0) continue;

      const left = cnt.slice();
      let next = mask;
      for (let i = 0; i < m; i++) {
        if (next & (1 << i)) continue;
        const c = target.charCodeAt(i) - 97;
        if (left[c] > 0) {
          left[c]--;
          next |= 1 << i;
        }
      }
      if (dp[mask] + 1 < dp[next]) dp[next] = dp[mask] + 1;
    }
  }

  return dp[full] === Infinity ? -1 : dp[full];
};
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [58. Length of Last Word](../../0001-0500/0058-length-of-last-word/)
- [79. Word Search](../../0001-0500/0079-word-search/)
- [126. Word Ladder II](../../0001-0500/0126-word-ladder-ii/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/stickers-to-spell-word/)
