# LeetCode 888: Fair Candy Swap

**LeetCode Problem #888 — Fair Candy Swap**
Solve LeetCode Fair Candy Swap using Python and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Fair Candy Swap |
| LeetCode | #888 |
| Difficulty | Easy |
| Language | Python |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Alice and Bob have a different total number of candies. You are given two integer arrays `aliceSizes` and `bobSizes` where `aliceSizes[i]` is the number of candies of the `i^th` box of candy that Alice has and `bobSizes[j]` is the number of candies of the `j^th` box of candy that Bob has.

Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the same total amount of candy. The total amount of candy a person has is the sum of the number of candies in each box they have.

Return a*n integer array *`answer`* where *`answer[0]`* is the number of candies in the box that Alice must exchange, and *`answer[1]`* is the number of candies in the box that Bob must exchange*. If there are multiple answers, you may **return any** one of them. It is guaranteed that at least one answer exists.

## Constraints
- `1 <= aliceSizes.length, bobSizes.length <= 10^4`
- `1 <= aliceSizes[i], bobSizes[j] <= 10^5`
- Alice and Bob have a different total number of candies.
- There will be at least one valid answer for the given input.

## Examples
### Example 1
- **Input:** `aliceSizes = [1,1], bobSizes = [2,2]`
- **Output:** `[1,2]`

### Example 2
- **Input:** `aliceSizes = [1,2], bobSizes = [2,3]`
- **Output:** `[1,2]`

### Example 3
- **Input:** `aliceSizes = [2], bobSizes = [1,3]`
- **Output:** `[2,3]`

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Fair Candy Swap**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `aliceSizes = [1,1], bobSizes = [2,2]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[1,2]`.

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
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)

        diff = (alice_sum - bob_sum) // 2
        bob_set = set(bobSizes)

        for a in aliceSizes:
            b = a - diff
            if b in bob_set:
                return [a, b]

        return []
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
- [1664. Ways to Make a Fair Array](../../1501-2000/1783-ways-to-make-a-fair-array/)
- [2305. Fair Distribution of Cookies](../../1001-1500/1418-fair-distribution-of-cookies/)
- [135. Candy](../../0001-0500/0135-candy/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/fair-candy-swap/)
