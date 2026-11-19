#include <string>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

class Solution {
public:
    int minOperationsToFlip(string expression) {
        // Each entry stores {evaluated_value, min_cost_to_flip}
        vector<pair<int, int>> vals;
        vector<char> ops;
        
        auto apply_op = [&]() {
            char op = ops.back();
            ops.pop_back();
            
            auto [v2, c2] = vals.back(); vals.pop_back();
            auto [v1, c1] = vals.back(); vals.pop_back();
            
            int new_val, new_cost;
            if (op == '&') {
                new_val = v1 & v2;
                if (v1 == 1 && v2 == 1) {
                    new_cost = min(c1, c2);
                } else if (v1 == 0 && v2 == 0) {
                    new_cost = 1 + min(c1, c2);
                } else {
                    // One is 1, one is 0 -> changing '&' to '|' costs 1
                    new_cost = 1;
                }
            } else { // op == '|'
                new_val = v1 | v2;
                if (v1 == 0 && v2 == 0) {
                    new_cost = min(c1, c2);
                } else if (v1 == 1 && v2 == 1) {
                    new_cost = 1 + min(c1, c2);
                } else {
                    // One is 1, one is 0 -> changing '|' to '&' costs 1
                    new_cost = 1;
                }
            }
            vals.push_back({new_val, new_cost});
        };
        
        for (char c : expression) {
            if (c == '(' || c == '&' || c == '|') {
                ops.push_back(c);
            } else {
                if (c == '0' || c == '1') {
                    vals.push_back({c - '0', 1});
                } else if (c == ')') {
                    // Pop the matching '('
                    ops.pop_back();
                }
                // Enforce left-to-right evaluation whenever an operand completes
                if (!ops.empty() && (ops.back() == '&' || ops.back() == '|')) {
                    apply_op();
                }
            }
        }
        
        return vals.back().second;
    }
};
