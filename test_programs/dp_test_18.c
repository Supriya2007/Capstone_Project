int knapSack(int W, int wt[], int val[], int n)
{
    int dp[W + 1];
   int i, w;
    for (i = 1; i < n + 1; i++) {
        for (w = W; w >= 0; w--) {
 
            if (wt[i - 1] <= w)
                dp[w] = max(dp[w],
                            dp[w - wt[i - 1]] + val[i - 1]);
        }
    }
    return dp[W];
}
int main()
{
    int val[] = { 60, 100, 120 };
    int wt[] = { 10, 20, 30 };
    int W = 50;
    int n = sizeof(val) / sizeof(val[0]);
    printf(knapSack(W, wt, val, n));
    return 0;
}