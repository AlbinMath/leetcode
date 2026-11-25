# LeetCode 3666: Minimum Operations to Equalize Binary String

**LeetCode Problem #3666 — Minimum Operations to Equalize Binary String**
Solve LeetCode Minimum Operations to Equalize Binary String using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Operations to Equalize Binary String |
| LeetCode | #3666 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a binary string `s`, and an integer `k`.

In one operation, you must choose **exactly** `k` **different** indices and **flip** each `'0'` to `'1'` and each `'1'` to `'0'`.

Return the **minimum** number of operations required to make all characters in the string equal to `'1'`. If it is not possible, return -1.

## Constraints
- `1 <= s.length <= 10^​​​​​​​5`
- `s[i]` is either `'0'` or `'1'`.
- `1 <= k <= s.length`

## Examples
### Example 1
- **Input:** `s = "110", k = 1`
- **Output:** `1`
- **Explanation:** There is one `'0'` in `s`. 
 Since `k = 1`, we can flip it directly in one operation.

### Example 2
- **Input:** `s = "0101", k = 3`
- **Output:** `2`
- **Explanation:** One optimal set of operations choosing `k = 3` indices in each operation is:

### Example 3
- **Input:** `s = "101", k = 2`
- **Output:** `-1`
- **Explanation:** Since `k = 2` and `s` has only one `'0'`, it is impossible to flip exactly `k` indices to make all `'1'`. Hence, the answer is -1.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Operations to Equalize Binary String**, we observe the problem requirements and utilize the **Tree & Graph** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "110", k = 1`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** There is one `'0'` in `s`. 
 Since `k = 1`, we can flip it directly in one operation.

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
from collections import deque

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        cnt0 = s.count('0')
        if cnt0 == 0:
            return 0

        # parent[i] points to the next unvisited integer of the same parity >= i
        parent = list(range(n + 3))

        def find(x: int) -> int:
            path = []
            while parent[x] != x:
                path.append(x)
                x = parent[x]
            for node in path:
                parent[node] = x
            return x

        def remove(x: int):
            parent[x] = find(x + 2)

        # Remove the initial state
        remove(cnt0)

        queue = deque([(cnt0, 0)])

        while queue:
            cur, dist = queue.popleft()

            # Bound x (the number of 0s flipped to 1s)
            x_min = max(0, k - n + cur)
            x_max = min(cur, k)

            l = cur + k - 2 * x_max
            r = cur + k - 2 * x_min

            # Search in the range [l, r] with parity matching (cur + k) % 2
            nxt = find(l)
            while nxt <= r:
                if nxt == 0:
                    return dist + 1
                queue.append((nxt, dist + 1))
                remove(nxt)
                nxt = find(nxt)

        return -1
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
- [3674. Minimum Operations to Equalize Array](../../3501-4000/3674-minimum-operations-to-equalize-array/)
- [3762. Minimum Operations to Equalize Subarrays](../../3501-4000/3762-minimum-operations-to-equalize-subarrays/)
- [1830. Minimum Number of Operations to Make String Sorted](../../1501-2000/1830-minimum-number-of-operations-to-make-string-sorted/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/)
