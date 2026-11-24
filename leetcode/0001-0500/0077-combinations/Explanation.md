# LeetCode 77: Combinations

**LeetCode Problem #77 — Combinations**
Solve LeetCode Combinations using PHP, Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Combinations |
| LeetCode | #77 |
| Difficulty | Medium |
| Language | PHP, Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integers `n` and `k`, return *all possible combinations of* `k` *numbers chosen from the range* `[1, n]`.

You may return the answer in **any order**.

## Constraints
- `1 <= n <= 20`
- `1 <= k <= n`

## Examples
### Example 1
- **Input:** `n = 4, k = 2`
- **Output:** `[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]`
- **Explanation:** There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

### Example 2
- **Input:** `n = 1, k = 1`
- **Output:** `[[1]]`
- **Explanation:** There is 1 choose 1 = 1 total combination.

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Combinations**, we observe the problem requirements and utilize the **Backtracking** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 4, k = 2`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]`.
4. **Verification:** There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
PHP, Python

## Source Code
- [solution.php](./solution.php)
- [solution.py](./solution.py)


### PHP
```php
class Solution {
    function combine($n, $k) {
        $result = [];
        $current = [];

        $this->backtrack(1, $n, $k, $current, $result);

        return $result;
    }

    function backtrack($start, $n, $k, &$current, &$result) {
        // Combination is complete
        if (count($current) == $k) {
            $result[] = $current;
            return;
        }

        for ($i = $start; $i <= $n; $i++) {
            // Choose
            $current[] = $i;

            // Explore
            $this->backtrack(
                $i + 1,
                $n,
                $k,
                $current,
                $result
            );

            // Backtrack
            array_pop($current);
        }
    }
}
```

### Python
```python
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return res
```

## Why This Works
By utilizing **Backtracking**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [17. Letter Combinations of a Phone Number](../../0001-0500/0017-letter-combinations-of-a-phone-number/)
- [2056. Number of Valid Move Combinations On Chessboard](../../2001-2500/2056-number-of-valid-move-combinations-on-chessboard/)
- [22. Generate Parentheses](../../0001-0500/0022-generate-parentheses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/combinations/)
