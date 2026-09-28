import java.util.*;

class Solution {
    public int earliestFinishTime(int[] landStartTime, int[] landDuration,
                                  int[] waterStartTime, int[] waterDuration) {

        long ans = Long.MAX_VALUE;

        // Land -> Water
        ans = Math.min(ans, solve(landStartTime, landDuration,
                                   waterStartTime, waterDuration));

        // Water -> Land
        ans = Math.min(ans, solve(waterStartTime, waterDuration,
                                   landStartTime, landDuration));

        return (int) ans;
    }

    private long solve(int[] start1, int[] duration1,
                       int[] start2, int[] duration2) {

        int n = start2.length;

        // Store {start time, duration}
        int[][] rides = new int[n][2];

        for (int i = 0; i < n; i++) {
            rides[i][0] = start2[i];
            rides[i][1] = duration2[i];
        }

        // Sort second rides by start time
        Arrays.sort(rides, Comparator.comparingInt(a -> a[0]));

        // prefixMin[i] = minimum duration among rides [0...i]
        int[] prefixMin = new int[n];
        prefixMin[0] = rides[0][1];

        for (int i = 1; i < n; i++) {
            prefixMin[i] = Math.min(prefixMin[i - 1], rides[i][1]);
        }

        // suffixMin[i] = minimum (start + duration) among rides [i...n-1]
        long[] suffixMin = new long[n];
        suffixMin[n - 1] = (long) rides[n - 1][0] + rides[n - 1][1];

        for (int i = n - 2; i >= 0; i--) {
            suffixMin[i] = Math.min(
                suffixMin[i + 1],
                (long) rides[i][0] + rides[i][1]
            );
        }

        long ans = Long.MAX_VALUE;

        for (int i = 0; i < start1.length; i++) {

            // Finish first ride
            long finish = (long) start1[i] + duration1[i];

            // Find first ride in second category
            // whose start time > finish
            int pos = upperBound(rides, finish);

            // Case 1:
            // Second ride is already open when first ride finishes.
            // Finish = finish + minimum duration
            if (pos > 0) {
                ans = Math.min(
                    ans,
                    finish + prefixMin[pos - 1]
                );
            }

            // Case 2:
            // Second ride opens after first ride finishes.
            // Finish = start + duration
            if (pos < n) {
                ans = Math.min(
                    ans,
                    suffixMin[pos]
                );
            }
        }

        return ans;
    }

    // First index where rides[index][0] > time
    private int upperBound(int[][] rides, long time) {
        int left = 0;
        int right = rides.length;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (rides[mid][0] <= time) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
}
