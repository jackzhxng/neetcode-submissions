class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Time taken: 16 mins

        Algo is simple to get but exeution was a bit tricky

        Basically if you can form a valid two digit id you include dp - 2
        If you have valid one digit id (not 0 basically) you include dp - 1
        """
        if not s:
            return 1
        if s[0] == "0":
            return 0
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1
        for dp_i in range(2, len(dp)):
            s_i = dp_i - 1
            single_digit = 0 if s[s_i] == "0" else dp[dp_i - 1]
            double_digit = 0 # Whether to include dp[dp_i - 2] or not
            if s[s_i - 1] == "1": # Check tens digit to see if it's 1 or 2
                double_digit = dp[dp_i - 2]
            elif s[s_i - 1] == "2" and s[s_i] <= "6":
                double_digit = dp[dp_i - 2]
            dp[dp_i] = single_digit + double_digit
        return dp[-1]

