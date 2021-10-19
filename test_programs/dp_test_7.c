int numberOfPaths(int m, int n)
{
    if (m == 1 || n == 1)
        return 1;
    return numberOfPaths(m - 1, n) + numberOfPaths(m, n - 1);
}
 
int main()
{
    printf(numberOfPaths(3, 3));
    return 0;
}