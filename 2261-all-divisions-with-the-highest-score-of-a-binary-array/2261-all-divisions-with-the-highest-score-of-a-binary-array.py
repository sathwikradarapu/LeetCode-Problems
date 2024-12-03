class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_ones = sum(nums)  # Total number of 1's in the array
        left_zeros = 0  # Initially, no zeros in numsleft
        right_ones = total_ones  # Initially, all ones are in numsright
        
        max_score = 0
        result = []
        
        for i in range(n + 1):
            # Calculate the current score
            current_score = left_zeros + right_ones
            
            # Check if we found a higher score
            if current_score > max_score:
                max_score = current_score
                result = [i]  # Start a new list of indices
            elif current_score == max_score:
                result.append(i)  # Add index to the existing list
            
            # Update left_zeros and right_ones for next index
            if i < n:
                if nums[i] == 0:
                    left_zeros += 1
                else:
                    right_ones -= 1
        
        return result