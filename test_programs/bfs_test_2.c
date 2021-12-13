const int MAX_SIZE = 100;

//list impl
//Queue struct
//graph->adjacency list

struct Node{
    int val;
    struct Node* link;
};

struct Queue{
    struct Node* front;
    struct Node* rear;
};

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




void bfs(struct graph *g,int source,int *visited,int n)
 {
   int v,w;
   struct graph_node *p;
   struct Queue* q = createQueue();
   int front = -1; //points to first elem
   int rear = -1; //points to 2nd elem
   visited[source]=1;
   printf("%d ",source);
   //q = createQueue(n);
   //enqueue(q,source);// Insert Source Into Queue
   enQueue(q, source);
   while(!isEmpty(q))
   {
     v=deQueue(q);
     //printf("v = %d\n", v);
     for(p=(g->alist[v]);p!=NULL;p=(p->link))
     {
       w=p->v;
       if(visited[w]==0)
       {
          visited[w]=1;
          printf(" %d ",w);
         enQueue(q, w);
       }
     }
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
