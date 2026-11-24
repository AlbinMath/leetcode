
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            # Swapping identical characters keeps the string unchanged
            return len(set(s)) < len(s)

        differences = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                differences.append(i)

        # Exactly two positions must differ
        if len(differences) != 2:
            return False

        i, j = differences

        # Swapping these two characters must produce goal
        return s[i] == goal[j] and s[j] == goal[i]

