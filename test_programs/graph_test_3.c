struct Queue 
{ 
	int front, rear,capacity; 
	int* array; 
}; 

struct Queue* createQueue(int capacity) 
{ 
	struct Queue* queue = (struct Queue*) malloc(sizeof(struct Queue)); 
	queue->capacity = capacity; 
	queue->front = -1;
        
	queue->rear = -1; 
	queue->array = (int*) malloc(queue->capacity * sizeof(int)); 
	return queue; 
} 

 
int isFull(struct Queue* queue) 
{ return (queue->rear == queue->capacity); } 


int isEmpty(struct Queue* queue) 
{ return ((queue->front==queue->rear+1) ||(queue->front==-1&&queue->rear==-1 ));
} 


void enqueue(struct Queue* queue, int item) 
{ 
	if (isFull(queue)) 
		return; 
	queue->rear = (queue->rear + 1);
        if(queue->rear==0)
        queue->front=0;
	queue->array[queue->rear] = item; 
	
        
} 


int dequeue(struct Queue* queue) 
{ 
    int item = queue->array[queue->front]; 
	if (isEmpty(queue)) 
		return -9999; //Error code
	
        queue->front = (queue->front )+ 1;
        
	
	return item; 
}
// Function to get front of queue 
int peekfront(struct Queue* queue) 
{ 
	if (isEmpty(queue)) 
		return -9999; 
	return queue->array[queue->front]; 
         
} 

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


void bfs(struct graph *g,int source,int *visited,int n)
 {
   int v,w;
   struct graph *p;
   struct Queue* q;
   visited[source]=1;
   printf("%d ",source);
   q = createQueue(n);
   enqueue(q,source);// Insert Source Into Queue
   
   while(!isEmpty(q))
   {
     v=dequeue(q);
     for(p=(g->alist[v]);p!=NULL;p=(p->link))
     {
       w=p->v;
       if(visited[w]==0)
       {
          visited[w]=1;
          printf(" %d ",w);
         enqueue(q,w);
       }
     }
   }
 }
void dfs(struct graph *g,int v,int *visited)
  {
    struct graph *p;
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
   printf("Enter the source vertex for DFS..\n");
   scanf("%d",&src);

   printf("The vertices reachable from %d using DFS are..\n",src);
   dfs(g,src,visited);
   for(i=0;i<n;i++)
	   visited[i]=0;
   
   printf("\nEnter the source vertex for BFS..\n");
   scanf("%d",&src);
   printf("Traversal order is");
   bfs(g,src,visited,n);
  
  }