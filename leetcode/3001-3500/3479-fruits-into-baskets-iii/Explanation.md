# LeetCode 3479: Fruits Into Baskets III

**LeetCode Problem #3479 — Fruits Into Baskets III**
Solve LeetCode Fruits Into Baskets III using Python and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Fruits Into Baskets III |
| LeetCode | #3479 |
| Difficulty | Medium |
| Language | Python |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two arrays of integers, `fruits` and `baskets`, each of length `n`, where `fruits[i]` represents the **quantity** of the `i^th` type of fruit, and `baskets[j]` represents the **capacity** of the `j^th` basket.

From left to right, place the fruits according to these rules:

Each fruit type must be placed in the **leftmost available basket** with a capacity **greater than or equal** to the quantity of that fruit type. 
 Each basket can hold only one type of fruit. 
 If a fruit type cannot be placed in any basket, it remains unplaced .

Return the number of fruit types that remain unplaced after all possible allocations are made.

## Constraints
- `n == fruits.length == baskets.length`
- `1 <= n <= 10^5`
- `1 <= fruits[i], baskets[i] <= 10^9`

## Examples
### Example 1
- **Input:** `fruits = [4,2,5], baskets = [3,5,4]`
- **Output:** `1`
- **Explanation:** `fruits[0] = 4` is placed in `baskets[1] = 5`. 
 `fruits[1] = 2` is placed in `baskets[0] = 3`. 
 `fruits[2] = 5` cannot be placed in `baskets[2] = 4`. 
 

 Since one fruit type remains unplaced, we return 1.

### Example 2
- **Input:** `fruits = [3,6,1], baskets = [6,4,7]`
- **Output:** `0`
- **Explanation:** `fruits[0] = 3` is placed in `baskets[0] = 6`. 
 `fruits[1] = 6` cannot be placed in `baskets[1] = 4` (insufficient capacity) but can be placed in the next available basket, `baskets[2] = 7`. 
 `fruits[2] = 1` is placed in `baskets[1] = 4`. 
 

 Since all fruits are successfully placed, we return 0.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Fruits Into Baskets III**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `fruits = [4,2,5], baskets = [3,5,4]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** `fruits[0] = 4` is placed in `baskets[1] = 5`. 
 `fruits[1] = 2` is placed in `baskets[0] = 3`. 
 `fruits[2] = 5` cannot be placed in `baskets[2] = 4`. 
 

 Since one fruit type remains unplaced, we return 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Sorted Array.

## Pattern
**Binary Search**

## Topics
- Binary Search
- Divide and Conquer
- Search Space

## Language
Python

## Source Code
- [solution.py](./solution.py)


```python
from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        size = 1
        while size < n:
            size *= 2

        tree = [0] * (2 * size)
        for i, b in enumerate(baskets):
            tree[size + i] = b
        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])

        unplaced = 0
        for f in fruits:
            if tree[1] < f:
                unplaced += 1
                continue
            node = 1
            while node < size:
                if tree[2 * node] >= f:
                    node = 2 * node
                else:
                    node = 2 * node + 1
            tree[node] = 0
            node //= 2
            while node >= 1:
                tree[node] = max(tree[2 * node], tree[2 * node + 1])
                node //= 2

        return unplaced
```

## Why This Works
By utilizing **Binary Search**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Applying standard binary search without accounting for array rotation or duplicates.
2. Off-by-one errors when updating boundary pointers (`left = mid + 1` vs `right = mid - 1`).
3. Integer overflow during midpoint calculation (use `mid = left + (right - left) // 2`).

## Interview Notes
- **Tests:** Logarithmic search space reduction, boundary handling, and invariant preservation.
- **Follow-up:** How does performance change if the array contains duplicate elements?

## Related Problems
- [3477. Fruits Into Baskets II](../../3001-3500/3477-fruits-into-baskets-ii/)
- [904. Fruit Into Baskets](../../0501-1000/0904-fruit-into-baskets/)
- [2106. Maximum Fruits Harvested After at Most K Steps](../../2001-2500/2106-maximum-fruits-harvested-after-at-most-k-steps/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/fruits-into-baskets-iii/)
