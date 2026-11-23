# LeetCode 2960: Count Tested Devices After Test Operations

**LeetCode Problem #2960 — Count Tested Devices After Test Operations**
Solve LeetCode Count Tested Devices After Test Operations using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Count Tested Devices After Test Operations |
| LeetCode | #2960 |
| Difficulty | Easy |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
You are given a **0-indexed** integer array `batteryPercentages` having length `n`, denoting the battery percentages of `n` **0-indexed** devices.

Your task is to test each device `i` **in order** from `0` to `n - 1`, by performing the following test operations:

If `batteryPercentages[i]` is **greater** than `0`:

**Increment** the count of tested devices. 
 **Decrease** the battery percentage of all devices with indices `j` in the range `[i + 1, n - 1]` by `1`, ensuring their battery percentage **never goes below** `0`, i.e, `batteryPercentages[j] = max(0, batteryPercentages[j] - 1)`. 
 Move to the next device. 
 
 
 Otherwise, move to the next device without performing any test.

Return *an integer denoting the number of devices that will be tested after performing the test operations in order.*

## Constraints
- `1 <= n == batteryPercentages.length <= 100 `
- `0 <= batteryPercentages[i] <= 100`

## Examples
### Example 1
- **Input:** `batteryPercentages = [1,1,2,1,3]`
- **Output:** `3`
- **Explanation:** Performing the test operations in order starting from device 0:
At device 0, batteryPercentages[0] > 0, so there is now 1 tested device, and batteryPercentages becomes [1,0,1,0,2].
At device 1, batteryPercentages[1] == 0, so we move to the next device without testing.
At device 2, batteryPercentages[2] > 0, so there are now 2 tested devices, and batteryPercentages becomes [1,0,1,0,1].
At device 3, batteryPercentages[3] == 0, so we move to the next device without testing.
At device 4, batteryPercentages[4] > 0, so there are now 3 tested devices, and batteryPercentages stays the same.
So, the answer is 3.

### Example 2
- **Input:** `batteryPercentages = [0,1,2]`
- **Output:** `2`
- **Explanation:** Performing the test operations in order starting from device 0:
At device 0, batteryPercentages[0] == 0, so we move to the next device without testing.
At device 1, batteryPercentages[1] > 0, so there is now 1 tested device, and batteryPercentages becomes [0,1,1].
At device 2, batteryPercentages[2] > 0, so there are now 2 tested devices, and batteryPercentages stays the same.
So, the answer is 2.

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Count Tested Devices After Test Operations**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `batteryPercentages = [1,1,2,1,3]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `3`.
4. **Verification:** Performing the test operations in order starting from device 0:
At device 0, batteryPercentages[0] > 0, so there is now 1 tested device, and batteryPercentages becomes [1,0,1,0,2].
At device 1, batteryPercentages[1] == 0, so we move to the next device without testing.
At device 2, batteryPercentages[2] > 0, so there are now 2 tested devices, and batteryPercentages becomes [1,0,1,0,1].
At device 3, batteryPercentages[3] == 0, so we move to the next device without testing.
At device 4, batteryPercentages[4] > 0, so there are now 3 tested devices, and batteryPercentages stays the same.
So, the answer is 3.

## Complexity Analysis
- **Time Complexity:** O(n) — The algorithm processes input elements in optimal amortized time.
- **Space Complexity:** O(1) — Memory footprint corresponds to auxiliary storage for Array.

## Pattern
**Array / General**

## Topics
- Array

## Language
JavaScript

## Source Code
- [solution.js](./solution.js)


```javascript
var countTestedDevices = function(batteryPercentages) {
    let tested = 0;
    for (const battery of batteryPercentages) {
        if (battery > tested) {
            tested++;
        }
    }
    return tested;
};
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
- [3420. Count Non-Decreasing Subarrays After K Operations](../../3501-4000/3674-count-non-decreasing-subarrays-after-k-operations/)
- [1625. Lexicographically Smallest String After Applying Operations](../../1501-2000/1747-lexicographically-smallest-string-after-applying-operations/)
- [1722. Minimize Hamming Distance After Swap Operations](../../1501-2000/1840-minimize-hamming-distance-after-swap-operations/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/count-tested-devices-after-test-operations/)
