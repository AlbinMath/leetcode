#include <string>
#include <string_view>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxFreq(string s, int maxLetters, int minSize, int maxSize) {
        int n = s.length();
        int freq[26] = {0};
        int distinct = 0;
        int max_occ = 0;
        
        unordered_map<string_view, int> counts;
        counts.reserve(n);
        string_view sv(s);
        
        for (int i = 0; i < n; ++i) {
            if (freq[s[i] - 'a']++ == 0) {
                distinct++;
            }
            
            if (i >= minSize) {
                if (--freq[s[i - minSize] - 'a'] == 0) {
                    distinct--;
                }
            }
            
            if (i >= minSize - 1 && distinct <= maxLetters) {
                string_view sub = sv.substr(i - minSize + 1, minSize);
                max_occ = max(max_occ, ++counts[sub]);
            }
        }
        
        return max_occ;
    }
};
