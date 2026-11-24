# LeetCode 2069: Walking Robot Simulation II

**LeetCode Problem #2069 — Walking Robot Simulation II**
Solve LeetCode Walking Robot Simulation II using JavaScript and Array / General. This solution finds the optimal result using In-Place Array Traversal & Index Mapping in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Walking Robot Simulation II |
| LeetCode | #2069 |
| Difficulty | Medium |
| Language | JavaScript |
| Algorithm | In-Place Array Traversal & Index Mapping |
| Data Structure | Array |
| Pattern | Array / General |
| Time Complexity | O(n) |
| Space Complexity | O(1) |

## Problem Statement
A `width x height` grid is on an XY-plane with the **bottom-left** cell at `(0, 0)` and the **top-right** cell at `(width - 1, height - 1)`. The grid is aligned with the four cardinal directions (`"North"`, `"East"`, `"South"`, and `"West"`). A robot is **initially** at cell `(0, 0)` facing direction `"East"`.

The robot can be instructed to move for a specific number of **steps**. For each step, it does the following.

Attempts to move **forward one** cell in the direction it is facing. 
 If the cell the robot is **moving to** is **out of bounds**, the robot instead **turns** 90 degrees **counterclockwise** and retries the step.

After the robot finishes moving the number of steps required, it stops and awaits the next instruction.

Implement the `Robot` class:

`Robot(int width, int height)` Initializes the `width x height` grid with the robot at `(0, 0)` facing `"East"`. 
 `void step(int num)` Instructs the robot to move forward `num` steps. 
 `int[] getPos()` Returns the current cell the robot is at, as an array of length 2, `[x, y]`. 
 `String getDir()` Returns the current direction of the robot, `"North"`, `"East"`, `"South"`, or `"West"`.

## Constraints
- `2 <= width, height <= 100`
- `1 <= num <= 10^5`
- At most `10^4` calls **in total** will be made to `step`, `getPos`, and `getDir`.

## Examples
### Example 1
- **Input:** `["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]`
- **Output:** `[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]`
- **Explanation:** Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
robot.step(2); // It moves two steps East to (2, 0), and faces East.
robot.step(2); // It moves two steps East to (4, 0), and faces East.
robot.getPos(); // return [4, 0]
robot.getDir(); // return "East"
robot.step(2); // It moves one step East to (5, 0), and faces East.
 // Moving the next step East would be out of bounds, so it turns and faces North.
 // Then, it moves one step North to (5, 1), and faces North.
robot.step(1); // It moves one step North to (5, 2), and faces

## Key Insight
Leverage **Array / General** with **Array** to process inputs efficiently and achieve optimal time and space complexity.

## Approach
To solve **Walking Robot Simulation II**, we observe the problem requirements and utilize the **Array / General** technique. We iterate through the inputs using **In-Place Array Traversal & Index Mapping**, leveraging a **Array** to efficiently manage state and achieve optimal complexity.

## Algorithm
1. Initialize state variables and the **Array**.
2. Iterate through elements, applying the transformation or evaluation logic.
3. Validate boundary conditions and return the final computed result.

## Example Walkthrough
1. **Input State:** We begin with `["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]`.
2. **Processing Steps:** We apply **In-Place Array Traversal & Index Mapping** using our **Array**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]`.
4. **Verification:** Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
robot.step(2); // It moves two steps East to (2, 0), and faces East.
robot.step(2); // It moves two steps East to (4, 0), and faces East.
robot.getPos(); // return [4, 0]
robot.getDir(); // return "East"
robot.step(2); // It moves one step East to (5, 0), and faces East.
 // Moving the next step East would be out of bounds, so it turns and faces North.
 // Then, it moves one step North to (5, 1), and faces North.
robot.step(1); // It moves one step North to (5, 2), and faces

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
var Robot = function(width, height) {
    this.cells = [];
    this.dirs = [];
    this.pos = 0;
    this.moved = false;
    for (let x = 0; x < width; x++) {
        this.cells.push([x, 0]);
        this.dirs.push("East");
    }
    for (let y = 1; y < height; y++) {
        this.cells.push([width - 1, y]);
        this.dirs.push("North");
    }
    for (let x = width - 2; x >= 0; x--) {
        this.cells.push([x, height - 1]);
        this.dirs.push("West");
    }
    for (let y = height - 2; y >= 1; y--) {
        this.cells.push([0, y]);
        this.dirs.push("South");
    }
    this.dirs[0] = "South";
};
Robot.prototype.step = function(num) {
    this.moved = true;
    this.pos = (this.pos + num) % this.cells.length;
};
Robot.prototype.getPos = function() {
    return this.cells[this.pos];
};
Robot.prototype.getDir = function() {
    if (!this.moved) return "East";
    return this.dirs[this.pos];
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
- [874. Walking Robot Simulation](../../0501-1000/0874-walking-robot-simulation/)
- [657. Robot Return to Origin](../../0501-1000/0657-robot-return-to-origin/)
- [1041. Robot Bounded In Circle](../../1001-1500/1041-robot-bounded-in-circle/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/walking-robot-simulation-ii/)
