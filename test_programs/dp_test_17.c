
int max(int a, int b)
{
    return (a > b) ? a : b;
}

int knapSackRec(int W, int wt[],
                int val[], int i,
                int** dp)
{
    if (i < 0)
        return 0;
    if (dp[i][W] != -1)
        return dp[i][W];
 
    if (wt[i] > W) {
        dp[i][W] = knapSackRec(W, wt,
                               val, i - 1,
                               dp);
        return dp[i][W];
    }
    else {
    
        dp[i][W] = max(val[i]
                      + knapSackRec(W - wt[i],
                                   wt, val,
                                   i - 1, dp),
                       knapSackRec(W, wt, val,
                                   i - 1, dp));
 
        return dp[i][W];
    }
}
 
int knapSack(int W, int wt[], int val[], int n)
{
    int* dp[n];
    int i,j;
    
    for(i=0; i<n; i++){
        dp[i] = (int *) malloc(sizeof(int)*(W+1));
    }
    
    for (i = 0; i < n; i++)
        for (j = 0; j < W + 1; j++)
            dp[i][j] = -1;
    return knapSackRec(W, wt, val, n - 1, dp);
}
 
int main()
{
    int val[] = { 60, 100, 120 };
    int wt[] = { 10, 20, 30 };
    int W = 50;
    int n = sizeof(val) / sizeof(val[0]);
    printf("%d", knapSack(W, wt, val, n));
    return 0;
}
