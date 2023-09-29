"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # Base case
        if n <= 1:
            return n

        # Initialize the DP array
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        # Fill up the DP array
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        # Return the number of ways to climb n stairs
        return dp[n]
