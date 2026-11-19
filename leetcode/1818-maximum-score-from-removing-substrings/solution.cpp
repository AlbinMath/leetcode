#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maximumGain(string s, int x, int y) {
        char first = 'a', second = 'b';
        // Ensure `first + second` is always the higher-scoring pair
        if (y > x) {
            swap(x, y);
            swap(first, second);
        }
        
        int total_score = 0;
        int first_cnt = 0;
        int second_cnt = 0;
        
        for (char c : s) {
            if (c == first) {
                first_cnt++;
            } else if (c == second) {
                if (first_cnt > 0) {
                    // Greedily form the high-value pair immediately
                    first_cnt--;
                    total_score += x;
                } else {
                    second_cnt++;
                }
            } else {
                // Non-'a'/'b' character acts as a wall; pair leftover characters for `y`
                total_score += min(first_cnt, second_cnt) * y;
                first_cnt = 0;
                second_cnt = 0;
            }
        }
        
        // Pair any remaining characters after the last wall
        total_score += min(first_cnt, second_cnt) * y;
        
        return total_score;
    }
};
