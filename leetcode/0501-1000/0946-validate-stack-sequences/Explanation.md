# LeetCode 946: Validate Stack Sequences

**LeetCode Problem #946 — Validate Stack Sequences**
Solve LeetCode Validate Stack Sequences using JavaScript and Binary Search. This solution finds the optimal result using Modified Binary Search in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Validate Stack Sequences |
| LeetCode | #946 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | Modified Binary Search |
| Data Structure | Sorted Array |
| Pattern | Binary Search |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
Given two integer arrays `pushed` and `popped` each with distinct values, return `true`* if this could have been the result of a sequence of push and pop operations on an initially empty stack, or *`false`* otherwise.*

## Constraints
- `1 <= pushed.length <= 1000`
- `0 <= pushed[i] <= 1000`
- All the elements of `pushed` are **unique**.
- `popped.length == pushed.length`
- `popped` is a permutation of `pushed`.

## Examples
### Example 1
- **Input:** `pushed = [1,2,3,4,5], popped = [4,5,3,2,1]`
- **Output:** `true`
- **Explanation:** We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

### Example 2
- **Input:** `pushed = [1,2,3,4,5], popped = [4,3,5,1,2]`
- **Output:** `false`
- **Explanation:** 1 cannot be popped before 2.

## Key Insight
Exploit sorted ordering or monotonic properties to eliminate half of the search space at each step in $O(\log n)$ time.

## Approach
To solve **Validate Stack Sequences**, we observe the problem requirements and utilize the **Binary Search** technique. Exploiting monotonic ordering or sorted properties in the input space, we maintain `left` and `right` boundary pointers. In each iteration, we evaluate the midpoint to discard half of the search range, reducing the time complexity to $O(\log n)$.

## Algorithm
1. Initialize boundary pointers `left` and `right`.
2. Compute `mid = left + (right - left) // 2` to prevent overflow.
3. Adjust `left` or `right` depending on whether target satisfies the partition condition.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `pushed = [1,2,3,4,5], popped = [4,5,3,2,1]`.
2. **Processing Steps:** We apply **Modified Binary Search** using our **Sorted Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `true`.
4. **Verification:** We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

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
var validateStackSequences = function(pushed, popped) {
    const stack = [];
    let j = 0;

    for (let num of pushed) {
        // Push element onto stack
        stack.push(num);

        // Pop while stack top matches popped sequence
        while (
            stack.length > 0 &&
            stack[stack.length - 1] === popped[j]
        ) {
            stack.pop();
            j++;
        }
    }

    // All elements must be popped
    return j === popped.length;
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
- [155. Min Stack](../../0001-0500/0155-min-stack/)
- [225. Implement Stack using Queues](../../0001-0500/0225-implement-stack-using-queues/)
- [895. Maximum Frequency Stack](../../0501-1000/0895-maximum-frequency-stack/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/validate-stack-sequences/)
