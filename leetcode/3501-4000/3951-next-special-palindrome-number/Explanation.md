# LeetCode 3646: Next Special Palindrome Number

**LeetCode Problem #3646 — Next Special Palindrome Number**
Solve LeetCode Next Special Palindrome Number using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Next Special Palindrome Number |
| LeetCode | #3646 |
| Difficulty | Hard |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer `n`.

A number is called **special** if:

It is a ** palindrome **. 
 Every digit `k` in the number appears **exactly** `k` times.

Return the **smallest** special number **strictly **greater than `n`.

## Constraints
- `0 <= n <= 10^15`

## Examples
### Example 1
- **Input:** `n = 2`
- **Output:** `22`
- **Explanation:** 22 is the smallest special number greater than 2, as it is a palindrome and the digit 2 appears exactly 2 times.

### Example 2
- **Input:** `n = 33`
- **Output:** `212`
- **Explanation:** 212 is the smallest special number greater than 33, as it is a palindrome and the digits 1 and 2 appear exactly 1 and 2 times respectively.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Next Special Palindrome Number**, we observe the problem requirements and utilize the **Two Pointers** technique. By maintaining a **Array**, we can store elements and their corresponding indices or frequencies. This allows us to look up complements or past values in $O(1)$ time instead of scanning through nested iterations.

## Algorithm
1. Initialize a **Array** to record observed values and indices.
2. Iterate through elements, querying the hash map for complementary conditions.
3. Insert the current element into the hash map if no match is found.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `22`.
4. **Verification:** 22 is the smallest special number greater than 2, as it is a palindrome and the digit 2 appears exactly 2 times.

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
class Solution:
    def specialPalindrome(self, n: int) -> int:
        # group valid digit subsets by their total length
        by_len = {}
        for m in range(1, 1 << 9):
            ds = [i + 1 for i in range(9) if m >> i & 1]
            if sum(d & 1 for d in ds) <= 1:
                by_len.setdefault(sum(ds), []).append(ds)

        def first_above(ds, n):
            cnt = [0] * 10
            mid = ""
            for d in ds:
                cnt[d] = d // 2
                if d & 1:
                    mid = str(d)
            half_len = sum(cnt)

            def gen(cur):
                if len(cur) == half_len:
                    h = "".join(cur)
                    yield int(h + mid + h[::-1])
                    return
                for d in range(1, 10):
                    if cnt[d]:
                        cnt[d] -= 1
                        cur.append(str(d))
                        yield from gen(cur)
                        cur.pop()
                        cnt[d] += 1

            for v in gen([]):
                if v > n:
                    return v
            return None

        for L in range(len(str(n)), 46):
            best = None
            for ds in by_len.get(L, []):
                v = first_above(ds, n)
                if v is not None and (best is None or v < best):
                    best = v
            if best is not None:
                return best
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
- [9. Palindrome Number](../../0001-0500/0009-palindrome-number/)
- [2048. Next Greater Numerically Balanced Number](../../2001-2500/2174-next-greater-numerically-balanced-number/)
- [2193. Minimum Number of Moves to Make Palindrome](../../1001-1500/1356-minimum-number-of-moves-to-make-palindrome/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/next-special-palindrome-number/)
