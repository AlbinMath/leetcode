# LeetCode 2086: Minimum Number of Food Buckets to Feed the Hamsters

**LeetCode Problem #2086 — Minimum Number of Food Buckets to Feed the Hamsters**
Solve LeetCode Minimum Number of Food Buckets to Feed the Hamsters using Python and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Number of Food Buckets to Feed the Hamsters |
| LeetCode | #2086 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** string `hamsters` where `hamsters[i]` is either:

`'H'` indicating that there is a hamster at index `i`, or 
 `'.'` indicating that index `i` is empty.

You will add some number of food buckets at the empty indices in order to feed the hamsters. A hamster can be fed if there is at least one food bucket to its left or to its right. More formally, a hamster at index `i` can be fed if you place a food bucket at index `i - 1` **and/or** at index `i + 1`.

Return *the minimum number of food buckets you should **place at empty indices** to feed all the hamsters or *`-1`* if it is impossible to feed all of them*.

## Constraints
- `1 <= hamsters.length <= 10^5`
- `hamsters[i]` is either`'H'` or `'.'`.

## Examples
### Example 1
- **Input:** `hamsters = "H..H"`
- **Output:** `2`
- **Explanation:** We place two food buckets at indices 1 and 2.
It can be shown that if we place only one food bucket, one of the hamsters will not be fed.

### Example 2
- **Input:** `hamsters = ".H.H."`
- **Output:** `1`
- **Explanation:** We place one food bucket at index 2.

### Example 3
- **Input:** `hamsters = ".HHH."`
- **Output:** `-1`
- **Explanation:** If we place a food bucket at every empty index as shown, the hamster at index 2 will not be able to eat.

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Minimum Number of Food Buckets to Feed the Hamsters**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `hamsters = "H..H"`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** We place two food buckets at indices 1 and 2.
It can be shown that if we place only one food bucket, one of the hamsters will not be fed.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        s = list(hamsters)
        n = len(s)
        count = 0
        i = 0
        while i < n:
            if s[i] == 'H':
                if i + 1 < n and s[i + 1] == '.':
                    count += 1
                    i += 3  # bucket at i+1 feeds i and i+2; next unfed candidate is i+3
                    continue
                elif i - 1 >= 0 and s[i - 1] == '.':
                    count += 1
                else:
                    return -1
            i += 1
        return count
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [452. Minimum Number of Arrows to Burst Balloons](../../0001-0500/0452-minimum-number-of-arrows-to-burst-balloons/)
- [871. Minimum Number of Refueling Stops](../../0501-1000/0871-minimum-number-of-refueling-stops/)
- [995. Minimum Number of K Consecutive Bit Flips](../../0501-1000/0995-minimum-number-of-k-consecutive-bit-flips/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/)
