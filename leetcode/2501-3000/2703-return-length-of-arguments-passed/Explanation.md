# LeetCode 2703: Return Length of Arguments Passed

**LeetCode Problem #2703 — Return Length of Arguments Passed**
Solve LeetCode Return Length of Arguments Passed using TypeScript and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Return Length of Arguments Passed |
| LeetCode | #2703 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Write a function `argumentsLength` that returns the count of arguments passed to it.

## Constraints
- `args` is a valid JSON array
- `0 <= args.length <= 100`

## Examples
### Example 1
- **Input:** `args = [5]`
- **Output:** `1`
- **Explanation:** argumentsLength(5); // 1

One value was passed to the function so it should return 1.

### Example 2
- **Input:** `args = [{}, null, "3"]`
- **Output:** `3`
- **Explanation:** argumentsLength({}, null, "3"); // 3

Three values were passed to the function so it should return 3.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
Uses rest parameters: `function(...args) { return args.length; }`. The spread operator collects all arguments into an array, and `.length` gives the count.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `args = [5]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** argumentsLength(5); // 1

One value was passed to the function so it should return 1.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Dictionary / Hash Map.

## Pattern
**Hash Map**

## Topics
- Hash Table
- Array
- Complement Lookup

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
function argumentsLength(...args: any[]): number {
    return args.length;
}
```

## Why This Works
By utilizing **Hash Map**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Using the same element twice.
2. Checking the map before inserting elements in the correct order.
3. Inefficient hash functions or unnecessary duplicate key updates.

## Interview Notes
- **Tests:** Hash map usage, complement/frequency lookup, and $O(n)$ time optimization.
- **Follow-up:** Can you solve the problem in $O(1)$ extra space if the input array is sorted?

## Related Problems
- [657. Robot Return to Origin](../../0501-1000/0657-robot-return-to-origin/)
- [1110. Delete Nodes And Return Forest](../../1001-1500/1110-delete-nodes-and-return-forest/)
- [58. Length of Last Word](../../0001-0500/0058-length-of-last-word/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/return-length-of-arguments-passed/)
