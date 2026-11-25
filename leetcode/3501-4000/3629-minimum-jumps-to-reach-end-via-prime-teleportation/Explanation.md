# LeetCode 3629: Minimum Jumps to Reach End via Prime Teleportation

**LeetCode Problem #3629 — Minimum Jumps to Reach End via Prime Teleportation**
Solve LeetCode Minimum Jumps to Reach End via Prime Teleportation using C++ and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Minimum Jumps to Reach End via Prime Teleportation |
| LeetCode | #3629 |
| Difficulty | Medium |
| Language | C++ |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given an integer array `nums` of length `n`.

You start at index 0, and your goal is to reach index `n - 1`.

From any index `i`, you may perform one of the following operations:

**Adjacent Step**: Jump to index `i + 1` or `i - 1`, if the index is within bounds. 
 **Prime Teleportation**: If `nums[i]` is a prime number `p`, you may instantly jump to any index `j != i` such that `nums[j] % p == 0`.

Return the **minimum** number of jumps required to reach index `n - 1`.

## Constraints
- `1 <= n == nums.length <= 10^5`
- `1 <= nums[i] <= 10^6`

## Examples
### Example 1
- **Input:** `nums = [1,2,4,6]`
- **Output:** `2`
- **Explanation:** One optimal sequence of jumps is: 

 
 Start at index `i = 0`. Take an adjacent step to index 1. 
 At index `i = 1`, `nums[1] = 2` is a prime number. Therefore, we teleport to index `i = 3` as `nums[3] = 6` is divisible by 2. 
 

 Thus, the answer is 2.

### Example 2
- **Input:** `nums = [2,3,4,7,9]`
- **Output:** `2`
- **Explanation:** One optimal sequence of jumps is: 

 
 Start at index `i = 0`. Take an adjacent step to index `i = 1`. 
 At index `i = 1`, `nums[1] = 3` is a prime number. Therefore, we teleport to index `i = 4` since `nums[4] = 9` is divisible by 3. 
 

 Thus, the answer is 2.

### Example 3
- **Input:** `nums = [4,6,5,8]`
- **Output:** `3`
- **Explanation:** Since no teleportation is possible, we move through `0 &rarr; 1 &rarr; 2 &rarr; 3`. Thus, the answer is 3.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Minimum Jumps to Reach End via Prime Teleportation**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,4,6]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `2`.
4. **Verification:** One optimal sequence of jumps is: 

 
 Start at index `i = 0`. Take an adjacent step to index 1. 
 At index `i = 1`, `nums[1] = 2` is a prime number. Therefore, we teleport to index `i = 3` as `nums[3] = 6` is divisible by 2. 
 

 Thus, the answer is 2.

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
C++

## Source Code
- [solution.cpp](./solution.cpp)


```cpp
class Solution {
public:
    int minJumps(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return 0;

        int mx = *max_element(nums.begin(), nums.end());

        // Smallest Prime Factor (SPF)
        vector<int> spf(mx + 1);
        for (int i = 0; i <= mx; i++)
            spf[i] = i;

        for (int i = 2; i * i <= mx; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j <= mx; j += i) {
                    if (spf[j] == j)
                        spf[j] = i;
                }
            }
        }

        // prime -> indices whose values are divisible by that prime
        vector<vector<int>> groups(mx + 1);

        for (int i = 0; i < n; i++) {
            int x = nums[i];

            while (x > 1) {
                int p = spf[x];
                groups[p].push_back(i);

                while (x % p == 0)
                    x /= p;
            }
        }

        vector<int> dist(n, -1);
        vector<bool> usedPrime(mx + 1, false);

        queue<int> q;
        q.push(0);
        dist[0] = 0;

        while (!q.empty()) {
            int i = q.front();
            q.pop();

            if (i == n - 1)
                return dist[i];

            // Adjacent jumps
            if (i + 1 < n && dist[i + 1] == -1) {
                dist[i + 1] = dist[i] + 1;
                q.push(i + 1);
            }

            if (i - 1 >= 0 && dist[i - 1] == -1) {
                dist[i - 1] = dist[i] + 1;
                q.push(i - 1);
            }

            // Prime teleportation
            int value = nums[i];

            // Teleportation is possible only if nums[i] itself is prime
            if (value >= 2 && spf[value] == value &&
                !usedPrime[value]) {

                usedPrime[value] = true;

                for (int j : groups[value]) {
                    if (dist[j] == -1) {
                        dist[j] = dist[i] + 1;
                        q.push(j);
                    }
                }
            }
        }

        return -1;
    }
};
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
- [1654. Minimum Jumps to Reach Home](../../1501-2000/1654-minimum-jumps-to-reach-home/)
- [3896. Minimum Operations to Transform Array into Alternating Prime](../../3501-4000/3896-minimum-operations-to-transform-array-into-alternating-prime/)
- [3133. Minimum Array End](../../3001-3500/3133-minimum-array-end/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/)
