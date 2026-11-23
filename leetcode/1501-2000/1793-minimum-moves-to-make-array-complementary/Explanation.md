# LeetCode 1674: Minimum Moves to Make Array Complementary

**LeetCode Problem #1674 — Minimum Moves to Make Array Complementary**
Solve LeetCode Minimum Moves to Make Array Complementary using C++ and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Moves to Make Array Complementary |
| LeetCode | #1674 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
You are given an integer array `nums` of **even** length `n` and an integer `limit`. In one move, you can replace any integer from `nums` with another integer between `1` and `limit`, inclusive.

The array `nums` is **complementary** if for all indices `i` (**0-indexed**), `nums[i] + nums[n - 1 - i]` equals the same number. For example, the array `[1,2,3,4]` is complementary because for all indices `i`, `nums[i] + nums[n - 1 - i] = 5`.

Return the ***minimum** number of moves required to make *`nums`* **complementary***.

## Constraints
- `n == nums.length`
- `2 <= n <= 10^5`
- `1 <= nums[i] <= limit <= 10^5`
- `n` is even.

## Examples
### Example 1
- **Input:** `nums = [1,2,4,3], limit = 4`
- **Output:** `1`
- **Explanation:** In 1 move, you can change nums to [1,2, 2 ,3] (underlined elements are changed).
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.

### Example 2
- **Input:** `nums = [1,2,2,1], limit = 2`
- **Output:** `2`
- **Explanation:** In 2 moves, you can change nums to [ 2 ,2,2, 2 ]. You cannot change any number to 3 since 3 > limit.

### Example 3
- **Input:** `nums = [1,2,1,2], limit = 2`
- **Output:** `0`
- **Explanation:** nums is already complementary.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
The code uses a **Difference Array** technique to efficiently calculate the cost for every possible target sum.

1. For each pair `(a, b)`, determine the ranges of target sums achievable with 0, 1, or 2 replacements.
2. Use a difference array to mark these ranges: target sum = `a+b` needs 0 moves, sums in `[min(a,b)+1, max(a,b)+limit]` need 1 move, all others need 2.
3. Sweep through the difference array to find the target sum with minimum total moves.

Time complexity is $O(N + \text{limit})$ and space complexity is $O(\text{limit})$.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,4,3], limit = 4`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `1`.
4. **Verification:** In 1 move, you can change nums to [1,2, 2 ,3] (underlined elements are changed).
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int minMoves(vector<int>& nums, int limit) {
        int n = nums.size();

        // Difference array for number of moves
        vector<int> diff(2 * limit + 2, 0);

        for (int i = 0; i < n / 2; i++) {
            int a = nums[i];
            int b = nums[n - 1 - i];

            int low = min(a, b) + 1;
            int high = max(a, b) + limit;

            int sum = a + b;

            // 1 move is possible for sums in [low, high]
            diff[low]--;
            diff[high + 1]++;

            // 0 moves for exactly 'sum'
            diff[sum]--;
            diff[sum + 1]++;
        }

        int moves = n;
        int current = n;

        for (int s = 2; s <= 2 * limit; s++) {
            current += diff[s];
            moves = min(moves, current);
        }

        return moves;
    }
};
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
- [945. Minimum Increment to Make Array Unique](../../0501-1000/0982-minimum-increment-to-make-array-unique/)
- [1558. Minimum Numbers of Function Calls to Make Target Array](../../1501-2000/1662-minimum-numbers-of-function-calls-to-make-target-array/)
- [1827. Minimum Operations to Make the Array Increasing](../../1501-2000/1938-minimum-operations-to-make-the-array-increasing/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/)
