# LeetCode 3477: Fruits Into Baskets II

**LeetCode Problem #3477 — Fruits Into Baskets II**
Solve LeetCode Fruits Into Baskets II using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Fruits Into Baskets II |
| LeetCode | #3477 |
| Difficulty | Easy |
| Language | JavaScript |
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
- `1 <= n <= 100`
- `1 <= fruits[i], baskets[i] <= 1000`

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
To solve **Fruits Into Baskets II**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

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
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var numOfUnplacedFruits = function(fruits, baskets) {
    let unplaced = 0;

    for (const fruit of fruits) {
        let placed = false;
        for (let j = 0; j < baskets.length; j++) {
            if (baskets[j] >= fruit) {
                baskets[j] = 0; // Mark basket as occupied
                placed = true;
                break;
            }
        }
        if (!placed) {
            unplaced++;
        }
    }

    return unplaced;
};
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
- [904. Fruit Into Baskets](../../0501-1000/0940-fruit-into-baskets/)
- [701. Insert into a Binary Search Tree](../../0501-1000/0784-insert-into-a-binary-search-tree/)
- [842. Split Array into Fibonacci Sequence](../../0501-1000/0872-split-array-into-fibonacci-sequence/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/fruits-into-baskets-ii/)
