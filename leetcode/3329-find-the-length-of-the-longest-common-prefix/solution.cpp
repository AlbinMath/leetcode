class Solution {
public:
    struct TrieNode {
        TrieNode* child[10];

        TrieNode() {
            for (int i = 0; i < 10; i++)
                child[i] = nullptr;
        }
    };

    int longestCommonPrefix(vector<int>& arr1, vector<int>& arr2) {
        TrieNode* root = new TrieNode();

        // Insert all numbers from arr1
        for (int num : arr1) {
            string s = to_string(num);
            TrieNode* node = root;

            for (char c : s) {
                int digit = c - '0';

                if (!node->child[digit])
                    node->child[digit] = new TrieNode();

                node = node->child[digit];
            }
        }

        int answer = 0;

        // Search prefixes of numbers in arr2
        for (int num : arr2) {
            string s = to_string(num);
            TrieNode* node = root;
            int len = 0;

            for (char c : s) {
                int digit = c - '0';

                if (!node->child[digit])
                    break;

                node = node->child[digit];
                len++;
            }

            answer = max(answer, len);
        }

        return answer;
    }
};
