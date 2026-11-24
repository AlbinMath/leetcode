# LeetCode 1018: Binary Prefix Divisible By 5

**LeetCode Problem #1018 — Binary Prefix Divisible By 5**
Solve LeetCode Binary Prefix Divisible By 5 using Python and Trie. This solution finds the optimal result using Prefix Tree Lookup in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Binary Prefix Divisible By 5 |
| LeetCode | #1018 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | Prefix Tree Lookup |
| Data Structure | Trie Node |
| Pattern | Trie |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given a binary array `nums` (**0-indexed**).

We define `x_i` as the number whose binary representation is the subarray `nums[0..i]` (from most-significant-bit to least-significant-bit).

For example, if `nums = [1,0,1]`, then `x_0 = 1`, `x_1 = 2`, and `x_2 = 5`.

Return *an array of booleans *`answer`* where *`answer[i]`* is *`true`* if *`x_i`* is divisible by *`5`.

## Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

## Examples
### Example 1
- **Input:** `nums = [0,1,1]`
- **Output:** `[true,false,false]`
- **Explanation:** The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.

### Example 2
- **Input:** `nums = [1,1,1]`
- **Output:** `[false,false,false]`

## Key Insight
Leverage **Trie** with **Trie Node** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Binary Prefix Divisible By 5**, we observe the problem requirements and utilize the **Trie** technique. We iterate through the inputs using **Prefix Tree Lookup**, leveraging a **Trie Node** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Trie Node**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [0,1,1]`.
2. **Processing Steps:** We apply **Prefix Tree Lookup** using our **Trie Node**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[true,false,false]`.
4. **Verification:** The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Trie Node.

## Pattern
**Trie**

## Topics
- Trie
- String
- Prefix Search

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        remainder = 0

        for num in nums:
            remainder = (remainder * 2 + num) % 5
            result.append(remainder == 0)

        return result
```

## Why This Works
By utilizing **Trie**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [14. Longest Common Prefix](../../0001-0500/0014-longest-common-prefix/)
- [208. Implement Trie (Prefix Tree)](../../0001-0500/0208-implement-trie-prefix-tree/)
- [745. Prefix and Suffix Search](../../0501-1000/0746-prefix-and-suffix-search/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/binary-prefix-divisible-by-5/)
