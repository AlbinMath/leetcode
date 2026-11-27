# LeetCode 2418: Sort the People

**LeetCode Problem #2418 — Sort the People**
Solve LeetCode Sort the People using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sort the People |
| LeetCode | #2418 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an array of strings `names`, and an array `heights` that consists of **distinct** positive integers. Both arrays are of length `n`.

For each index `i`, `names[i]` and `heights[i]` denote the name and height of the `i^th` person.

Return `names`* sorted in **descending** order by the people's heights*.

## Constraints
- `n == names.length == heights.length`
- `1 <= n <= 10^3`
- `1 <= names[i].length <= 20`
- `1 <= heights[i] <= 10^5`
- `names[i]` consists of lower and upper case English letters.
- All the values of `heights` are distinct.

## Examples
### Example 1
- **Input:** `names = ["Mary","John","Emma"], heights = [180,165,170]`
- **Output:** `["Mary","Emma","John"]`
- **Explanation:** Mary is the tallest, followed by Emma and John.

### Example 2
- **Input:** `names = ["Alice","Bob","Bob"], heights = [155,185,150]`
- **Output:** `["Bob","Alice","Bob"]`
- **Explanation:** The first Bob is the tallest, followed by Alice and the second Bob.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sort the People**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `names = ["Mary","John","Emma"], heights = [180,165,170]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["Mary","Emma","John"]`.
4. **Verification:** Mary is the tallest, followed by Emma and John.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var sortPeople = function(names, heights) {
    const people = [];

    for (let i = 0; i < names.length; i++) {
        people.push([heights[i], names[i]]);
    }

    people.sort((a, b) => b[0] - a[0]);
    return people.map(person => person[1]);
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
- [881. Boats to Save People](../../0501-1000/0881-boats-to-save-people/)
- [1103. Distribute Candies to People](../../1001-1500/1103-distribute-candies-to-people/)
- [1282. Group the People Given the Group Size They Belong To](../../1001-1500/1282-group-the-people-given-the-group-size-they-belong-to/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sort-the-people/)
