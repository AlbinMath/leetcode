class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """

        # Building 1 must have height 0
        restrictions.append([1, 0])

        # Sort restrictions by building ID
        restrictions.sort()

        m = len(restrictions)

        # Left to right:
        # A building cannot exceed the previous
        # restricted height + distance.
        for i in range(1, m):
            distance = restrictions[i][0] - restrictions[i - 1][0]

            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + distance
            )

        # Right to left:
        # Apply restrictions from the right side.
        for i in range(m - 2, -1, -1):
            distance = restrictions[i + 1][0] - restrictions[i][0]

            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + distance
            )

        answer = 0

        # Calculate maximum possible height between
        # consecutive restricted buildings.
        for i in range(1, m):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            distance = x2 - x1

            # Highest possible peak between x1 and x2
            peak = (h1 + h2 + distance) // 2

            answer = max(answer, peak)

        # After the last restricted building,
        # heights can increase by 1 each step.
        last_id, last_height = restrictions[-1]

        answer = max(
            answer,
            last_height + (n - last_id)
        )

        return answer
