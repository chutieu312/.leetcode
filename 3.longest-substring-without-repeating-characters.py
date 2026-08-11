# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium
# Topic: Sliding Window / Hash Map
#
# Problem:
#   Given a string s, find the length of the longest substring that contains
#   no repeating characters.
#
# Examples:
#   "abcabcbb" → 3  ("abc")
#   "bbbbb"    → 1  ("b")
#   "pwwkew"   → 3  ("wke")
#
# Approach: Sliding window with a dict that maps char → its last-seen index.
#   - right pointer expands the window one char at a time.
#   - If s[right] was seen and its last index is inside the window, jump left
#     to last_index + 1 (shrink window to remove the duplicate).
#   - Track the max window size seen.
#
# Time:  O(n)
# Space: O(min(n, alphabet_size)) — at most 128 entries for ASCII


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}   # char -> most recent index
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                # duplicate is inside current window — shrink from the left
                left = last_seen[ch] + 1
            last_seen[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len


# ---------------------------------------------------------------------------
# Interview talking point
# ---------------------------------------------------------------------------
# "I use a sliding window. The right pointer always moves forward; the dict
#  stores where each character was last seen. When I encounter a repeat that's
#  still inside my window, I move left just past the previous occurrence —
#  that's the smallest shrink that removes the duplicate.
#  One pass, O(n) time, O(1) space for fixed alphabets."
#
# Common mistake to mention: checking 'if ch in last_seen' WITHOUT the
# 'last_seen[ch] >= left' guard can incorrectly shrink the window when the
# duplicate is to the left of the current window.
# ---------------------------------------------------------------------------


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(s.lengthOfLongestSubstring("bbbbb"))     # 1
    print(s.lengthOfLongestSubstring("pwwkew"))    # 3
    print(s.lengthOfLongestSubstring(""))          # 0
    print(s.lengthOfLongestSubstring("au"))        # 2
