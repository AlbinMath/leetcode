class Solution {
public:
    int maxActiveSectionsAfterTrade(string s) {
        int n = s.size();

        // Number of existing 1s
        int base = count(s.begin(), s.end(), '1');

        // Augmented string
        string t = "1" + s + "1";

        int ans = base;

        int i = 1;

        while (i < n + 1) {
            // Skip 0s
            if (t[i] == '0') {
                i++;
                continue;
            }

            // Find a block of 1s
            int l = i;

            while (i < n + 1 && t[i] == '1') {
                i++;
            }

            int r = i - 1;

            // This 1-block must be surrounded by 0s
            if (l > 1 && r < n &&
                t[l - 1] == '0' &&
                t[r + 1] == '0') {

                // Count zeros on the left
                int left = l - 1;
                while (left >= 0 && t[left] == '0') {
                    left--;
                }

                int leftZeros = l - left - 1;

                // Count zeros on the right
                int right = r + 1;
                while (right < n + 2 && t[right] == '0') {
                    right++;
                }

                int rightZeros = right - r - 1;

                // After the trade, these two zero blocks
                // become active.
                ans = max(ans, base + leftZeros + rightZeros);
            }
        }

        return ans;
    }
};
