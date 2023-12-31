## Educational DP Contest

### A - Frog 1

$dp[i] = min(dp[i-1] + |h_{i} - h_{i-1}|,dp[i-1] + |h_{i} - h_{i-2}|  )$

base case: $dp[1] = 0$,  $dp[2] = |h_2 - h_1|$

### B - Frog 2

```
dp[i] = MIN(dp[i-j] + |h_i - h_(i-j)|) 
    for j in [1, K] if (i-j) >= 0
BASE: dp[1] = 0
```

### C - Vacation

```
A, B, C 's ith element denotes the max hapiness after picking 
the ai, bi and ci respectively on day i. 
A[i] = a[i] + MAX(B[i-1], C[i-1])
B[i] = b[i] + MAX(A[i-1], C[i-1])
C[i] = c[i] + MAX(B[i-1], A[i-1])
BASE: A[1] = a[1], B[1] = b[1], C[1] = c[1]
ANS = MAX(A[N], B[N], C[N])
```

### D - Knapsack 1

```
dp[i][j] denotes the max value you can get by taking the
first i objects having weight j. 
DP[i][j] = MAX(DP[i-1][j], V[i] + DP[i-1][j - W[i]]) 
    if (j - W[i]) >= 0
BASE: if i == 0 or j == 0: DP[i][j] = 0
ANS: MAX(DP[N][j]) for j in [1, W]
```

### E - Knapsack 2

1<=N<=100 and 1<=v[i]<=10<sup>3</sup>

```
DP[i][j] denotes the min weight, after considering the first
i objects having value j
i is [1, N] and j is [0, sum(v[i])]
DP[i][j] = MIN(DP[i-1][j], DP[i-1][j - V[i]] + W[i])
    if (j - V[i]) >= 0
BASE: i == 0 or j == 0: DP[i][j] = 0

ANS:
for v in range(sum(v[i]), -1, -1):
    if DP[N][v] <= W:
        return v
```

### F - LCS (longest common subsequence)
