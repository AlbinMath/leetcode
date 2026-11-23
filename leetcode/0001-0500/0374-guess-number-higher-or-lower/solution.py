# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          0 if num is equal to the picked number

class Solution:
    def guessNumber(self, n):
        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2

            result = guess(mid)

            if result == 0:
                return mid

            elif result == -1:
                # Our guess is too high
                right = mid - 1

            else:
                # Our guess is too low
                left = mid + 1
