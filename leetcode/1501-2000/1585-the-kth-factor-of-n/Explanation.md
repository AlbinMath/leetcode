# LeetCode 1492: The kth Factor of n

**LeetCode Problem #1492 — The kth Factor of n**
Solve LeetCode The kth Factor of n using Kotlin, Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | The kth Factor of n |
| LeetCode | #1492 |
| Difficulty | Medium |
| Language | Kotlin, Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two positive integers `n` and `k`. A factor of an integer `n` is defined as an integer `i` where `n % i == 0`.

Consider a list of all factors of `n` sorted in **ascending order**, return *the *`k^th`* factor* in this list or return `-1` if `n` has less than `k` factors.

## Constraints
- `1 <= k <= n <= 1000`

## Examples
### Example 1
- **Input:** `n = 12, k = 3`
- **Output:** `3`
- **Explanation:** Factors list is [1, 2, 3, 4, 6, 12], the 3^rd factor is 3.

### Example 2
- **Input:** `n = 7, k = 2`
- **Output:** `7`
- **Explanation:** Factors list is [1, 7], the 2^nd factor is 7.

### Example 3
- **Input:** `n = 4, k = 4`
- **Output:** `-1`
- **Explanation:** Factors list is [1, 2, 4], there is only 3 factors. We should return -1.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **The kth Factor of n**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 12, k = 3`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Factors list is [1, 2, 3, 4, 6, 12], the 3^rd factor is 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
Kotlin, Python

## Source Code
- [solution.kt](./solution.kt)
- [solution.py](./solution.py)


### Kotlin
```kotlin
class Solution {
    fun kthFactor(n: Int, k: Int): Int {
        var count = 0
        for (i in 1..n) {
            if (n % i == 0 && ++count == k) return i
        }
        return -1
    }
}
```

### Python
```python
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        small = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                small.append(i)
            i += 1

        # k falls among the small factors
        if k <= len(small):
            return small[k - 1]

        # otherwise it is among the large partners, in reverse order
        large = [n // d for d in reversed(small)]
        if small and small[-1] * small[-1] == n:
            large = large[1:]            # drop the duplicated square root
        k -= len(small)
        return large[k - 1] if k <= len(large) else -1
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
- [952. Largest Component Size by Common Factor](../../0501-1000/0989-largest-component-size-by-common-factor/)
- [3334. Find the Maximum Factor Score of Array](../../3501-4000/3593-find-the-maximum-factor-score-of-array/)
- [3605. Minimum Stability Factor of Array](../../3501-4000/3920-minimum-stability-factor-of-array/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/the-kth-factor-of-n/)
