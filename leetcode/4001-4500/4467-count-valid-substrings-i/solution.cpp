#include <string>
using namespace std;

class Solution {
public:
    long long countValidSubstrings(string s) {
        long long total = 0;
        int left = 0;
        int n = s.length();
        
        for (int right = 0; right < n; ++right) {
            // If the last 3 characters form "abc", shrink the window
            if (right >= 2 && s[right - 2] == 'a' && s[right - 1] == 'b' && s[right] == 'c') {
                left = right - 1;
            }
            // All substrings starting between left and right and ending at right are valid
            total += (right - left + 1);
        }
        
        return total;
    }
};
