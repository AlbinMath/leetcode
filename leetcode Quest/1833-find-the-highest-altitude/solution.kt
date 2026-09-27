class Solution {
    fun largestAltitude(gain: IntArray): Int {
        var altitude = 0
        var highest = 0

        for (g in gain) {
            altitude += g
            highest = maxOf(highest, altitude)
        }

        return highest
    }
}
