class Solution {
    public long findKthSmallest(int[] coins, int k) {
        long left = 1;
        long right = (long) coins[0] * k;

        for (int coin : coins) {
            right = Math.min(right, (long) coin * k);
        }

        while (left < right) {
            long mid = left + (right - left) / 2;

            if (count(mid, coins) >= k) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    private long count(long x, int[] coins) {
        return dfs(0, x, 1, coins, 0);
    }

    private long dfs(int index, long x, long lcm,
                     int[] coins, int chosen) {

        long result = 0;

        for (int i = index; i < coins.length; i++) {
            long newLcm = lcm(lcm, coins[i]);

            // LCM is already larger than x, so no multiple exists
            if (newLcm > x) {
                continue;
            }

            long multiples = x / newLcm;

            if ((chosen & 1) == 0) {
                result += multiples;
            } else {
                result -= multiples;
            }

            result += dfs(i + 1, x, newLcm, coins, chosen + 1);
        }

        return result;
    }

    private long gcd(long a, long b) {
        while (b != 0) {
            long temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }

    private long lcm(long a, long b) {
        long g = gcd(a, b);
        return a / g * b;
    }
}
