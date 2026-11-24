# LeetCode 1114: Print in Order

**LeetCode Problem #1114 — Print in Order**
Solve LeetCode Print in Order using Java and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Print in Order |
| LeetCode | #1114 |
| Difficulty | Easy |
| Language | Java |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Suppose we have a class:

public class Foo {
 public void first() { print("first"); }
 public void second() { print("second"); }
 public void third() { print("third"); }
}

The same instance of `Foo` will be passed to three different threads. Thread A will call `first()`, thread B will call `second()`, and thread C will call `third()`. Design a mechanism and modify the program to ensure that `second()` is executed after `first()`, and `third()` is executed after `second()`.

**Note:**

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

## Constraints
- `nums` is a permutation of `[1, 2, 3]`.

## Examples
### Example 1
- **Input:** `nums = [1,2,3]`
- **Output:** `"firstsecondthird"`
- **Explanation:** There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.

### Example 2
- **Input:** `nums = [1,3,2]`
- **Output:** `"firstsecondthird"`
- **Explanation:** The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
The code uses **Semaphores** (or equivalent synchronization) to enforce ordering.

1. Two semaphores control the gates: `sem1` (blocks `second`) and `sem2` (blocks `third`), both starting at `0`.
2. **first():** Prints "first", then releases `sem1`.
3. **second():** Waits on `sem1`, prints "second", then releases `sem2`.
4. **third():** Waits on `sem2`, then prints "third".

This chain of semaphores guarantees the correct order regardless of thread scheduling.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `nums = [1,2,3]`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"firstsecondthird"`.
4. **Verification:** There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.

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
Java

## Source Code
- [solution.java](./solution.java)


```java
import java.util.concurrent.Semaphore;

class Foo {

    private Semaphore second = new Semaphore(0);
    private Semaphore third = new Semaphore(0);

    public Foo() {
        
    }

    public void first(Runnable printFirst) throws InterruptedException {
        
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        
        second.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        
        second.acquire();
        
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        
        third.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
        
        third.acquire();
        
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
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
- [655. Print Binary Tree](../../0501-1000/0655-print-binary-tree/)
- [1115. Print FooBar Alternately](../../1001-1500/1115-print-foobar-alternately/)
- [1116. Print Zero Even Odd](../../1001-1500/1116-print-zero-even-odd/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/print-in-order/)
