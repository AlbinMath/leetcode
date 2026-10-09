
class Solution {
public:
    bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
        unordered_map<int, int> mp;

        // Map each piece's first element to its index
        for (int i = 0; i < pieces.size(); i++) {
            mp[pieces[i][0]] = i;
        }

        int i = 0;

        while (i < arr.size()) {
            // No piece starts with this element
            if (mp.find(arr[i]) == mp.end()) {
                return false;
            }

            vector<int>& piece = pieces[mp[arr[i]]];

            // Match all elements of the piece
            for (int num : piece) {
                if (i >= arr.size() || arr[i] != num) {
                    return false;
                }
                i++;
            }
        }

        return true;
    }
};

