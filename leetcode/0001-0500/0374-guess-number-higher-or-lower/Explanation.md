# LeetCode 374: Guess Number Higher or Lower

**LeetCode Problem #374 — Guess Number Higher or Lower**
Solve LeetCode Guess Number Higher or Lower using JavaScript, Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Guess Number Higher or Lower |
| LeetCode | #374 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
We are playing the Guess Game. The game is as follows:

I pick a number from `1` to `n`. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API `int guess(int num)`, which returns three possible results:

`-1`: Your guess is higher than the number I picked (i.e. `num > pick`). 
 `1`: Your guess is lower than the number I picked (i.e. `num < pick`). 
 `0`: your guess is equal to the number I picked (i.e. `num == pick`).

Return *the number that I picked*.

## Constraints
- `1 <= n <= 2^31 - 1`
- `1 <= pick <= n`

## Examples
### Example 1
- **Input:** `n = 10, pick = 6`
- **Output:** `6`

### Example 2
- **Input:** `n = 1, pick = 1`
- **Output:** `1`

### Example 3
- **Input:** `n = 2, pick = 1`
- **Output:** `1`

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Guess Number Higher or Lower**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 10, pick = 6`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `6`.

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
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
/**
 * @param {number} n
 * @return {number}
 */
var guessNumber = function(n) {
    let left = 1;
    let right = n;

    while (left <= right) {
        const mid = left + Math.floor((right - left) / 2);
        const result = guess(mid);

        if (result === 0) {
            return mid;
        } else if (result === -1) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
};
```

### Python
```python
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          0 if num is equal to the picked number

class Solution:
    def guessNumber(self, n):
        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2

            result = guess(mid)

            if result == 0:
                return mid

            elif result == -1:
                # Our guess is too high
                right = mid - 1

            else:
                # Our guess is too low
                left = mid + 1
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
- [375. Guess Number Higher or Lower II](../../0001-0500/0375-guess-number-higher-or-lower-ii/)
- [843. Guess the Word](../../0501-1000/0843-guess-the-word/)
- [709. To Lower Case](../../0501-1000/0709-to-lower-case/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/guess-number-higher-or-lower/)
