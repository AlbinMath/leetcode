class Solution {
public:
    string smallestPalindrome(string s) {
        vector<int> freq(26, 0);

        for (char c : s) {
            freq[c - 'a']++;
        }

        string left = "";

        for (int i = 0; i < 26; i++) {
            left += string(freq[i] / 2, 'a' + i);
        }

        string right = left;
        reverse(right.begin(), right.end());

        char middle = 0;
        if (s.size() % 2 == 1) {
            for (int i = 0; i < 26; i++) {
                if (freq[i] % 2) {
                    middle = 'a' + i;
                    break;
                }
            }
        }

        return left + (middle ? string(1, middle) : "") + right;
    }
};
