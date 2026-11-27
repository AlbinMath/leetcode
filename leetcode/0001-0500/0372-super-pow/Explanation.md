# LeetCode 372: Super Pow

**LeetCode Problem #372 — Super Pow**
Solve LeetCode Super Pow using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Super Pow |
| LeetCode | #372 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Your task is to calculate `a^b` mod `1337` where `a` is a positive integer and `b` is an extremely large positive integer given in the form of an array.

## Constraints
- `1 <= a <= 2^31 - 1`
- `1 <= b.length <= 2000`
- `0 <= b[i] <= 9`
- `b` does not contain leading zeros.

## Examples
### Example 1
- **Input:** `a = 2, b = [3]`
- **Output:** `8`
- **Explanation:** The array `b = [3]` represents the exponent 3. Therefore, `a^3 = 2^3 = 8`, so the result is 8.

### Example 2
- **Input:** `a = 2, b = [1,0]`
- **Output:** `1024`
- **Explanation:** The array `b = [1, 0]` represents the exponent 10. Therefore, `a^10 = 2^10 = 1024`, so the result is 1024.

### Example 3
- **Input:** `a = 1, b = [4,3,3,8,5,2]`
- **Output:** `1`
- **Explanation:** The array `b = [4, 3, 3, 8, 5, 2]` represents a positive exponent. Since `a = 1`, any positive power of 1 is 1. Therefore, the result is 1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Super Pow**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `a = 2, b = [3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `8`.
4. **Verification:** The array `b = [3]` represents the exponent 3. Therefore, `a^3 = 2^3 = 8`, so the result is 8.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        a %= MOD
        res = 1
        for d in b:
            res = pow(res, 10, MOD) * pow(a, d, MOD) % MOD
        return res
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [313. Super Ugly Number](../../0001-0500/0313-super-ugly-number/)
- [517. Super Washing Machines](../../0501-1000/0517-super-washing-machines/)
- [887. Super Egg Drop](../../0501-1000/0887-super-egg-drop/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/super-pow/)
