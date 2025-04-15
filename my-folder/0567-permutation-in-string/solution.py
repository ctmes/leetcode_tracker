class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length, s2_length = len(s1), len(s2)
        s1_counts, s2_counts = [0] * 26, [0] * 26

        if s1_length > s2_length:
            return False

        for i in range(s1_length):
            s1_counts[ord(s1[i]) - 97] += 1
            s2_counts[ord(s2[i]) - 97] += 1

        if s1_counts == s2_counts:
            return True

        for i in range(s1_length, s2_length):
            s2_counts[ord(s2[i]) - 97] += 1
            s2_counts[ord(s2[i - s1_length]) - 97] -= 1

            if s1_counts == s2_counts:
                return True

        return False

        
