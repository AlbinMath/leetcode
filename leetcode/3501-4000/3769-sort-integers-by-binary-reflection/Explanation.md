# LeetCode 3769: Sort Integers by Binary Reflection

**LeetCode Problem #3769 — Sort Integers by Binary Reflection**
Solve LeetCode Sort Integers by Binary Reflection using JavaScript and Tree & Graph. This solution finds the optimal result using Depth-First Search (DFS) / Breadth-First Search (BFS) in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Sort Integers by Binary Reflection |
| LeetCode | #3769 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | Depth-First Search (DFS) / Breadth-First Search (BFS) |
| Data Structure | Tree / Graph / Grid |
| Pattern | Tree & Graph |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums`.

The **binary reflection** of a **positive** integer is defined as the number obtained by reversing the order of its **binary** digits (ignoring any leading zeros) and interpreting the resulting binary number as a decimal.

Sort the array in **ascending** order based on the binary reflection of each element. If two different numbers have the same binary reflection, the **smaller** original number should appear first.

Return the resulting sorted array.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 10^9`

## Examples
### Example 1
- **Input:** `nums = [4,5,4]`
- **Output:** `[4,4,5]`
- **Explanation:** Binary reflections are: 

 
 4 -> (binary) `100` -> (reversed) `001` -> 1 
 5 -> (binary) `101` -> (reversed) `101` -> 5 
 4 -> (binary) `100` -> (reversed) `001` -> 1 
 
Sorting by the reflected values gives `[4, 4, 5]`.

### Example 2
- **Input:** `nums = [3,6,5,8]`
- **Output:** `[8,3,6,5]`
- **Explanation:** Binary reflections are: 

 
 3 -> (binary) `11` -> (reversed) `11` -> 3 
 6 -> (binary) `110` -> (reversed) `011` -> 3 
 5 -> (binary) `101` -> (reversed) `101` -> 5 
 8 -> (binary) `1000` -> (reversed) `0001` -> 1 
 
Sorting by the reflected values gives `[8, 3, 6, 5]`. 
Note that 3 and 6 have the same reflection, so we arrange them in increasing order of original value.

## Key Insight
Leverage **Tree & Graph** with **Tree / Graph / Grid** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Sort Integers by Binary Reflection**, we observe the problem requirements and utilize the **Bit Manipulation** technique. We employ bitwise operations (`&`, `|`, `^`, `~`, `<<`, `>>`) to directly manipulate bits in constant time without allocating dynamic auxiliary structures.

## Algorithm
1. Apply bitwise masks or shift operators.
2. Accumulate bitwise state to determine final output.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [4,5,4]`.
2. **Processing Steps:** We apply **Depth-First Search (DFS) / Breadth-First Search (BFS)** using our **Tree / Graph / Grid**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[4,4,5]`.
4. **Verification:** Binary reflections are: 

 
 4 -> (binary) `100` -> (reversed) `001` -> 1 
 5 -> (binary) `101` -> (reversed) `101` -> 5 
 4 -> (binary) `100` -> (reversed) `001` -> 1 
 
Sorting by the reflected values gives `[4, 4, 5]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Tree / Graph / Grid.

## Pattern
**Tree & Graph**

## Topics
- Tree
- Graph
- DFS
- BFS

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var sortByReflection = function(nums) {
    function getReflection(num) {
        let reflected = 0;

        while (num > 0) {
            let bit = num & 1;
            reflected = (reflected << 1) | bit;
            num >>>= 1;
        }

        return reflected;
    }

    return nums.sort((a, b) => {
        const reflectionA = getReflection(a);
        const reflectionB = getReflection(b);

        if (reflectionA !== reflectionB) {
            return reflectionA - reflectionB;
        }

        return a - b;
    });
};
```

## Why This Works
By utilizing **Tree & Graph**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [1356. Sort Integers by The Number of 1 Bits](../../1001-1500/1356-sort-integers-by-the-number-of-1-bits/)
- [1387. Sort Integers by The Power Value](../../1001-1500/1387-sort-integers-by-the-power-value/)
- [2471. Minimum Number of Operations to Sort a Binary Tree by Level](../../2001-2500/2471-minimum-number-of-operations-to-sort-a-binary-tree-by-level/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/sort-integers-by-binary-reflection/)
