# LeetCode 842: Split Array into Fibonacci Sequence

**LeetCode Problem #842 — Split Array into Fibonacci Sequence**
Solve LeetCode Split Array into Fibonacci Sequence using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Split Array into Fibonacci Sequence |
| LeetCode | #842 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a string of digits `num`, such as `"123456579"`. We can split it into a Fibonacci-like sequence `[123, 456, 579]`.

Formally, a **Fibonacci-like** sequence is a list `f` of non-negative integers such that:

`0 <= f[i] < 2^31`, (that is, each integer fits in a **32-bit** signed integer type), 
 `f.length >= 3`, and 
 `f[i] + f[i + 1] == f[i + 2]` for all `0 <= i < f.length - 2`.

Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number `0` itself.

Return any Fibonacci-like sequence split from `num`, or return `[]` if it cannot be done.

## Constraints
- `1 <= num.length <= 200`
- `num` contains only digits.

## Examples
### Example 1
- **Input:** `num = "1101111"`
- **Output:** `[11,0,11,11]`
- **Explanation:** The output [110, 1, 111] would also be accepted.

### Example 2
- **Input:** `num = "112358130"`
- **Output:** `[]`
- **Explanation:** The task is impossible.

### Example 3
- **Input:** `num = "0123"`
- **Output:** `[]`
- **Explanation:** Leading zeroes are not allowed, so "01", "2", "3" is not valid.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Split Array into Fibonacci Sequence**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `num = "1101111"`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[11,0,11,11]`.
4. **Verification:** The output [110, 1, 111] would also be accepted.

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
from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)
        LIMIT = 2**31

        for i in range(1, min(11, n)):          # length of first number
            if i > 1 and num[0] == "0":
                break                            # leading zero, longer prefixes fail too
            a = int(num[:i])
            if a >= LIMIT:
                break
            for j in range(1, min(11, n - i)):   # length of second number
                if j > 1 and num[i] == "0":
                    break
                b = int(num[i:i + j])
                if b >= LIMIT:
                    break

                seq = [a, b]
                pos = i + j
                x, y = a, b
                while pos < n:
                    z = x + y
                    if z >= LIMIT:
                        break
                    s = str(z)
                    if not num.startswith(s, pos):
                        break
                    seq.append(z)
                    pos += len(s)
                    x, y = y, z
                if pos == n and len(seq) >= 3:
                    return seq
        return []
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
- [2871. Split Array Into Maximum Number of Subarrays](../../2501-3000/2871-split-array-into-maximum-number-of-subarrays/)
- [2648. Generate Fibonacci Sequence](../../2501-3000/2648-generate-fibonacci-sequence/)
- [1593. Split a String Into the Max Number of Unique Substrings](../../1501-2000/1593-split-a-string-into-the-max-number-of-unique-substrings/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/split-array-into-fibonacci-sequence/)
