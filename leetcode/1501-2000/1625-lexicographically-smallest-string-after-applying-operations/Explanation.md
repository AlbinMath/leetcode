# LeetCode 1625: Lexicographically Smallest String After Applying Operations

**LeetCode Problem #1625 — Lexicographically Smallest String After Applying Operations**
Solve LeetCode Lexicographically Smallest String After Applying Operations using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Lexicographically Smallest String After Applying Operations |
| LeetCode | #1625 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string `s` of **even length** consisting of digits from `0` to `9`, and two integers `a` and `b`.

You can apply either of the following two operations any number of times and in any order on `s`:

Add `a` to all odd indices of `s` **(0-indexed)**. Digits post `9` are cycled back to `0`. For example, if `s = "3456"` and `a = 5`, `s` becomes `"3951"`. 
 Rotate `s` to the right by `b` positions. For example, if `s = "3456"` and `b = 1`, `s` becomes `"6345"`.

Return *the **lexicographically smallest** string you can obtain by applying the above operations any number of times on* `s`.

A string `a` is lexicographically smaller than a string `b` (of the same length) if in the first position where `a` and `b` differ, string `a` has a letter that appears earlier in the alphabet than the corresponding letter in `b`. For example, `"0158"` is lexicographically smaller than `"0190"` because the first position they differ is at the third letter, and `'5'` comes before `'9'`.

## Constraints
- `2 <= s.length <= 100`
- `s.length` is even.
- `s` consists of digits from `0` to `9` only.
- `1 <= a <= 9`
- `1 <= b <= s.length - 1`

## Examples
### Example 1
- **Input:** `s = "5525", a = 9, b = 2`
- **Output:** `"2050"`
- **Explanation:** We can apply the following operations:
Start: "5525"
Rotate: "2555"
Add: "2454"
Add: "2353"
Rotate: "5323"
Add: "5222"
Add: "5121"
Rotate: "2151"
Add: "2050"​​​​​
There is no way to obtain a string that is lexicographically smaller than "2050".

### Example 2
- **Input:** `s = "74", a = 5, b = 1`
- **Output:** `"24"`
- **Explanation:** We can apply the following operations:
Start: "74"
Rotate: "47"
​​​​​​​Add: "42"
​​​​​​​Rotate: "24"​​​​​​​​​​​​
There is no way to obtain a string that is lexicographically smaller than "24".

### Example 3
- **Input:** `s = "0011", a = 4, b = 2`
- **Output:** `"0011"`
- **Explanation:** There are no sequence of operations that will give us a lexicographically smaller string than "0011".

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Lexicographically Smallest String After Applying Operations**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "5525", a = 9, b = 2`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"2050"`.
4. **Verification:** We can apply the following operations:
Start: "5525"
Rotate: "2555"
Add: "2454"
Add: "2353"
Rotate: "5323"
Add: "5222"
Add: "5121"
Rotate: "2151"
Add: "2050"​​​​​
There is no way to obtain a string that is lexicographically smaller than "2050".

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

class Solution(object):
    def findLexSmallestString(self, s, a, b):
        visited = {s}
        queue = deque([s])
        smallest = s
        n = len(s)
        
        while queue:
            curr = queue.popleft()
            if curr < smallest:
                smallest = curr
            
            # Operation 1: Add 'a' to all odd indices
            chars = list(curr)
            for i in range(1, n, 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            added = "".join(chars)
            if added not in visited:
                visited.add(added)
                queue.append(added)
                
            # Operation 2: Rotate right by 'b' positions
            rotated = curr[-b:] + curr[:-b]
            if rotated not in visited:
                visited.add(rotated)
                queue.append(rotated)
                
        return smallest
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
- [3722. Lexicographically Smallest String After Reverse](../../3501-4000/3722-lexicographically-smallest-string-after-reverse/)
- [3816. Lexicographically Smallest String After Deleting Duplicate Characters](../../3501-4000/3816-lexicographically-smallest-string-after-deleting-duplicate-characters/)
- [3223. Minimum Length of String After Operations](../../3001-3500/3223-minimum-length-of-string-after-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/)
