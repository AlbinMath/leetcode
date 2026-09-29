# Angle Between Hands Of A Clock

## Problem Explanation
Given two numbers `hour` and `minutes`, return the smaller angle (in degrees) formed between the hour and the minute hand of a clock.

## How the Code Works
1. **Minute Hand Angle:** Each minute moves the minute hand by `6°` → `minuteAngle = minutes * 6.0`.
2. **Hour Hand Angle:** Each hour moves the hour hand by `30°`, and each minute moves it by `0.5°` → `hourAngle = (hour % 12) * 30.0 + minutes * 0.5`.
3. **Angle Between:** The absolute difference gives one angle. The other angle is `360 - difference`. Return the smaller of the two.

Time and space complexity are both $O(1)$.
