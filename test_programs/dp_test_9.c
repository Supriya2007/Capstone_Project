int numberOfPaths(int m, int n)
{
    int dp[n] = { 1 };
    int i,j;
    dp[0] = 1;
    for (i = 0; i < m; i++) {
        for (j = 1; j < n; j++) {
            dp[j] += dp[j - 1];
        }
    }
 
    return dp[n - 1];
}
 
int main()
{
    printf(numberOfPaths(3, 3));
}