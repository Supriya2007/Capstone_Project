const int MAX_SIZE = 100;

//array impl
//no Queue struct
//dequeue without loop
//no capacity limit
//front may be changed in enqueue

struct graph_node {
    struct graph_node *link;
    int v;
};
typedef struct graph_node graph_node;
struct graph {
    int n;   // # of vertices
    int edgeCount;  // # of edges
    struct graph_node **alist;
};

struct graph *graphCreate(int n)
{
     struct graph *g = malloc(sizeof(struct graph));
    g->n = n;
    g->edgeCount = 0;
    g->alist = calloc(n, sizeof(struct graph_node *));

    return g;
}

void graphAddEdge(struct graph *g, int u, int v)
{
    struct graph_node *e = malloc(sizeof(struct graph_node));
    e->v = v;
    e->link = g->alist[u];
    g->alist[u] = e;
    g->edgeCount++;
}

void readgraph(struct graph *g)
{    int i,j;
	while(1)
    {
        printf("Enter the source and the destination vertex..");
        scanf("%d%d",&i,&j);
        if((i==-1)&&(j==-1))
           break;
        graphAddEdge(g,i,j);
        //insert(j,i);//for undirected graph
     }

}

void graphDestroy(struct graph *g)
{
    int u;
    graph_node *nextnode;
    for(u = 0; u < g->n; u++) {
        while(g->alist[u]) {
            nextnode = g->alist[u]->link;
            free(g->alist[u]);
            g->alist[u] = nextnode;
        }
    }

    free(g->alist);
    free(g);
}

int graphSize(const struct graph *g)
{
    return g->n;
}

int graphEdgeCount(const struct graph *g)
{
    return g->edgeCount;
}



int isEmpty(int* arr, int front, int rear) 
{ return ((front==rear+1) ||(front==-1&&rear==-1 ));
} 

void enqueue(int arr[], int *front, int *rear, int item){
    *rear = (*rear + 1);
    if(*rear==0)
        *front=0;
	arr[*rear] = item; 
}

int dequeue(int arr[], int *front, int *rear) 
{ 
    int item = arr[*front]; 
	if (isEmpty(arr, *front, *rear)) 
		return -9999; //Error code
	
    *front = *front+ 1; //could instead move back all elems by one pos
    //queue->front +=1
	
	return item; 
}

void bfs(struct graph *g,int source,int *visited,int n)
 {
   int v,w;
   struct graph_node *p;
   int q[MAX_SIZE];
   int front = -1; //points to first elem
   int rear = -1; //points to 2nd elem
   visited[source]=1;
   printf("%d ",source);
   //q = createQueue(n);
   //enqueue(q,source);// Insert Source Into Queue
   enqueue(q, &front, &rear, source);
   while(!isEmpty(q, front, rear))
   {
     v=dequeue(q, &front, &rear);
     //printf("v = %d\n", v);
     for(p=(g->alist[v]);p!=NULL;p=(p->link))
     {
       w=p->v;
       if(visited[w]==0)
       {
          visited[w]=1;
          printf(" %d ",w);
         enqueue(q, &front, &rear, w);
       }
     }
   }
 }
void dfs(struct graph *g,int v,int *visited)
  {
    struct graph_node *p;
    int w;
    visited[v]=1;
    printf("%d ",v);
   
    for(p=(g->alist[v]);p!=NULL;p=(p->link))
    {
      w=p->v;
      if(visited[w]==0)//not visited
        dfs(g,w,visited);
     }
   }
//////////////////////////////////////////////////////////////////////
 int main()
 {
   int i,v,k,n,src;  
   struct graph *g; 
   int *visited; 
   printf("Enter the number of vertices..");
   scanf("%d",&n);
   g = graphCreate(n);
   readgraph(g);
   visited=calloc(sizeof(int),n);
   //printf("Enter the source vertex for DFS..\n");
   //scanf("%d",&src);

   //printf("The vertices reachable from %d using DFS are..\n",src);
   //dfs(g,src,visited);
   //for(i=0;i<n;i++)
    //	   visited[i]=0;
   
   printf("\nEnter the source vertex for BFS..\n");
   scanf("%d",&src);
   printf("Traversal order is");
   bfs(g,src,visited,n);
  
  }
