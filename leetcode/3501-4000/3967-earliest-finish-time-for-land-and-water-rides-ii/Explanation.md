# LeetCode 3635: Earliest Finish Time for Land and Water Rides II

**LeetCode Problem #3635 — Earliest Finish Time for Land and Water Rides II**
Solve LeetCode Earliest Finish Time for Land and Water Rides II using Java and Two Pointers. This solution finds the optimal result using Two Pointer Convergence & Scanning in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Earliest Finish Time for Land and Water Rides II |
| LeetCode | #3635 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Two Pointer Convergence & Scanning |
| Data Structure | Array |
| Pattern | Two Pointers |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given two categories of theme park attractions: land rides and water rides .

Land rides

landStartTime[i] &ndash; the earliest time the `i^th` land ride can be boarded. 
 landDuration[i] &ndash; how long the `i^th` land ride lasts. 
 
 
 Water rides 
 
 waterStartTime[j] &ndash; the earliest time the `j^th` water ride can be boarded. 
 waterDuration[j] &ndash; how long the `j^th` water ride lasts.

A tourist must experience exactly one ride from each category, in either order .

A ride may be started at its opening time or any later moment . 
 If a ride is started at time t , it finishes at time t + duration . 
 Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.

Return the earliest possible time at which the tourist can finish both rides.

## Constraints
- 1 <= n, m <= 5 * 10^4
- landStartTime.length == landDuration.length == n
- waterStartTime.length == waterDuration.length == m
- 1 <= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] <= 10^5

## Examples
### Example 1
- **Input:** `landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]`
- **Output:** `9`
- **Explanation:** ​​​​​​​ 

 
 Plan A (land ride 0 &rarr; water ride 0):
 
 Start land ride 0 at time landStartTime[0] = 2 . Finish at 2 + landDuration[0] = 6 . 
 Water ride 0 opens at time waterStartTime[0] = 6 . Start immediately at 6 , finish at 6 + waterDuration[0] = 9 . 
 
 
 Plan B (water ride 0 &rarr; land ride 1):
 
 Start water ride 0 at time waterStartTime[0] = 6 . Finish at 6 + waterDuration[0] = 9 . 
 Land ride 1 opens at landStartTime[1] = 8 . Start at time 9 , finish at 9 + landDuration[1] = 10 . 
 
 
 Plan C (land ride 1 &rarr; water ride 0):
 
 Start land ride 1 at time landStartTime[1] = 8 . Finish at 8 + landDuration[1] = 9 . 
 Water ride 0 opened at waterStartTime[0] = 6 . Start at time 9 , finish at 9 + waterDuration[0] = 12 . 
 
 
 Plan D (water ride 0 &rarr; land ride 0):
 
 Start water ride 0 at time waterStartTime[0] = 6 . Finish at 6 + waterDuration[0] = 9 . 
 Land ride 0 opened at landStartTime[0] = 2 . Start at time 9 , finish at 9 + landDuration[0] = 13 . 
 
 
 

 Plan A gives the earliest finish time of 9.

### Example 2
- **Input:** `landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]`
- **Output:** `14`
- **Explanation:** ​​​​​​​ 

 
 Plan A (water ride 0 &rarr; land ride 0):
 
 Start water ride 0 at time waterStartTime[0] = 1 . Finish at 1 + waterDuration[0] = 11 . 
 Land ride 0 opened at landStartTime[0] = 5 . Start immediately at 11 and finish at 11 + landDuration[0] = 14 . 
 
 
 Plan B (land ride 0 &rarr; water ride 0):
 
 Start land ride 0 at time landStartTime[0] = 5 . Finish at 5 + landDuration[0] = 8 . 
 Water ride 0 opened at waterStartTime[0] = 1 . Start immediately at 8 and finish at 8 + waterDuration[0] = 18 . 
 
 
 

 Plan A provides the earliest finish time of 14.

## Key Insight
Use two pointers moving toward each other or in parallel to process elements in a single pass without quadratic nested loops.

## Approach
To solve **Earliest Finish Time for Land and Water Rides II**, we observe the problem requirements and utilize the **Array / General** technique. We place two pointers at key reference points (typically start and end) and advance them inward based on condition evaluations. This linear convergence avoids quadratic comparisons.

