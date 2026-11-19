#include <string>
using namespace std;

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n1 = s1.length(), n2 = s2.length();
        if (n1 > n2) return false;
        
        int cnt1[26] = {0}, cnt2[26] = {0};
        for (int i = 0; i < n1; ++i) {
            cnt1[s1[i] - 'a']++;
            cnt2[s2[i] - 'a']++;
        }
        
        int matches = 0;
        for (int c = 0; c < 26; ++c) {
            if (cnt1[c] == cnt2[c]) matches++;
        }
        if (matches == 26) return true;
        
        for (int i = n1; i < n2; ++i) {
            int r = s2[i] - 'a';       // Incoming right character
            int l = s2[i - n1] - 'a';  // Outgoing left character
            
            if (cnt2[r] == cnt1[r]) matches--;
            cnt2[r]++;
            if (cnt2[r] == cnt1[r]) matches++;
            
            if (cnt2[l] == cnt1[l]) matches--;
            cnt2[l]--;
            if (cnt2[l] == cnt1[l]) matches++;
            
            if (matches == 26) return true;
        }
        
        return false;
    }
};
