class Solution {
    fun earliestFinishTime(
        landStartTime: IntArray,
        landDuration: IntArray,
        waterStartTime: IntArray,
        waterDuration: IntArray
    ): Int {
        var ans = Int.MAX_VALUE

        // Land ride first, then water ride
        for (i in landStartTime.indices) {
            val landFinish = landStartTime[i] + landDuration[i]

            for (j in waterStartTime.indices) {
                val waterFinish =
                    maxOf(landFinish, waterStartTime[j]) + waterDuration[j]

                ans = minOf(ans, waterFinish)
            }
        }

        // Water ride first, then land ride
        for (i in waterStartTime.indices) {
            val waterFinish = waterStartTime[i] + waterDuration[i]

            for (j in landStartTime.indices) {
                val landFinish =
                    maxOf(waterFinish, landStartTime[j]) + landDuration[j]

                ans = minOf(ans, landFinish)
            }
        }

        return ans
    }
}
