/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */

class Solution {
    function isPalindrome($head) {
        if ($head === null || $head->next === null) {
            return true;
        }

        // 1. Find the middle of the list
        $slow = $head;
        $fast = $head;

        while ($fast !== null && $fast->next !== null) {
            $slow = $slow->next;
            $fast = $fast->next->next;
        }

        // 2. Reverse the second half
        $secondHalf = $this->reverseList($slow);

        // 3. Compare both halves
        $firstHalf = $head;
        $current = $secondHalf;

        while ($current !== null) {
            if ($firstHalf->val !== $current->val) {
                return false;
            }

            $firstHalf = $firstHalf->next;
            $current = $current->next;
        }

        return true;
    }

    function reverseList($head) {
        $prev = null;
        $current = $head;

        while ($current !== null) {
            $next = $current->next;
            $current->next = $prev;
            $prev = $current;
            $current = $next;
        }

        return $prev;
    }
}
