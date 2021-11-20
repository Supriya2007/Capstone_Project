void creategraph(int **adjacencymatrix,int n)
  {
    int i,j,v;
	adjacencymatrix=(int**)malloc(sizeof(int*)*n);
	for(i=0;i<n;i++)
		adjacencymatrix[i]=(int*)malloc(sizeof(int)*n);
	 
    while(1)
    {
        printf("Enter the source and the destination vertex and path cost");
        scanf("%d %d %d",&i,&j,&v);
        if((i==-1)&&(j==-1))
           break;
        adjacencymatrix[i][j]=1;
     }
	for(i=0;i<n;i++)
		 for(j=0;i<n;i++)
		  printf("%d",adjacencymatrix[i][j]);

  }

 

void bfs(int source, int **adjacencyMatrix, int n,int *visited) {

	int poppedvertex, i;
	int front = -1;
	int rear = -1;
    struct Queue* q = createQueue(n);
	enqueue(q,source);// Insert Source Into Queue
	visited[source] = 1;
	printf("%d",source);
	
	

	while (!isEmpty(q)) { // While Queue Isn't Empty

		
		poppedvertex =dequeue(q) ; // Pop Value From Queue
		for (i = 0; i < n; i++) {

			if (adjacencyMatrix[poppedvertex][i] == 1 && visited[i] == 0) {

				visited[i] = 1;
				printf("---->%d",i);
				enqueue(q,i); // Push City i into queue.
			}
		}
	}

	
}


void dfs (int source, int **adjacencyMatrix, int n,int *visited) {

	int i;
	visited[source] = 1;
	printf("---->%d",source);
	for (i = 0; i < n; i++) {

		if (visited[i] == 0 && adjacencyMatrix[source][i] == 1) {

			dfs(i, adjacencyMatrix, n,visited);
		}
	}
}

int main() {

	int n, i, j;
	int **adjacencyMatrix;
	int *visited;
	int source;
	int choice=0;
	int flag;

	printf("Enter Number Of vertices\n");
	scanf("%d", &n);
	
	creategraph(adjacencyMatrix,n);
	visited=malloc(sizeof(int)*n);

	while (choice < 3){

		printf("Enter Choice\n1. BFS\n2. DFS\n3. Exit\n");	
		scanf("%d", &choice);

		switch(choice) {

			case 1: printf("Enter Source\n");
					scanf("%d", &source);
					for(i = 0; i < n; i++) {

						visited[i] = 0;
					}
					if (source < 0 || source > n) {

						printf("BFS Not Possible With Given Source Value\n");
						break;
					}
					else {

						bfs(source, adjacencyMatrix, n,visited);
					}

	/*				for (i = 0; i < n; i++) {

						if (visited[i] == 1) {

							printf("%d Is Reachable\n", i);
						}

						else {

							printf("%d Is Not Reachable\n", i);
						}
					}
					break;*/

			case 2: flag = 1;
					for (source = 0; source < n; source++) {

						for (i = 0; i < n; i++) {

							visited[i] = 0;
						}

						dfs(source, adjacencyMatrix, n,visited);
						for (i = 0; i < n; i++) {


							if (visited[i] == 0) {

								printf("%d Is Not Reachable\n", i);
								printf("Graph Is Not Connected\n");
								flag = 0;
								return 0;
							}
						}
					}

					if (flag == 1) {

						printf("Graph Is Connected\n");
					}
					break;

		}
	} 

	return 0;

}













