# LeetCode 1441: Build an Array With Stack Operations

**LeetCode Problem #1441 — Build an Array With Stack Operations**
Solve LeetCode Build an Array With Stack Operations using TypeScript and Stack & Queue. This solution finds the optimal result using Stack Push / Pop Parsing in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Build an Array With Stack Operations |
| LeetCode | #1441 |
| Difficulty | Medium |
| Language | TypeScript |
| Algorithm | Stack Push / Pop Parsing |
| Data Structure | Stack |
| Pattern | Stack & Queue |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `target` and an integer `n`.

You have an empty stack with the two following operations:

**`"Push"`**: pushes an integer to the top of the stack. 
 **`"Pop"`**: removes the integer on the top of the stack.

You also have a stream of the integers in the range `[1, n]`.

Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to `target`. You should follow the following rules:

If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack. 
 If the stack is not empty, pop the integer at the top of the stack. 
 If, at any moment, the elements in the stack (from the bottom to the top) are equal to `target`, do not read new integers from the stream and do not do more operations on the stack.

Return *the stack operations needed to build *`target` following the mentioned rules. If there are multiple valid answers, return **any of them**.

## Constraints
- `1 <= target.length <= 100`
- `1 <= n <= 100`
- `1 <= target[i] <= n`
- `target` is strictly increasing.

## Examples
### Example 1
- **Input:** `target = [1,3], n = 3`
- **Output:** `["Push","Push","Pop","Push"]`
- **Explanation:** Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Pop the integer on the top of the stack. s = [1].
Read 3 from the stream and push it to the stack. s = [1,3].

### Example 2
- **Input:** `target = [1,2,3], n = 3`
- **Output:** `["Push","Push","Push"]`
- **Explanation:** Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Read 3 from the stream and push it to the stack. s = [1,2,3].

### Example 3
- **Input:** `target = [1,2], n = 4`
- **Output:** `["Push","Push"]`
- **Explanation:** Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Since the stack (from the bottom to the top) is equal to target, we stop the stack operations.
The answers that read integer 3 from the stream are not accepted.

## Key Insight
Leverage **Stack & Queue** with **Stack** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code iterates through numbers 1 to n while tracking which element of the target we need next. If the current number matches the next target element, push it. If it doesn't match, push then immediately pop it (to skip that number). Stop once the entire target is built.

Time complexity is $O(N)$ and space complexity is $O(N)$ for the output.

## Algorithm
1. Initialize state variables / data structure (**Stack**).
2. Process elements sequentially using **Stack Push / Pop Parsing**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `target = [1,3], n = 3`.
2. **Processing Steps:** We apply **Stack Push / Pop Parsing** using our **Stack**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `["Push","Push","Pop","Push"]`.
4. **Verification:** Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Pop the integer on the top of the stack. s = [1].
Read 3 from the stream and push it to the stack. s = [1,3].

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Stack.

## Pattern
**Stack & Queue**

## Topics
- Stack
- String Parsing

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
function buildArray(target: number[], n: number): string[] {
    const result: string[] = [];
    let index = 0;

    for (let num = 1; num <= n && index < target.length; num++) {
        result.push("Push");

        if (num === target[index]) {
            index++;
        } else {
            result.push("Pop");
        }
    }

    return result;
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
- [1551. Minimum Operations to Make Array Equal](../../1501-2000/1551-minimum-operations-to-make-array-equal/)
- [1827. Minimum Operations to Make the Array Increasing](../../1501-2000/1827-minimum-operations-to-make-the-array-increasing/)
- [1887. Reduction Operations to Make the Array Elements Equal](../../1501-2000/1887-reduction-operations-to-make-the-array-elements-equal/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/build-an-array-with-stack-operations/)
