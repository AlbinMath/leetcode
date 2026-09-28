class Solution {
    public int numberOfSubstrings(String s) {
        int[] last = {-1, -1, -1};
        int ans = 0;

        for (int right = 0; right < s.length(); right++) {
            int index = s.charAt(right) - 'a';
            last[index] = right;

            // All three characters have appeared
            if (last[0] != -1 && last[1] != -1 && last[2] != -1) {
                int minLast = Math.min(last[0],
                              Math.min(last[1], last[2]));

                ans += minLast + 1;
            }
        }

        return ans;
    }
}
