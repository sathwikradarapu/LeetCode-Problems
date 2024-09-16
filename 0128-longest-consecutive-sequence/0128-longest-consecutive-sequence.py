class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert the list to a set for O(1) lookups
        set_nums = set(nums)
        max_seq_len = 0

        for num in set_nums:
            # Only start counting if `num` is the beginning of a sequence
            if num - 1 not in set_nums:
                current_num = num
                current_streak = 1

                # Count the length of the sequence
                while current_num + 1 in set_nums:
                    current_num += 1
                    current_streak += 1

                max_seq_len = max(max_seq_len, current_streak)

        return max_seq_len