## Algorithm
1. Initialize two pointers at opposite ends of the input.
2. Evaluate pointer elements and update running calculations.
3. Advance or retreat pointers conditionally until they meet.
4. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]`.
2. **Processing Steps:** We apply **Two Pointer Convergence & Scanning** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `9`.
4. **Verification:** ​​​​​​​ 

 
 Plan A (land ride 0 &rarr; water ride 0):
 
 Start land ride 0 at time landStartTime[0] = 2 . Finish at 2 + landDuration[0] = 6 . 
 Water ride 0 opens at time waterStartTime[0] = 6 . Start immediately at 6 , finish at 6 + waterDuration[0] = 9 . 
 
 
 Plan B (water ride 0 &rarr; land ride 1):
 
 Start water ride 0 at time waterStartTime[0] = 6 . Finish at 6 + waterDuration[0] = 9 . 
 Land ride 1 opens at landStartTime[1] = 8 . Start at time 9 , finish at 9 + landDuration[1] = 10 . 
 
 
 Plan C (land ride 1 &rarr; water ride 0):
 
 Start land ride 1 at time landStartTime[1] = 8 . Finish at 8 + landDuration[1] = 9 . 
 Water ride 0 opened at waterStartTime[0] = 6 . Start at time 9 , finish at 9 + waterDuration[0] = 12 . 
 
 
 Plan D (water ride 0 &rarr; land ride 0):
 
 Start water ride 0 at time waterStartTime[0] = 6 . Finish at 6 + waterDuration[0] = 9 . 
 Land ride 0 opened at landStartTime[0] = 2 . Start at time 9 , finish at 9 + landDuration[0] = 13 . 
 
 
 

 Plan A gives the earliest finish time of 9.

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
Java

## Source Code
- [solution.java](./solution.java)


```java
import java.util.*;

class Solution {
    public int earliestFinishTime(int[] landStartTime, int[] landDuration,
                                  int[] waterStartTime, int[] waterDuration) {

        long ans = Long.MAX_VALUE;

        // Land -> Water
        ans = Math.min(ans, solve(landStartTime, landDuration,
                                   waterStartTime, waterDuration));

        // Water -> Land
        ans = Math.min(ans, solve(waterStartTime, waterDuration,
                                   landStartTime, landDuration));

        return (int) ans;
    }

    private long solve(int[] start1, int[] duration1,
                       int[] start2, int[] duration2) {

        int n = start2.length;

        // Store {start time, duration}
        int[][] rides = new int[n][2];

        for (int i = 0; i < n; i++) {
            rides[i][0] = start2[i];
            rides[i][1] = duration2[i];
        }

        // Sort second rides by start time
        Arrays.sort(rides, Comparator.comparingInt(a -> a[0]));

        // prefixMin[i] = minimum duration among rides [0...i]
        int[] prefixMin = new int[n];
        prefixMin[0] = rides[0][1];

        for (int i = 1; i < n; i++) {
            prefixMin[i] = Math.min(prefixMin[i - 1], rides[i][1]);
        }

        // suffixMin[i] = minimum (start + duration) among rides [i...n-1]
        long[] suffixMin = new long[n];
        suffixMin[n - 1] = (long) rides[n - 1][0] + rides[n - 1][1];

        for (int i = n - 2; i >= 0; i--) {
            suffixMin[i] = Math.min(
                suffixMin[i + 1],
                (long) rides[i][0] + rides[i][1]
            );
        }

        long ans = Long.MAX_VALUE;

        for (int i = 0; i < start1.length; i++) {

            // Finish first ride
            long finish = (long) start1[i] + duration1[i];

            // Find first ride in second category
            // whose start time > finish
            int pos = upperBound(rides, finish);

            // Case 1:
            // Second ride is already open when first ride finishes.
            // Finish = finish + minimum duration
            if (pos > 0) {
                ans = Math.min(
                    ans,
                    finish + prefixMin[pos - 1]
                );
            }

            // Case 2:
            // Second ride opens after first ride finishes.
            // Finish = start + duration
            if (pos < n) {
                ans = Math.min(
                    ans,
                    suffixMin[pos]
                );
            }
        }

        return ans;
    }

    // First index where rides[index][0] > time
    private int upperBound(int[][] rides, long time) {
        int left = 0;
        int right = rides.length;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (rides[mid][0] <= time) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
}
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
- [3633. Earliest Finish Time for Land and Water Rides I](../../3501-4000/3965-earliest-finish-time-for-land-and-water-rides-i/)
- [1723. Find Minimum Time to Finish All Jobs](../../1501-2000/1825-find-minimum-time-to-finish-all-jobs/)
- [1900. The Earliest and Latest Rounds Where Players Compete](../../2001-2500/2028-the-earliest-and-latest-rounds-where-players-compete/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/)
