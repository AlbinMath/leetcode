import java.util.*;

class Solution {
    public int maximumLength(int[] nums) {
        Map<Long, Integer> freq = new HashMap<>();

        for (int num : nums) {
            long x = num;
            freq.put(x, freq.getOrDefault(x, 0) + 1);
        }

        int ans = 1;

        for (long x : freq.keySet()) {

            // Special case: all elements are 1
            if (x == 1) {
                int count = freq.get(1L);

                // Length must be odd
                if (count % 2 == 0) {
                    count--;
                }

                ans = Math.max(ans, count);
                continue;
            }

            // x must appear at least twice
            if (freq.get(x) < 2) {
                continue;
            }

            int len = 1;
            long cur = x;

            while (true) {
                // Prevent overflow
                if (cur > 1_000_000_000L / cur) {
                    break;
                }

                long next = cur * cur;

                Integer count = freq.get(next);

                // next doesn't exist
                if (count == null) {
                    break;
                }

                // One copy is enough for the center
                len += 2;

                // Only one copy -> this is the center
                if (count < 2) {
                    break;
                }

                // Two copies -> can continue
                cur = next;
            }

            ans = Math.max(ans, len);
        }

        return ans;
    }
}
