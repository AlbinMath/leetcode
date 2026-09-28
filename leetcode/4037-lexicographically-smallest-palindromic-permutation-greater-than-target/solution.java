class Solution {
    public String lexPalindromicPermutation(String s, String target) {
        int n = s.length();

        // Count characters
        int[] freq = new int[26];
        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }

        // A palindrome can have at most one character with odd frequency
        int odd = -1;
        for (int i = 0; i < 26; i++) {
            if (freq[i] % 2 == 1) {
                if (odd != -1) {
                    return "";
                }
                odd = i;
            }
        }

        char middle = odd == -1 ? 0 : (char) ('a' + odd);

        // Frequencies for the first half
        int[] halfFreq = new int[26];
        int halfLen = 0;

        for (int i = 0; i < 26; i++) {
            halfFreq[i] = freq[i] / 2;
            halfLen += halfFreq[i];
        }

        String bound = target.substring(0, halfLen);

        // Try to make the first half exactly equal to target's first half
        int[] remaining = halfFreq.clone();
        boolean possible = true;

        for (int i = 0; i < halfLen; i++) {
            int x = bound.charAt(i) - 'a';

            if (remaining[x] == 0) {
                possible = false;
                break;
            }

            remaining[x]--;
        }

        // If exact half is possible, check its palindrome
        if (possible) {
            String half = bound;
            String palindrome = makePalindrome(half, middle);

            if (palindrome.compareTo(target) > 0) {
                return palindrome;
            }

            // Need the next permutation of the half
            char[] arr = half.toCharArray();

            int i = arr.length - 2;
            while (i >= 0 && arr[i] >= arr[i + 1]) {
                i--;
            }

            if (i < 0) {
                return "";
            }

            int j = arr.length - 1;
            while (arr[j] <= arr[i]) {
                j--;
            }

            char temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;

            reverse(arr, i + 1, arr.length - 1);

            return makePalindrome(new String(arr), middle);
        }

        /*
         * Exact target prefix is impossible.
         * Find the smallest half that is lexicographically greater
         * than target.substring(0, halfLen).
         */

        remaining = halfFreq.clone();

        // states[i] = remaining frequencies after matching first i chars
        int[][] states = new int[halfLen + 1][26];

        int matched = 0;

        for (int i = 0; i < halfLen; i++) {
            states[i] = remaining.clone();

            int x = bound.charAt(i) - 'a';

            if (remaining[x] == 0) {
                break;
            }

            remaining[x]--;
            matched++;
        }

        states[matched] = remaining.clone();

        // Work backwards to find the rightmost position we can increase
        for (int pos = matched; pos >= 0; pos--) {
            if (pos >= halfLen) {
                continue;
            }

            remaining = states[pos].clone();

            int current = bound.charAt(pos) - 'a';

            // Choose the smallest available character greater than target[pos]
            for (int c = current + 1; c < 26; c++) {
                if (remaining[c] > 0) {
                    remaining[c]--;

                    StringBuilder half = new StringBuilder();
                    half.append(bound, 0, pos);
                    half.append((char) ('a' + c));

                    // Fill remaining positions with smallest characters
                    for (int k = 0; k < 26; k++) {
                        while (remaining[k] > 0) {
                            half.append((char) ('a' + k));
                            remaining[k]--;
                        }
                    }

                    return makePalindrome(half.toString(), middle);
                }
            }
        }

        return "";
    }

    private String makePalindrome(String half, char middle) {
        StringBuilder result = new StringBuilder();

        result.append(half);

        if (middle != 0) {
            result.append(middle);
        }

        result.append(new StringBuilder(half).reverse());

        return result.toString();
    }

    private void reverse(char[] arr, int left, int right) {
        while (left < right) {
            char temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }
}
