class Solution {
public:
    vector<int> validSequence(string word1, string word2) {
        int n = word1.size();
        int m = word2.size();

        // suf[i] = first unmatched position in word2
        // after matching word1[i...n-1] from right to left.
        vector<int> suf(n + 1);
        suf[n] = m;

        int j = m - 1;

        for (int i = n - 1; i >= 0; i--) {
            if (j >= 0 && word1[i] == word2[j]) {
                j--;
            }

            suf[i] = j + 1;
        }

        vector<int> ans;

        bool changed = false;
        j = 0;

        for (int i = 0; i < n; i++) {
            if (j == m)
                break;

            // Normal matching
            if (word1[i] == word2[j]) {
                ans.push_back(i);
                j++;
            }
            // Use the one allowed mismatch
            else if (!changed && suf[i + 1] <= j + 1) {
                ans.push_back(i);
                j++;
                changed = true;
            }
        }

        if (j == m)
            return ans;

        return {};
    }
};

