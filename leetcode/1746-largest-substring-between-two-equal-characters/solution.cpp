
class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        int first[26];
        fill(first, first + 26, -1);

        int maxLen = -1;

        for (int i = 0; i < s.size(); i++) {
            int index = s[i] - 'a';

            if (first[index] == -1) {
                first[index] = i;
            } else {
                maxLen = max(maxLen, i - first[index] - 1);
            }
        }

        return maxLen;
    }
};

