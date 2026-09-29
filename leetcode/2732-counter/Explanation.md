# Counter

## Problem Explanation
Create a function that returns a counter function. Each time the counter is called, it returns the next incremented value starting from `n`.

## How the Code Works
Uses a **closure** to capture and increment a variable `n`. Each call to the returned function returns `n++`, which returns the current value and then increments it for the next call.
