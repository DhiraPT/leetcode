class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_f = [0] * 26
        s2_f = [0] * 26
        valid = True

        for i in range(len(s1)):
            s1_f[ord(s1[i]) - ord('a')] += 1
            s2_f[ord(s2[i]) - ord('a')] += 1
        matches = sum(1 for i in range(26) if s1_f[i] == s2_f[i])

        if matches == 26:
            return True

        for i in range(len(s1), len(s2)):
            new_index = ord(s2[i]) - ord('a')
            s2_f[new_index] += 1
            if s1_f[new_index] == s2_f[new_index]:
                matches += 1
            elif s1_f[new_index] + 1 == s2_f[new_index]:
                matches -= 1

            old_index = ord(s2[i-len(s1)]) - ord('a')
            s2_f[old_index] -= 1
            if s1_f[old_index] == s2_f[old_index]:
                matches += 1
            elif s1_f[old_index] - 1 == s2_f[old_index]:
                matches -= 1

            if matches == 26:
                return True

        return False