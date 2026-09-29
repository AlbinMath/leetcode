# Valid Phone Numbers

## Problem Explanation
Given a file `file.txt` that contains a list of phone numbers (one per line), write a one-liner bash command to print all valid phone numbers. A valid phone number must be in one of these two formats:
- `(xxx) xxx-xxxx`
- `xxx-xxx-xxxx`
where `x` represents a digit.

## How the Code Works
The solution uses `grep -E` (extended regular expressions) to match lines that conform to one of the two valid formats:
- `^([0-9]{3}-[0-9]{3}-[0-9]{4})$` matches the format `xxx-xxx-xxxx`.
- `^(\([0-9]{3}\) [0-9]{3}-[0-9]{4})$` matches the format `(xxx) xxx-xxxx`.
- The `^` and `$` anchors ensure the entire line must match (no extra characters before or after).
- The `|` operator combines both patterns so either format is accepted.
