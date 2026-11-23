class Solution {
    fun arrayRankTransform(arr: IntArray): IntArray {
        val sorted = arr.clone()
        sorted.sort()

        val rank = HashMap<Int, Int>()
        var r = 1

        for (num in sorted) {
            if (!rank.containsKey(num)) {
                rank[num] = r
                r++
            }
        }

        return IntArray(arr.size) { i ->
            rank[arr[i]]!!
        }
    }
}
