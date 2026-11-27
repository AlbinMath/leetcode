# LeetCode 1869: Longer Contiguous Segments of Ones than Zeros

**LeetCode Problem #1869 — Longer Contiguous Segments of Ones than Zeros**
Solve LeetCode Longer Contiguous Segments of Ones than Zeros using C++ and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Longer Contiguous Segments of Ones than Zeros |
| LeetCode | #1869 |
| Difficulty | Easy |
| Language | C++ |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a binary string `s`, return `true`* if the **longest** contiguous segment of *`1`'*s is **strictly longer** than the **longest** contiguous segment of *`0`'*s in *`s`, or return `false`* otherwise*.

For example, in `s = " 11 01 000 10"` the longest continuous segment of `1`s has length `2`, and the longest continuous segment of `0`s has length `3`.

Note that if there are no `0`'s, then the longest continuous segment of `0`'s is considered to have a length `0`. The same applies if there is no `1`'s.

## Constraints
- `1 <= s.length <= 100`
- `s[i]` is either `'0'` or `'1'`.

## Examples
### Example 1
- **Input:** `s = "1101"`
- **Output:** `true`
- **Explanation:** The longest contiguous segment of 1s has length 2: " 11 01"
The longest contiguous segment of 0s has length 1: "11 0 1"
The segment of 1s is longer, so return true.

### Example 2
- **Input:** `s = "111000"`
- **Output:** `false`
- **Explanation:** The longest contiguous segment of 1s has length 3: " 111 000"
The longest contiguous segment of 0s has length 3: "111 000 "
The segment of 1s is not longer, so return false.

### Example 3
- **Input:** `s = "110100010"`
- **Output:** `false`
- **Explanation:** The longest contiguous segment of 1s has length 2: " 11 0100010"
The longest contiguous segment of 0s has length 3: "1101 000 10"
The segment of 1s is not longer, so return false.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Longer Contiguous Segments of Ones than Zeros**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `s = "1101"`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** The longest contiguous segment of 1s has length 2: " 11 01"
The longest contiguous segment of 0s has length 1: "11 0 1"
The segment of 1s is longer, so return true.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    bool checkZeroOnes(string s) {
        int maxOnes = 0, maxZeros = 0;
        int currentOnes = 0, currentZeros = 0;

        for (char c : s) {
            if (c == '1') {
                currentOnes++;
                currentZeros = 0;
                maxOnes = max(maxOnes, currentOnes);
            } else {
                currentZeros++;
                currentOnes = 0;
                maxZeros = max(maxZeros, currentZeros);
            }
        }

        return maxOnes > maxZeros;
    }
};
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
- [2482. Difference Between Ones and Zeros in Row and Column](../../2001-2500/2482-difference-between-ones-and-zeros-in-row-and-column/)
- [474. Ones and Zeroes](../../0001-0500/0474-ones-and-zeroes/)
- [485. Max Consecutive Ones](../../0001-0500/0485-max-consecutive-ones/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/)
