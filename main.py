from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Create a set for quick lookup
        word_set = set(dictionary)
        n = len(s)
        
        # dp[i] will hold the minimum extra characters for substring s[0:i]
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # Start with assuming all characters are extra
            dp[i] = dp[i - 1] + 1
            
            # Check if any substring ending at i can be found in the dictionary
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])  # No extra chars if this substring is valid
        
        return dp[n]

# Example usage:
solution = Solution()
print(solution.minExtraChar("leetscode", ["leet", "code", "leetcode"]))  # Output: 1
print(solution.minExtraChar("sayhelloworld", ["hello", "world"]))  # Output: 3
