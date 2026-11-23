#include <string>
using namespace std;

class Solution {
public:
    int minLength(string s) {
        int top = 0; // Acts as the size/write-pointer of our in-place stack
        
        for (char c : s) {
            if (top > 0 && ((c == 'B' && s[top - 1] == 'A') || 
                            (c == 'D' && s[top - 1] == 'C'))) {
                top--; // Pop matching 'A' or 'C'
            } else {
                s[top++] = c; // Push current character
            }
        }
        
        return top;
    }
};
