class Solution:
    def subarrayBitwiseORs(self, arr):
        # Store all the unique OR results
        unique_results = set()
        
        # Store the OR results of the previous subarray
        current_results = set()
        
        for num in arr:
            # Update current results: OR the current number with all previous results
            current_results = {num | x for x in current_results} | {num}
            
            # Add all results from current results to unique results
            unique_results.update(current_results)
        
        # Return the total count of unique OR results
        return len(unique_results)
