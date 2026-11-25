# LeetCode 1237: Find Positive Integer Solution for a Given Equation

**LeetCode Problem #1237 — Find Positive Integer Solution for a Given Equation**
Solve LeetCode Find Positive Integer Solution for a Given Equation using Python and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Find Positive Integer Solution for a Given Equation |
| LeetCode | #1237 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given a callable function `f(x, y)` **with a hidden formula** and a value `z`, reverse engineer the formula and return *all positive integer pairs *`x`* and *`y`* where *`f(x,y) == z`. You may return the pairs in any order.

While the exact formula is hidden, the function is monotonically increasing, i.e.:

`f(x, y) < f(x + 1, y)` 
 `f(x, y) < f(x, y + 1)`

The function interface is defined like this:

interface CustomFunction {
public:
 // Returns some positive integer f(x, y) for two positive integers x and y based on a formula.
 int f(int x, int y);
};

We will judge your solution as follows:

The judge has a list of `9` hidden implementations of `CustomFunction`, along with a way to generate an **answer key** of all valid pairs for a specific `z`. 
 The judge will receive two inputs: a `function_id` (to determine which implementation to test your code with), and the target `z`. 
 The judge will call your `findSolution` and compare your results with the **answer key**. 
 If your results match the **answer key**, your solution will be `Accepted`.

## Constraints
- `1 <= function_id <= 9`
- `1 <= z <= 100`
- It is guaranteed that the solutions of `f(x, y) == z` will be in the range `1 <= x, y <= 1000`.
- It is also guaranteed that `f(x, y)` will fit in 32 bit signed integer if `1 <= x, y <= 1000`.

## Examples
### Example 1
- **Input:** `function_id = 1, z = 5`
- **Output:** `[[1,4],[2,3],[3,2],[4,1]]`
- **Explanation:** The hidden formula for function_id = 1 is f(x, y) = x + y.
The following positive integer values of x and y make f(x, y) equal to 5:
x=1, y=4 -> f(1, 4) = 1 + 4 = 5.
x=2, y=3 -> f(2, 3) = 2 + 3 = 5.
x=3, y=2 -> f(3, 2) = 3 + 2 = 5.
x=4, y=1 -> f(4, 1) = 4 + 1 = 5.

### Example 2
- **Input:** `function_id = 2, z = 5`
- **Output:** `[[1,5],[5,1]]`
- **Explanation:** The hidden formula for function_id = 2 is f(x, y) = x * y.
The following positive integer values of x and y make f(x, y) equal to 5:
x=1, y=5 -> f(1, 5) = 1 * 5 = 5.
x=5, y=1 -> f(5, 1) = 5 * 1 = 5.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Find Positive Integer Solution for a Given Equation**, we observe the problem requirements and utilize the **Monotonic Stack** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `function_id = 1, z = 5`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[[1,4],[2,3],[3,2],[4,1]]`.
4. **Verification:** The hidden formula for function_id = 1 is f(x, y) = x + y.
The following positive integer values of x and y make f(x, y) equal to 5:
x=1, y=4 -> f(1, 4) = 1 + 4 = 5.
x=2, y=3 -> f(2, 3) = 2 + 3 = 5.
x=3, y=2 -> f(3, 2) = 3 + 2 = 5.
x=4, y=1 -> f(4, 1) = 4 + 1 = 5.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Two Pointers**

## Topics
- Two Pointers
- Array
- Sorting

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        x, y = 1, 1000
        while x <= 1000 and y >= 1:
            v = customfunction.f(x, y)
            if v < z:
                x += 1
            elif v > z:
                y -= 1
            else:
                res.append([x, y])
                x += 1
                y -= 1
        return res
```

## Why This Works
By utilizing **Two Pointers**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Failing to sort the array when ordering is required.
2. Not skipping duplicate elements leading to non-unique pairs.
3. Pointer out-of-bounds errors on edge inputs.

## Interview Notes
- **Tests:** In-place array traversal, duplicate elimination, and pointer convergence.
- **Follow-up:** Can this approach be extended to 3Sum or 4Sum variants?

## Related Problems
- [2529. Maximum Count of Positive Integer and Negative Integer](../../2501-3000/2529-maximum-count-of-positive-integer-and-negative-integer/)
- [1283. Find the Smallest Divisor Given a Threshold](../../1001-1500/1283-find-the-smallest-divisor-given-a-threshold/)
- [1982. Find Array Given Subset Sums](../../1501-2000/1982-find-array-given-subset-sums/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/)
