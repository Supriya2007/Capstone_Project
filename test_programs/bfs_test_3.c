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


struct Node{
    int val;
    struct Node* link;
};

struct Queue{
    struct Node* front;
    struct Node* rear;
};

struct Queue* createQueue(void){
    struct Queue* q = malloc(sizeof(struct Queue)); 
    if (q != NULL)
        q->front = NULL; 
        q->rear = NULL;
    return q;        
}

void enQueue(struct Queue *q, int data){
  struct Node *new_node=(struct Node *)malloc(sizeof(struct Node));
  struct Node* cur = q->front;
  new_node->val = data;
  new_node->link = NULL;
  
  if (q->rear == NULL) 
    { 
        q->front = q->rear = new_node; 
    } 
    else{
        q->rear->link = new_node; 
        q->rear = new_node; 
    }
}

int deQueue(struct Queue *q){
    struct Node* first = q->front;
    int val=-1;
    if(!q->front){
        return -1;
    }
    q->front = q->front->link;
    val = first->val;
    free(first);    
    if(q->front == NULL){
            q->rear = NULL;
    }
    return val;
}



int isEmpty(struct Queue *q) 
{ if (q->front)
    return 1;
  return 0;
} 


 

void bfs(int source, int **adjacencyMatrix, int n,int *visited) {

  int poppedvertex, i;
  int front = -1;
  int rear = -1;
    struct Queue* q = createQueue(n);
  enQueue(q,source);// Insert Source Into Queue
  visited[source] = 1;
  printf("%d",source);
  
  

  while (!isEmpty(q)) { // While Queue Isn't Empty

    
    poppedvertex =deQueue(q) ; // Pop Value From Queue
    for (i = 0; i < n; i++) {

      if (adjacencyMatrix[poppedvertex][i] == 1 && visited[i] == 0) {

        visited[i] = 1;
        printf("---->%d",i);
        enQueue(q,i); // Push City i into queue.
      }
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

  /*        for (i = 0; i < n; i++) {

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













