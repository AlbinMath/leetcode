# LeetCode 1115: Print FooBar Alternately

**LeetCode Problem #1115 — Print FooBar Alternately**
Solve LeetCode Print FooBar Alternately using Java and Hash Map. This solution finds the optimal result using Complement Lookup / Hash Table Frequency in O(n) time.

## Problem Information
| Property | Value |
|---|---|
| Problem | Print FooBar Alternately |
| LeetCode | #1115 |
| Difficulty | Medium |
| Language | Java |
| Algorithm | Complement Lookup / Hash Table Frequency |
| Data Structure | Dictionary / Hash Map |
| Pattern | Hash Map |
| Time Complexity | O(n) |
| Space Complexity | O(n) |

## Problem Statement
Suppose you are given the following code:

class FooBar {
 public void foo() {
 for (int i = 0; i < n; i++) {
 print("foo");
 }
 }

public void bar() {
 for (int i = 0; i < n; i++) {
 print("bar");
 }
 }
}

The same instance of `FooBar` will be passed to two different threads:

thread `A` will call `foo()`, while 
 thread `B` will call `bar()`.

Modify the given program to output `"foobar"` `n` times.

## Constraints
- `1 <= n <= 1000`

## Examples
### Example 1
- **Input:** `n = 1`
- **Output:** `"foobar"`
- **Explanation:** There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar().
"foobar" is being output 1 time.

### Example 2
- **Input:** `n = 2`
- **Output:** `"foobarfoobar"`
- **Explanation:** "foobar" is being output 2 times.

## Key Insight
Store previously seen elements or their frequencies in a hash map to achieve instant $O(1)$ lookup rather than nested $O(n^2)$ iterations.

## Approach
The code uses **Semaphores** for synchronization.

1. `fooSem` starts at `1` (foo can go first) and `barSem` starts at `0` (bar must wait).
2. **foo thread:** Acquires `fooSem`, prints "foo", then releases `barSem` (allowing bar to proceed).
3. **bar thread:** Acquires `barSem`, prints "bar", then releases `fooSem` (allowing foo to proceed again).

This ping-pong of semaphores ensures strict alternation for `n` iterations.

## Algorithm
1. Initialize state variables / data structure (**Dictionary / Hash Map**).
2. Process elements sequentially using **Complement Lookup / Hash Table Frequency**.
3. Validate boundary conditions and return optimal result.

## Example Walkthrough
1. **Input State:** We begin with `n = 1`.
2. **Processing Steps:** We apply **Complement Lookup / Hash Table Frequency** using our **Dictionary / Hash Map**:
   - Initialize the state according to the problem setup.
   - Trace intermediate operations and invariant checks.
3. **Result:** Arrive at the expected output `"foobar"`.
4. **Verification:** There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar().
"foobar" is being output 1 time.

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
class FooBar {
    private int n;
    private boolean fooTurn = true;

    public FooBar(int n) {
        this.n = n;
    }

    public synchronized void foo(Runnable printFoo) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            
            while (!fooTurn) {
                wait();
            }

            // printFoo.run() outputs "foo". Do not change or remove this line.
            printFoo.run();

            fooTurn = false;
            notifyAll();
        }
    }

    public synchronized void bar(Runnable printBar) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            
            while (fooTurn) {
                wait();
            }

            // printBar.run() outputs "bar". Do not change or remove this line.
            printBar.run();

            fooTurn = true;
            notifyAll();
        }
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
- [1114. Print in Order](../../1001-1500/1203-print-in-order/)
- [1116. Print Zero Even Odd](../../1001-1500/1216-print-zero-even-odd/)

## LeetCode
[View problem on LeetCode](https://leetcode.com/problems/print-foobar-alternately/)
