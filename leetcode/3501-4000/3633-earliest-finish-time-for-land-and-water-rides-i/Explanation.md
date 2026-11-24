# LeetCode 3633: Earliest Finish Time for Land and Water Rides I

**LeetCode Problem #3633 — Earliest Finish Time for Land and Water Rides I**
Solve LeetCode Earliest Finish Time for Land and Water Rides I using Kotlin and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Earliest Finish Time for Land and Water Rides I |
| LeetCode | #3633 |
| Difficulty | Easy |
| Language | Kotlin |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
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
- 1 <= n, m <= 100
- landStartTime.length == landDuration.length == n
- waterStartTime.length == waterDuration.length == m
- 1 <= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] <= 1000

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
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Earliest Finish Time for Land and Water Rides I**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
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
**Array / General**

## Topics
- Array

## Language
Kotlin

## Source Code
- [solution.kt](./solution.kt)


```kotlin
class Solution {
    fun earliestFinishTime(
        landStartTime: IntArray,
        landDuration: IntArray,
        waterStartTime: IntArray,
        waterDuration: IntArray
    ): Int {
        var ans = Int.MAX_VALUE

        // Land ride first, then water ride
        for (i in landStartTime.indices) {
            val landFinish = landStartTime[i] + landDuration[i]

            for (j in waterStartTime.indices) {
                val waterFinish =
                    maxOf(landFinish, waterStartTime[j]) + waterDuration[j]

                ans = minOf(ans, waterFinish)
            }
        }

        // Water ride first, then land ride
        for (i in waterStartTime.indices) {
            val waterFinish = waterStartTime[i] + waterDuration[i]

            for (j in landStartTime.indices) {
                val landFinish =
                    maxOf(waterFinish, landStartTime[j]) + landDuration[j]

                ans = minOf(ans, landFinish)
            }
        }

        return ans
    }
}
```

## Why This Works
By utilizing **Array / General**, each element is processed efficiently, ensuring optimal performance while avoiding unnecessary re-computations.

## Common Mistakes
1. Missing edge cases (empty inputs, boundary limits, negative values).
2. Off-by-one errors in loop conditions.
3. TLE due to suboptimal data structure choices.

## Interview Notes
- **Tests:** Fundamental DSA concepts, problem analysis, and edge-case handling.
- **Follow-up:** How would you scale this solution for large input streams?

## Related Problems
- [3635. Earliest Finish Time for Land and Water Rides II](../../3501-4000/3635-earliest-finish-time-for-land-and-water-rides-ii/)
- [1723. Find Minimum Time to Finish All Jobs](../../1501-2000/1723-find-minimum-time-to-finish-all-jobs/)
- [1162. As Far from Land as Possible](../../1001-1500/1162-as-far-from-land-as-possible/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/)
