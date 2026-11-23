import java.util.*;

class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        // Sort by start ascending.
        // If starts are equal, sort end descending.
        Arrays.sort(intervals, (a, b) -> {
            if (a[0] == b[0]) {
                return Integer.compare(b[1], a[1]);
            }
            return Integer.compare(a[0], b[0]);
        });

        int count = 0;
        int maxEnd = 0;

        for (int[] interval : intervals) {
            // This interval is not covered
            if (interval[1] > maxEnd) {
                count++;
                maxEnd = interval[1];
            }
        }

        return count;
    }
}
