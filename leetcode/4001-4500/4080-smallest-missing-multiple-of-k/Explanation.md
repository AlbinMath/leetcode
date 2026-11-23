# LeetCode 3718: Smallest Missing Multiple of K

**LeetCode Problem #3718 — Smallest Missing Multiple of K**
Solve LeetCode Smallest Missing Multiple of K using C# and Prefix Sum. This solution finds the optimal result using Prefix Sum Precomputation in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Smallest Missing Multiple of K |
| LeetCode | #3718 |
| Difficulty | Easy |
| Language | C# |
| Algorithm | Prefix Sum Precomputation |
| Data Structure | Prefix Array |
| Pattern | Prefix Sum |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Given an integer array `nums` and an integer `k`, return the **smallest positive multiple** of `k` that is **missing** from `nums`.

A **multiple** of `k` is any positive integer divisible by `k`.

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`
- `1 <= k <= 100`

## Examples
### Example 1
- **Input:** `nums = [8,2,3,4,6], k = 2`
- **Output:** `10`
- **Explanation:** The multiples of `k = 2` are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from `nums` is 10.

### Example 2
- **Input:** `nums = [1,4,7,10,15], k = 5`
- **Output:** `5`
- **Explanation:** The multiples of `k = 5` are 5, 10, 15, 20... and the smallest multiple missing from `nums` is 5.

## Key Insight
Leverage **Prefix Sum** with **Prefix Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
The code uses a `HashSet` to efficiently check for the presence of numbers in $O(1)$ time.
1. First, it converts the `nums` array into a `HashSet<int>` called `set`. This allows us to quickly look up whether a number exists in the array without having to scan the entire array every time.
2. It initializes a variable `multiple` to the first multiple, which is `k`.
3. It uses a `while` loop to continuously check if `set` contains the current `multiple`.
   - If it does, we increment the `multiple` by `k` to check the next multiple (`2k`, `3k`, etc.).
4. The loop stops as soon as it finds a `multiple` that is **not** in the `HashSet`.
5. Finally, it returns that missing `multiple`.

This approach is highly efficient. Converting the array to a HashSet takes $O(N)$ time (where $N$ is the number of elements in `nums`), and the while loop takes at most $O(N)$ steps because there can be at most $N$ multiples of $k$ present in the array. Therefore, the overall time complexity is $O(N)$ and the space complexity is $O(N)$.

## Algorithm
1. Initialize state variables / data structure (**Prefix Array**).
2. Process elements sequentially using **Prefix Sum Precomputation**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [8,2,3,4,6], k = 2`.
2. **Processing Steps:** We apply **Prefix Sum Precomputation** using our **Prefix Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `10`.
4. **Verification:** The multiples of `k = 2` are 2, 4, 6, 8, 10, 12... and the smallest multiple missing from `nums` is 10.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(n) — Memory footprint corresponds to auxiliary storage for Prefix Array.

## Pattern
**Prefix Sum**

## Topics
- Prefix Sum
- Array

## Language
C#

## Source Code
- [solution.cs](./solution.cs)


```csharp
public class Solution {
    public int MissingMultiple(int[] nums, int k) {
        HashSet<int> set = new HashSet<int>(nums);

        int multiple = k;

        while (set.Contains(multiple)) {
            multiple += k;
        }

        return multiple;
    }
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
- [2413. Smallest Even Multiple](../../2001-2500/2491-smallest-even-multiple/)
- [2003. Smallest Missing Genetic Value in Each Subtree](../../2001-2500/2131-smallest-missing-genetic-value-in-each-subtree/)
- [2996. Smallest Missing Integer Greater Than Sequential Prefix Sum](../../3001-3500/3236-smallest-missing-integer-greater-than-sequential-prefix-sum/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/smallest-missing-multiple-of-k/)
