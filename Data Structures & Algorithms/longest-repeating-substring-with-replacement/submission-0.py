class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charset = {}
        j = 0
        max_len = 0
        max_freq = 0

        for i in range(len(s)):
            charset[s[i]] = charset.get(s[i], 0) + 1

            max_freq = max(max_freq, charset[s[i]])

            while (i - j + 1) - max_freq > k:
                charset[s[j]] -= 1
                j += 1

            max_len = max(max_len, i - j + 1)

        return max_len