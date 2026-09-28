class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        vector<int> cnt(26, 0);

        for (char c : s) {
            cnt[c - 'a']++;
        }

        string ans;

        // Try to construct a permutation that is
        // strictly greater than target.
        for (int i = 0; i < (int)target.size(); i++) {

            // Try to put target[i] here first.
            int t = target[i] - 'a';

            // Case 1: We can continue equal to target.
            if (cnt[t] > 0) {
                cnt[t]--;
                ans += target[i];
                continue;
            }

            // Case 2: Cannot stay equal.
            // We need a character greater than target[i].
            for (int c = t + 1; c < 26; c++) {
                if (cnt[c] > 0) {
                    ans += char('a' + c);
                    cnt[c]--;

                    // Fill the rest with smallest characters.
                    for (int x = 0; x < 26; x++) {
                        while (cnt[x] > 0) {
                            ans += char('a' + x);
                            cnt[x]--;
                        }
                    }

                    return ans;
                }
            }

            // No greater character at this position.
            // We must backtrack.
            break;
        }

        /*
         * We reached a point where matching target is impossible.
         * Backtrack through ans and find the rightmost position
         * where we can replace the chosen character with something
         * larger.
         */
        for (int i = (int)ans.size() - 1; i >= 0; i--) {
            cnt[ans[i] - 'a']++;

            int cur = ans[i] - 'a';

            for (int c = cur + 1; c < 26; c++) {
                if (cnt[c] > 0) {
                    string res = ans.substr(0, i);
                    res += char('a' + c);
                    cnt[c]--;

                    // Fill remaining positions minimally.
                    for (int x = 0; x < 26; x++) {
                        while (cnt[x] > 0) {
                            res += char('a' + x);
                            cnt[x]--;
                        }
                    }

                    return res;
                }
            }
        }

        return "";
    }
};
