# LeetCode 1365: How Many Numbers Are Smaller Than the Current Number

**LeetCode Problem #1365 — How Many Numbers Are Smaller Than the Current Number**
Solve LeetCode How Many Numbers Are Smaller Than the Current Number using TypeScript and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | How Many Numbers Are Smaller Than the Current Number |
| LeetCode | #1365 |
| Difficulty | Easy |
| Language | TypeScript |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given the array `nums`, for each `nums[i]` find out how many numbers in the array are smaller than it. That is, for each `nums[i]` you have to count the number of valid `j's` such that `j != i` **and** `nums[j] < nums[i]`.

Return the answer in an array.

## Constraints
- `2 <= nums.length <= 500`
- `0 <= nums[i] <= 100`

## Examples
### Example 1
- **Input:** `nums = [8,1,2,2,3]`
- **Output:** `[4,0,1,1,3]`
- **Explanation:** For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

### Example 2
- **Input:** `nums = [6,5,4,8]`
- **Output:** `[2,1,0,3]`

### Example 3
- **Input:** `nums = [7,7,7,7]`
- **Output:** `[0,0,0,0]`

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses **Counting Sort + Prefix Sum** for an efficient $O(N)$ solution.

1. **Count Frequencies:** Count how many times each value `0–100` appears.
2. **Prefix Sum:** Transform the count array so `count[i]` = total numbers ≤ `i`.
3. **Build Result:** For each `num` in the original array, the count of numbers strictly smaller is `count[num - 1]` (or `0` if `num == 0`).

Time complexity is $O(N + K)$ where $K = 100$, and space complexity is $O(K)$.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [8,1,2,2,3]`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[4,0,1,1,3]`.
4. **Verification:** For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
TypeScript

## Source Code
- [solution.ts](./solution.ts)


```typescript
function smallerNumbersThanCurrent(nums: number[]): number[] {
    const count = new Array(101).fill(0);

    // Count frequency of each number
    for (const num of nums) {
        count[num]++;
    }

    // Prefix sum: count[x] = numbers <= x
    for (let i = 1; i <= 100; i++) {
        count[i] += count[i - 1];
    }

    const result: number[] = [];

    for (const num of nums) {
        // Number of elements strictly smaller than num
        result.push(num === 0 ? 0 : count[num - 1]);
    }

    return result;
}
```

## Why This Works
By utilizing **Prefix Sum**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [315. Count of Smaller Numbers After Self](../../0001-0500/0315-count-of-smaller-numbers-after-self/)
- [1295. Find Numbers with Even Number of Digits](../../1001-1500/1295-find-numbers-with-even-number-of-digits/)
- [1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K](../../1001-1500/1414-find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/)
