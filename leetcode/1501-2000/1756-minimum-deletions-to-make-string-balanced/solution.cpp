#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minimumDeletions(string s) {
        int deletions = 0;
        int b_count = 0;
        
        for (char c : s) {
            if (c == 'b') {
                b_count++;
            } else {
                // Either delete this 'a' (deletions + 1) or delete all previous 'b's (b_count)
                deletions = min(deletions + 1, b_count);
            }
        }
        
        return deletions;
    }
};
