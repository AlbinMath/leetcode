
class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        // Sort by units per box in descending order
        sort(boxTypes.begin(), boxTypes.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 return a[1] > b[1];
             });

        int totalUnits = 0;

        for (auto& box : boxTypes) {
            int boxesToTake = min(box[0], truckSize);

            totalUnits += boxesToTake * box[1];
            truckSize -= boxesToTake;

            if (truckSize == 0) {
                break;
            }
        }

        return totalUnits;
    }
};

