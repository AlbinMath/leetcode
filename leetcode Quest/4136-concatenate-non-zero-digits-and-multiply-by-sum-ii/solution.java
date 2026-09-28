class Solution {
    public int[] sumAndMultiply(String s, int[][] queries) {
        final long MOD = 1_000_000_007L;
        int n = s.length();

        // prefixNum[i] = value formed by non-zero digits in s[0..i-1]
        long[] prefixNum = new long[n + 1];

        // prefixSum[i] = sum of non-zero digits in s[0..i-1]
        long[] prefixSum = new long[n + 1];

        // prefixCount[i] = number of non-zero digits in s[0..i-1]
        int[] prefixCount = new int[n + 1];

        for (int i = 0; i < n; i++) {
            int digit = s.charAt(i) - '0';

            prefixNum[i + 1] = prefixNum[i];
            prefixSum[i + 1] = prefixSum[i];
            prefixCount[i + 1] = prefixCount[i];

            if (digit != 0) {
                prefixNum[i + 1] =
                    (prefixNum[i] * 10 + digit) % MOD;

                prefixSum[i + 1] += digit;
                prefixCount[i + 1]++;
            }
        }

        int[] answer = new int[queries.length];

        for (int q = 0; q < queries.length; q++) {
            int l = queries[q][0];
            int r = queries[q][1];

            // Number of non-zero digits in [l, r]
            int count = prefixCount[r + 1] - prefixCount[l];

            if (count == 0) {
                answer[q] = 0;
                continue;
            }

            // Sum of non-zero digits
            long sum = prefixSum[r + 1] - prefixSum[l];

            // To extract the concatenated number from the prefix,
            // remove the digits before l.
            long x;

            if (prefixCount[l] == 0) {
                x = prefixNum[r + 1];
            } else {
                long power = modPow(10, count);

                x = (prefixNum[r + 1]
                        - prefixNum[l] * power % MOD
                        + MOD) % MOD;
            }

            answer[q] = (int) (x * (sum % MOD) % MOD);
        }

        return answer;
    }

    private long modPow(long base, int exp) {
        final long MOD = 1_000_000_007L;
        long result = 1;

        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = result * base % MOD;
            }

            base = base * base % MOD;
            exp >>= 1;
        }

        return result;
    }
}
