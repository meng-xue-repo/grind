######### sorted #########
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

######### Array of 26 letters #########
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        freq = [0] * 26

        for i in range(len(s)):
            # Use 'a' to avoid Out of index
            index_s = ord(s[i]) - ord('a')
            index_t = ord(t[i]) - ord('a')

            freq[index_s] += 1
            freq[index_t] -= 1

        return all(i == 0 for i in freq)
