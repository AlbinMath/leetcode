# LeetCode 519: Random Flip Matrix

**LeetCode Problem #519 — Random Flip Matrix**
Solve LeetCode Random Flip Matrix using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Random Flip Matrix |
| LeetCode | #519 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There is an `m x n` binary grid `matrix` with all the values set `0` initially. Design an algorithm to randomly pick an index `(i, j)` where `matrix[i][j] == 0` and flips it to `1`. All the indices `(i, j)` where `matrix[i][j] == 0` should be equally likely to be returned.

Optimize your algorithm to minimize the number of calls made to the **built-in** random function of your language and optimize the time and space complexity.

Implement the `Solution` class:

`Solution(int m, int n)` Initializes the object with the size of the binary matrix `m` and `n`. 
 `int[] flip()` Returns a random index `[i, j]` of the matrix where `matrix[i][j] == 0` and flips it to `1`. 
 `void reset()` Resets all the values of the matrix to be `0`.

## Constraints
- `1 <= m, n <= 10^4`
- There will be at least one free cell for each call to `flip`.
- At most `1000` calls will be made to `flip` and `reset`.

## Examples
### Example 1
- **Input:** `["Solution", "flip", "flip", "flip", "reset", "flip"]
[[3, 1], [], [], [], [], []]`
- **Output:** `[null, [1, 0], [2, 0], [0, 0], null, [2, 0]]`
- **Explanation:** Solution solution = new Solution(3, 1);
solution.flip(); // return [1, 0], [0,0], [1,0], and [2,0] should be equally likely to be returned.
solution.flip(); // return [2, 0], Since [1,0] was returned, [2,0] and [0,0]
solution.flip(); // return [0, 0], Based on the previously returned indices, only [0,0] can be returned.
solution.reset(); // All the values are reset to 0 and can be returned.
solution.flip(); // return [2, 0], [0,0], [1,0], and [2,0] should be equally likely to be returned.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Random Flip Matrix**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["Solution", "flip", "flip", "flip", "reset", "flip"]
[[3, 1], [], [], [], [], []]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, [1, 0], [2, 0], [0, 0], null, [2, 0]]`.
4. **Verification:** Solution solution = new Solution(3, 1);
solution.flip(); // return [1, 0], [0,0], [1,0], and [2,0] should be equally likely to be returned.
solution.flip(); // return [2, 0], Since [1,0] was returned, [2,0] and [0,0]
solution.flip(); // return [0, 0], Based on the previously returned indices, only [0,0] can be returned.
solution.reset(); // All the values are reset to 0 and can be returned.
solution.flip(); // return [2, 0], [0,0], [1,0], and [2,0] should be equally likely to be returned.

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
Python

## Source Code
- [solution.py](./solution.py)


```python
import random

class Solution(object):

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.total = m * n
        self.rem = self.total
        self.flipped = {}

    def flip(self):
        r = random.randint(0, self.rem - 1)
        self.rem -= 1
        
        actual = self.flipped.get(r, r)
        self.flipped[r] = self.flipped.get(self.rem, self.rem)
        
        return [actual // self.n, actual % self.n]

    def reset(self):
        self.rem = self.total
        self.flipped.clear()
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
- [2556. Disconnect Path in a Binary Matrix by at Most One Flip](../../2501-3000/2641-disconnect-path-in-a-binary-matrix-by-at-most-one-flip/)
- [926. Flip String to Monotone Increasing](../../0501-1000/0962-flip-string-to-monotone-increasing/)
- [951. Flip Equivalent Binary Trees](../../0501-1000/0988-flip-equivalent-binary-trees/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/random-flip-matrix/)
