# LeetCode 1431: Kids With the Greatest Number of Candies

**LeetCode Problem #1431 — Kids With the Greatest Number of Candies**
Solve LeetCode Kids With the Greatest Number of Candies using JavaScript, Python and Math & Logic. This solution finds the optimal result using Mathematical Simulation & Modular Arithmetic in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Kids With the Greatest Number of Candies |
| LeetCode | #1431 |
| Difficulty | Easy |
| Language | JavaScript, Python |
| Algorithm | Mathematical Simulation & Modular Arithmetic |
| Data Structure | Primitive Types |
| Pattern | Math & Logic |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `i^th` kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return *a boolean array *`result`* of length *`n`*, where *`result[i]`* is *`true`* if, after giving the *`i^th`* kid all the *`extraCandies`*, they will have the **greatest** number of candies among all the kids**, or *`false`* otherwise*.

Note that **multiple** kids can have the **greatest** number of candies.

## Constraints
- `n == candies.length`
- `2 <= n <= 100`
- `1 <= candies[i] <= 100`
- `1 <= extraCandies <= 50`

## Examples
### Example 1
- **Input:** `candies = [2,3,5,1,3], extraCandies = 3`
- **Output:** `[true,true,true,false,true]`
- **Explanation:** If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

### Example 2
- **Input:** `candies = [4,2,1,1,2], extraCandies = 1`
- **Output:** `[true,false,false,false,false]`
- **Explanation:** There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

### Example 3
- **Input:** `candies = [12,1,12], extraCandies = 10`
- **Output:** `[true,false,true]`

## Key Insight
Leverage **Math & Logic** with **Primitive Types** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Kids With the Greatest Number of Candies**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `candies = [2,3,5,1,3], extraCandies = 3`.
2. **Processing Steps:** We apply **Mathematical Simulation & Modular Arithmetic** using our **Primitive Types**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[true,true,true,false,true]`.
4. **Verification:** If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Primitive Types.

## Pattern
**Math & Logic**

## Topics
- Math
- Simulation

## Language
JavaScript, Python

## Source Code
- [solution.js](./solution.js)
- [solution.py](./solution.py)


### JavaScript
```javascript
/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    const maxCandies = Math.max(...candies);

    return candies.map(candy => candy + extraCandies >= maxCandies);
};
```

### Python
```python
class Solution:
    def kidsWithCandies(
        self, candies: list[int], extraCandies: int
    ) -> list[bool]:
        maximum = max(candies)

        result = []

        for candy in candies:
            result.append(candy + extraCandies >= maximum)

        return result
```

## Why This Works
By utilizing **Math & Logic**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [575. Distribute Candies](../../0501-1000/0575-distribute-candies/)
- [1103. Distribute Candies to People](../../1001-1500/1103-distribute-candies-to-people/)
- [1298. Maximum Candies You Can Get from Boxes](../../1001-1500/1298-maximum-candies-you-can-get-from-boxes/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)
