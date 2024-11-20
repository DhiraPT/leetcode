class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counts = [0] * 3
        for c in s:
            counts[ord(c) - ord('a')] += 1

        max_remove_counts = [count - k for count in counts]
        if any(count < 0 for count in max_remove_counts):
            return -1

        left = right = 0
        curr_counts = [0] * 3
        max_length = 0
        while right < len(s):
            i = ord(s[right]) - ord('a')
            curr_counts[i] += 1

            while curr_counts[i] > max_remove_counts[i]:
                curr_counts[ord(s[left]) - ord('a')] -= 1
                left += 1

            right += 1
            max_length = max(max_length, right - left)

        return len(s) - max_length