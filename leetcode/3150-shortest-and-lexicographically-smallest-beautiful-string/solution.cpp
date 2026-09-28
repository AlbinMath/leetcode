class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        int n = s.size();

        int ones = 0;
        int left = 0;

        int bestLen = INT_MAX;
        string ans = "";

        for (int right = 0; right < n; right++) {
            if (s[right] == '1')
                ones++;

            // Keep exactly k ones
            while (ones > k) {
                if (s[left] == '1')
                    ones--;
                left++;
            }

            // We have exactly k ones
            if (ones == k) {
                // Remove unnecessary leading zeros
                while (left <= right && s[left] == '0')
                    left++;

                int len = right - left + 1;
                string cur = s.substr(left, len);

                if (len < bestLen) {
                    bestLen = len;
                    ans = cur;
                }
                else if (len == bestLen && cur < ans) {
                    ans = cur;
                }
            }
        }

        return ans;
    }
};
