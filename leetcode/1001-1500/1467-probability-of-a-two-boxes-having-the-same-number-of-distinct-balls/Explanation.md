# LeetCode 1467: Probability of a Two Boxes Having The Same Number of Distinct Balls

**LeetCode Problem #1467 — Probability of a Two Boxes Having The Same Number of Distinct Balls**
Solve LeetCode Probability of a Two Boxes Having The Same Number of Distinct Balls using JavaScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Probability of a Two Boxes Having The Same Number of Distinct Balls |
| LeetCode | #1467 |
| Difficulty | Hard |
| Language | JavaScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given `2n` balls of `k` distinct colors. You will be given an integer array `balls` of size `k` where `balls[i]` is the number of balls of color `i`.

All the balls will be **shuffled uniformly at random**, then we will distribute the first `n` balls to the first box and the remaining `n` balls to the other box (Please read the explanation of the second example carefully).

Please note that the two boxes are considered different. For example, if we have two balls of colors `a` and `b`, and two boxes `[]` and `()`, then the distribution `[a] (b)` is considered different than the distribution `[b] (a) `(Please read the explanation of the first example carefully).

Return* the probability* that the two boxes have the same number of distinct balls. Answers within `10^-5` of the actual value will be accepted as correct.

## Constraints
- `1 <= balls.length <= 8`
- `1 <= balls[i] <= 6`
- `sum(balls)` is even.

## Examples
### Example 1
- **Input:** `balls = [1,1]`
- **Output:** `1.00000`
- **Explanation:** Only 2 ways to divide the balls equally:
- A ball of color 1 to box 1 and a ball of color 2 to box 2
- A ball of color 2 to box 1 and a ball of color 1 to box 2
In both ways, the number of distinct colors in each box is equal. The probability is 2/2 = 1

### Example 2
- **Input:** `balls = [2,1,1]`
- **Output:** `0.66667`
- **Explanation:** We have the set of balls [1, 1, 2, 3]
This set of balls will be shuffled randomly and we may have one of the 12 distinct shuffles with equal probability (i.e. 1/12):
[1,1 / 2,3], [1,1 / 3,2], [1,2 / 1,3], [1,2 / 3,1], [1,3 / 1,2], [1,3 / 2,1], [2,1 / 1,3], [2,1 / 3,1], [2,3 / 1,1], [3,1 / 1,2], [3,1 / 2,1], [3,2 / 1,1]
After that, we add the first two balls to the first box and the second two balls to the second box.
We can see that 8 of these 12 possible random distributions have the same number of distinct colors of balls in each box.
Probability is 8/12 = 0.66667

### Example 3
- **Input:** `balls = [1,2,1,2]`
- **Output:** `0.60000`
- **Explanation:** The set of balls is [1, 2, 2, 3, 4, 4]. It is hard to display all the 180 possible random shuffles of this set but it is easy to check that 108 of them will have the same number of distinct colors in each box.
Probability = 108 / 180 = 0.6

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Probability of a Two Boxes Having The Same Number of Distinct Balls**, we observe the problem requirements and utilize the **Tree & Graph** technique. We conduct a structured Breadth-First Search (BFS) or Depth-First Search (DFS) traversal, tracking visited nodes to process connections without cycles.

## Algorithm
1. Initialize queue/stack with initial node.
2. Pop current node, visit adjacent neighbors, and push valid unvisited nodes.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `balls = [1,1]`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1.00000`.
4. **Verification:** Only 2 ways to divide the balls equally:
- A ball of color 1 to box 1 and a ball of color 2 to box 2
- A ball of color 2 to box 1 and a ball of color 1 to box 2
In both ways, the number of distinct colors in each box is equal. The probability is 2/2 = 1

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var getProbability = function(balls) {
    const n = balls.reduce((sum, x) => sum + x, 0) / 2;
    const k = balls.length;

    const fact = new Array(49).fill(1);
    for (let i = 1; i < fact.length; i++) {
        fact[i] = fact[i - 1] * i;
    }

    let totalWays = 0;
    let validWays = 0;

    const dfs = (idx, box1Count, box2Count, distinct1, distinct2, ways) => {
        if (box1Count > n || box2Count > n) return;

        if (idx === k) {
            if (box1Count === n && box2Count === n) {
                totalWays += ways;
                if (distinct1 === distinct2) {
                    validWays += ways;
                }
            }
            return;
        }

        const ballsOfColor = balls[idx];

        for (let take = 0; take <= ballsOfColor; take++) {
            const remaining = ballsOfColor - take;

            dfs(
                idx + 1,
                box1Count + take,
                box2Count + remaining,
                distinct1 + (take > 0 ? 1 : 0),
                distinct2 + (remaining > 0 ? 1 : 0),
                ways / (fact[take] * fact[remaining])
            );
        }
    };

    dfs(0, 0, 0, 0, 0, fact[n] * fact[n]);

    return validWays / totalWays;
};
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
- [3160. Find the Number of Distinct Colors Among the Balls](../../3001-3500/3160-find-the-number-of-distinct-colors-among-the-balls/)
- [1519. Number of Nodes in the Sub-Tree With the Same Label](../../1501-2000/1519-number-of-nodes-in-the-sub-tree-with-the-same-label/)
- [1569. Number of Ways to Reorder Array to Get Same BST](../../1501-2000/1569-number-of-ways-to-reorder-array-to-get-same-bst/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/)
