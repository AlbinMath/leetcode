# LeetCode 1497: Check If Array Pairs Are Divisible by k

**LeetCode Problem #1497 — Check If Array Pairs Are Divisible by k**
Solve LeetCode Check If Array Pairs Are Divisible by k using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Check If Array Pairs Are Divisible by k |
| LeetCode | #1497 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given an array of integers `arr` of even length `n` and an integer `k`.

We want to divide the array into exactly `n / 2` pairs such that the sum of each pair is divisible by `k`.

Return `true`* If you can find a way to do that or *`false`* otherwise*.

## Constraints
- `arr.length == n`
- `1 <= n <= 10^5`
- `n` is even.
- `-10^9 <= arr[i] <= 10^9`
- `1 <= k <= 10^5`

## Examples
### Example 1
- **Input:** `arr = [1,2,3,4,5,10,6,7,8,9], k = 5`
- **Output:** `true`
- **Explanation:** Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

### Example 2
- **Input:** `arr = [1,2,3,4,5,6], k = 7`
- **Output:** `true`
- **Explanation:** Pairs are (1,6),(2,5) and(3,4).

### Example 3
- **Input:** `arr = [1,2,3,4,5,6], k = 10`
- **Output:** `false`
- **Explanation:** You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Check If Array Pairs Are Divisible by k**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `arr = [1,2,3,4,5,10,6,7,8,9], k = 5`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).

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
class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        cnt = [0] * k
        for x in arr:
            cnt[x % k] += 1
        if cnt[0] % 2:
            return False
        for r in range(1, k // 2 + 1):
            if r == k - r:
                if cnt[r] % 2:
                    return False
            elif cnt[r] != cnt[k - r]:
                return False
        return True
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
- [2183. Count Array Pairs Divisible by K](../../2001-2500/2183-count-array-pairs-divisible-by-k/)
- [1437. Check If All 1's Are at Least Length K Places Away](../../1001-1500/1437-check-if-all-1s-are-at-least-length-k-places-away/)
- [1662. Check If Two String Arrays are Equivalent](../../1501-2000/1662-check-if-two-string-arrays-are-equivalent/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/)
