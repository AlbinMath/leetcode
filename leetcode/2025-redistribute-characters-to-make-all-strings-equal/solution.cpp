
class Solution {
public:
    bool makeEqual(vector<string>& words) {
        int count[26] = {0};
        int n = words.size();

        for (string word : words) {
            for (char c : word) {
                count[c - 'a']++;
            }
        }

        for (int i = 0; i < 26; i++) {
            if (count[i] % n != 0) {
                return false;
            }
        }

        return true;
    }
};

