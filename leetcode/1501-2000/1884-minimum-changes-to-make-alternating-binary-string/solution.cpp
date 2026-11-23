
class Solution {
public:
    int minOperations(string s) {
        int count1 = 0;
        int count2 = 0;

        for (int i = 0; i < s.size(); i++) {
            // Pattern 1: 010101...
            if (i % 2 == 0) {
                if (s[i] != '0') count1++;
                if (s[i] != '1') count2++;
            }
            // Pattern 2: 101010...
            else {
                if (s[i] != '1') count1++;
                if (s[i] != '0') count2++;
            }
        }

        return min(count1, count2);
    }
};

