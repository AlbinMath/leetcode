# LeetCode 3345: Smallest Divisible Digit Product I

**LeetCode Problem #3345 — Smallest Divisible Digit Product I**
Solve LeetCode Smallest Divisible Digit Product I using Ruby and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Divisible Digit Product I |
| LeetCode | #3345 |
| Difficulty | Easy |
| Language | Ruby |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given two integers `n` and `t`. Return the **smallest** number greater than or equal to `n` such that the **product of its digits** is divisible by `t`.

## Constraints
- `1 <= n <= 100`
- `1 <= t <= 10`

## Examples
### Example 1
- **Input:** `n = 10, t = 2`
- **Output:** `10`
- **Explanation:** The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.

### Example 2
- **Input:** `n = 15, t = 3`
- **Output:** `16`
- **Explanation:** The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater than or equal to 15 that satisfies the condition.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Smallest Divisible Digit Product I**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `n = 10, t = 2`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
Ruby

## Source Code
- [solution.rb](./solution.rb)


```ruby
# @param {Integer} n
# @param {Integer} t
# @return {Integer}
def smallest_number(n, t)
    while true
        x = n
        product = 1

        while x > 0
            product *= x % 10
            x /= 10
        end

        return n if product % t == 0

        n += 1
    end
end
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
- [3348. Smallest Divisible Digit Product II](../../3501-4000/3635-smallest-divisible-digit-product-ii/)
- [2605. Form Smallest Number From Two Digit Arrays](../../2501-3000/2668-form-smallest-number-from-two-digit-arrays/)
- [3550. Smallest Index With Digit Sum Equal to Index](../../3501-4000/3869-smallest-index-with-digit-sum-equal-to-index/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-divisible-digit-product-i/)
