int M,N;
void createAdjMatrix(int **Adj, int **arr)
{
    int i,j;
    for (i = 0; i < N + 1; i++) 
    {
        for (j = 0; j < N + 1; j++) {
            Adj[i][j] = 0;
        }
    }
    for (i = 0; i < M; i++) 
    {
        int x = arr[i][0];
        int y = arr[i][1];
        Adj[x][y] = 1;
        Adj[y][x] = 1;
    }
}
  
void printAdjMatrix(int **Adj)
{
    int i,j;
    for (i = 1; i < N + 1; i++) 
    {
        for (j = 1; j < N + 1; j++) 
        {
            printf("%d ", Adj[i][j]);
        }
        printf("\n");
    }
}
  
int main()
{
    int **Adj;
    int **arr;
    M = sizeof(arr) / sizeof(arr[0]);
    N = 5;
    createAdjMatrix(Adj, arr);
    printAdjMatrix(Adj);
    return 0;
}