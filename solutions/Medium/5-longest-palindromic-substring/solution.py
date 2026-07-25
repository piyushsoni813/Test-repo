class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        p = [0] * n
        c = r = 0
        for i in range(1, n - 1):
            mir = 2 * c - i
            if i < r:
                p[i] = min(r - i, p[mir])
            while t[i + p[i] + 1] == t[i - p[i] - 1]:
                p[i] += 1
            if i + p[i] > r:
                c, r = i, i + p[i]
        max_len = max(p)
        center = p.index(max_len)
        start = (center - max_len) // 2
        return s[start:start + max_len]