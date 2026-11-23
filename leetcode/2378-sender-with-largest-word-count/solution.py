from collections import defaultdict

class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        word_counts = defaultdict(int)
        max_words = 0
        best_sender = ""
        
        for sender, msg in zip(senders, messages):
            word_counts[sender] += msg.count(' ') + 1
            if (word_counts[sender], sender) > (max_words, best_sender):
                max_words = word_counts[sender]
                best_sender = sender
                
        return best_sender
