class Solution {
public:
    int lengthOfLongestSubstring(const std::string& s) {
        std::unordered_map<char, int> lastPos;
        int left = 0;
        int maxLen = 0;

        for (int right = 0; right < static_cast<int>(s.size()); ++right) {
            char ch = s[right];
            auto it = lastPos.find(ch);
            if (it != lastPos.end() && it->second >= left) {
                left = it->second + 1;
            }
            lastPos[ch] = right;
            int curLen = right - left + 1;
            if (curLen > maxLen) {
                maxLen = curLen;
            }
        }
        return maxLen;
    }
};