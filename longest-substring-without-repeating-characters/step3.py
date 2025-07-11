class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pointer_head = max_substring_length = 0
        substring_character_set = set()

        for pointer_tail in range(len(s)):
            while s[pointer_tail] in substring_character_set:
                substring_character_set.remove(s[pointer_head])
                pointer_head += 1
            substring_character_set.add(s[pointer_tail])
            max_substring_length = max(
                max_substring_length,
                len(substring_character_set),
            )

        return max_substring_length
