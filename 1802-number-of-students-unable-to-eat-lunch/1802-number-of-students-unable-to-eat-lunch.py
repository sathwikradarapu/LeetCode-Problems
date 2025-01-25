class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dici = {}
        
        # Count the number of each type of student
        for i in students:
            if i not in dici:
                dici[i] = 1
            else:
                dici[i] += 1
        
        rem = len(sandwiches)
        
        # Try to serve sandwiches to students
        for i in sandwiches:
            # If no students are left or no student of the current type is left, break
            if rem == 0 or dici.get(i, 0) == 0:
                break
            dici[i] -= 1
            rem -= 1
        
        return rem
