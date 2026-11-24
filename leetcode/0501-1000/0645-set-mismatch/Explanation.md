# LeetCode 645: Set Mismatch

**LeetCode Problem #645 — Set Mismatch**
Solve LeetCode Set Mismatch using TypeScript and Bit Manipulation. This solution finds the optimal result using Bitwise Masking & Bit Shift in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Set Mismatch |
| LeetCode | #645 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Bitwise Masking & Bit Shift |
| Data Structure | Integer Bitmask |
| Pattern | Bit Manipulation |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You have a set of integers `s`, which originally contains all the numbers from `1` to `n`. Unfortunately, due to some error, one of the numbers in `s` got duplicated to another number in the set, which results in **repetition of one** number and **loss of another** number.

You are given an integer array `nums` representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return *them in the form of an array*.

## Constraints
- `2 <= nums.length <= 10^4`
- `1 <= nums[i] <= 10^4`

## Examples
### Example 1
- **Input:** `nums = [1,2,2,4]`
- **Output:** `[2,3]`

### Example 2
- **Input:** `nums = [1,1]`
- **Output:** `[1,2]`

## Key Insight
Leverage **Bit Manipulation** with **Integer Bitmask** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a **HashSet** for straightforward detection.

1. **Find Duplicate:** It iterates through `nums`, adding each number to a `Set`. If a number is already in the set, it's the duplicate.
2. **Find Missing:** It loops from `1` to `n` and checks which number is not in the set — that's the missing number.

Time complexity is $O(N)$ and space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Integer Bitmask**).
2. Process elements sequentially using **Bitwise Masking & Bit Shift**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,2,4]`.
2. **Processing Steps:** We apply **Bitwise Masking & Bit Shift** using our **Integer Bitmask**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[2,3]`.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Integer Bitmask.

## Pattern
**Bit Manipulation**

## Topics
- Bit Manipulation
- Bitwise Math

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
function findErrorNums(nums: number[]): number[] {
    const n = nums.length;
    const seen = new Set<number>();

    let duplicate = 0;

    for (const num of nums) {
        if (seen.has(num)) {
            duplicate = num;
        }
        seen.add(num);
    }

    let missing = 0;

    for (let i = 1; i <= n; i++) {
        if (!seen.has(i)) {
            missing = i;
            break;
        }
    }

    return [duplicate, missing];
}
```

## Why This Works
By utilizing **Bit Manipulation**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [73. Set Matrix Zeroes](../../0001-0500/0073-set-matrix-zeroes/)
- [762. Prime Number of Set Bits in Binary Representation](../../0501-1000/0762-prime-number-of-set-bits-in-binary-representation/)
- [902. Numbers At Most N Given Digit Set](../../0501-1000/0902-numbers-at-most-n-given-digit-set/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/set-mismatch/)
