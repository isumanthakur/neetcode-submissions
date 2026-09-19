class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n, m = len(points), len(points[0])
        dp= points[0][:]
        for r in range(1,n):
            left_pass = [0]*m
            right_pass = [0]*m

            left_pass[0] = dp[0]
            for c in range(1, m):
                left_pass[c]=max(left_pass[c-1] -1, dp[c])

            right_pass[m-1] = dp[m-1]
            for c in range(m-2, -1, -1):
                right_pass[c]=max(right_pass[c+1] -1, dp[c])
            
            new_dp=[0]*m
            for c in range(m):
                new_dp[c]= points[r][c]+ max(left_pass[c], right_pass[c])
            dp = new_dp
        return max(dp)
