class Solution {
    fun minimumCost(cost: IntArray): Int {
        cost.sort()

        var total = 0
        var i = cost.size - 1

        while (i >= 0) {
            total += cost[i]

            if (i - 1 >= 0) {
                total += cost[i - 1]
            }

            // Third candy is free
            i -= 3
        }

        return total
    }
}
