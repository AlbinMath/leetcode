# LeetCode 93: Restore IP Addresses

**LeetCode Problem #93 — Restore IP Addresses**
Solve LeetCode Restore IP Addresses using JavaScript, Python and Backtracking. This solution finds the optimal result using Backtracking Recursive Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Restore IP Addresses |
| LeetCode | #93 |
| Difficulty | Medium |
| Language | JavaScript, Python |
| Algorithm | Backtracking Recursive Search |
| Data Structure | Recursion Tree |
| Pattern | Backtracking |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A **valid IP address** consists of exactly four integers separated by single dots. Each integer is between `0` and `255` (**inclusive**) and cannot have leading zeros.

For example, `"0.1.2.201"` and `"192.168.1.1"` are **valid** IP addresses, but `"0.011.255.245"`, `"192.168.1.312"` and `"192.168@1.1"` are **invalid** IP addresses.

Given a string `s` containing only digits, return *all possible valid IP addresses that can be formed by inserting dots into *`s`. You are **not** allowed to reorder or remove any digits in `s`. You may return the valid IP addresses in **any** order.

## Constraints
- `1 <= s.length <= 20`
- `s` consists of digits only.

## Examples
### Example 1
- **Input:** `s = "25525511135"`
- **Output:** `["255.255.11.135","255.255.111.35"]`

### Example 2
- **Input:** `s = "0000"`
- **Output:** `["0.0.0.0"]`

### Example 3
- **Input:** `s = "101023"`
- **Output:** `["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]`

## Key Insight
Leverage **Backtracking** with **Recursion Tree** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Restore IP Addresses**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "25525511135"`.
2. **Processing Steps:** We apply **Backtracking Recursive Search** using our **Recursion Tree**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["255.255.11.135","255.255.111.35"]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Recursion Tree.

## Pattern
**Backtracking**

## Topics
- Backtracking
- Recursion

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
var restoreIpAddresses = function(s) {
    const result = [];

    function backtrack(start, parts) {
        // A valid IP must have exactly four parts
        if (parts.length === 4) {
            if (start === s.length) {
                result.push(parts.join("."));
            }
            return;
        }

        // Try segments of length 1, 2, and 3
        for (let len = 1; len <= 3; len++) {
            if (start + len > s.length) break;

            const segment = s.substring(start, start + len);

            // Reject leading zeros
            if (segment.length > 1 && segment[0] === "0") {
                continue;
            }

            const value = Number(segment);

            // Each segment must be between 0 and 255
            if (value > 255) continue;

            parts.push(segment);
            backtrack(start + len, parts);
            parts.pop();
        }
    }

    backtrack(0, []);
    return result;
};
```

### Python
```python
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(i, parts):
            if len(parts) == 4:
                if i == len(s):
                    res.append(".".join(parts))
                return

            for j in range(i + 1, min(i + 4, len(s) + 1)):
                part = s[i:j]
                if (len(part) > 1 and part[0] == '0') or int(part) > 255:
                    continue
                backtrack(j, parts + [part])

        backtrack(0, [])
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
- [3451. Find Invalid IP Addresses](../../3001-3500/3451-find-invalid-ip-addresses/)
- [1416. Restore The Array](../../1001-1500/1416-restore-the-array/)
- [929. Unique Email Addresses](../../0501-1000/0929-unique-email-addresses/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/restore-ip-addresses/)
