#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findMinimumTime(vector<vector<int>>& tasks) {
        // Sort tasks by end time ascending
        sort(tasks.begin(), tasks.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        
        bool on[2001] = {false};
        int total_on = 0;
        
        for (const auto& task : tasks) {
            int start = task[0];
            int end = task[1];
            int duration = task[2];
            
            // Count how many seconds in [start, end] are already active
            for (int t = start; t <= end; ++t) {
                if (on[t]) {
                    duration--;
                }
            }
            
            // Greedily allocate remaining required seconds as late as possible
            for (int t = end; duration > 0; --t) {
                if (!on[t]) {
                    on[t] = true;
                    duration--;
                    total_on++;
                }
            }
        }
        
        return total_on;
    }
};
