#include <string>
using namespace std;

class Solution {
public:
    long long countValidSubstrings(string s) {
        long long total = 0;
        int last_a = -1;
        int last_ab = -1;
        int invalid_start = -1; // Latest index i such that s[i..right] has subsequence "abc"
        
        for (int right = 0; right < (int)s.length(); ++right) {
            if (s[right] == 'a') {
                last_a = right;
            } else if (s[right] == 'b') {
                if (last_a != -1) {
                    last_ab = last_a;
                }
            } else if (s[right] == 'c') {
                if (last_ab != -1) {
                    invalid_start = last_ab;
                }
            }
            // Valid substrings ending at `right` start from (invalid_start + 1) to right
            total += (right - invalid_start);
        }
        
        return total;
    }
};
