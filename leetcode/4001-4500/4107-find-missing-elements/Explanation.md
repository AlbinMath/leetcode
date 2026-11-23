# LeetCode 3731: Find Missing Elements

**LeetCode Problem #3731 — Find Missing Elements**
Solve LeetCode Find Missing Elements using PHP and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Missing Elements |
| LeetCode | #3731 |
| Difficulty | Easy |
| Language | PHP |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` consisting of **unique** integers.

Originally, `nums` contained **every integer** within a certain range. However, some integers might have gone **missing** from the array.

The **smallest** and **largest** integers of the original range are still present in `nums`.

Return a **sorted** list of all the missing integers in this range. If no integers are missing, return an **empty** list.

## Constraints
- `2 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [1,4,2,5]`
- **Output:** `[3]`
- **Explanation:** The smallest integer is 1 and the largest is 5, so the full range should be `[1,2,3,4,5]`. Among these, only 3 is missing.

### Example 2
- **Input:** `nums = [7,8,6,9]`
- **Output:** `[]`
- **Explanation:** The smallest integer is 6 and the largest is 9, so the full range is `[6,7,8,9]`. All integers are already present, so no integer is missing.

### Example 3
- **Input:** `nums = [5,1]`
- **Output:** `[2,3,4]`
- **Explanation:** The smallest integer is 1 and the largest is 5, so the full range should be `[1,2,3,4,5]`. The missing integers are 2, 3, and 4.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Find Missing Elements**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,4,2,5]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[3]`.
4. **Verification:** The smallest integer is 1 and the largest is 5, so the full range should be `[1,2,3,4,5]`. Among these, only 3 is missing.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
PHP

## Source Code
- [solution.php](./solution.php)


```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function findMissingElements($nums) {
        $min = min($nums);
        $max = max($nums);

        $present = array_flip($nums);
        $result = [];

        for ($i = $min; $i <= $max; $i++) {
            if (!isset($present[$i])) {
                $result[] = $i;
            }
        }

        return $result;
    }
}
```

## Why This Works
By utilizing **Stack & Queue**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [658. Find K Closest Elements](../../0501-1000/0658-find-k-closest-elements/)
- [1261. Find Elements in a Contaminated Binary Tree](../../1001-1500/1387-find-elements-in-a-contaminated-binary-tree/)
- [2593. Find Score of an Array After Marking All Elements](../../2501-3000/2695-find-score-of-an-array-after-marking-all-elements/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-missing-elements/)
