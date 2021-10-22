int subsetSum(int a[], int n, int sum)
{
    int** tab  = (int **) malloc(sizeof(int *) * (2000));
    int i;
    
    for(i=0; i<2000; i++){
        tab[i] = (int *) malloc(sizeof(int) * 2000);
    }
    
    if (sum == 0)
        return 1;
         
    if (n <= 0)
        return 0;
    if (tab[n - 1][sum] != -1)
        return tab[n - 1][sum];
    if (a[n - 1] > sum)
        return tab[n - 1][sum] = subsetSum(a, n - 1, sum);
    else
    {
        return tab[n - 1][sum] = subsetSum(a, n - 1, sum) ||
                       subsetSum(a, n - 1, sum - a[n - 1]);
    }
}
 
int main()
{
    int n = 5;
    int a[] = {1, 5, 3, 7, 4};
    int sum = 12;
 
    if (subsetSum(a, n, sum))
    {
        printf("YES");
    }
    else
        printf("NO");
}
