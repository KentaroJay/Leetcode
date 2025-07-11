class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        substring_character_to_index: dict[str, int] = dict()
        longest_substring_length = 0
        pointer_head = 0
        pointer_tail = 1

        substring_character_to_index[s[pointer_head]] = pointer_head

        while pointer_head < len(s) and pointer_tail < len(s):
            if s[pointer_tail] in substring_character_to_index:
                longest_substring_length = max(
                    longest_substring_length,
                    len(substring_character_to_index),
                )
                index_duplication = substring_character_to_index.get(s[pointer_tail])
                pointer_head = index_duplication + 1
                substring_character_to_index = {
                    character: index
                    for character, index in substring_character_to_index.items()
                    if index >= index_duplication
                }
                substring_character_to_index[s[pointer_tail]] = pointer_tail
                pointer_tail += 1
                continue
            substring_character_to_index[s[pointer_tail]] = pointer_tail
            pointer_tail += 1

        longest_substring_length = max(
            longest_substring_length,
            len(substring_character_to_index),
        )

        return longest_substring_length


if __name__ == "__main__":
    solution = Solution()
    assert 5 == solution.lengthOfLongestSubstring("anviaj")
