class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        decrypted_code = []

        for i in range(n):
            if k == 0:
                decrypted_code.append(0)  # If k is 0, replace with 0
            elif k > 0:
                # If k is positive, sum the next k elements (circular)
                total = 0
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
                decrypted_code.append(total)
            else:  # If k is negative, sum the previous |k| elements (circular)
                total = 0
                for j in range(1, -k + 1):
                    total += code[(i - j) % n]
                decrypted_code.append(total)
        
        return decrypted_code