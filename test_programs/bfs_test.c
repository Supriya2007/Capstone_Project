

// adjacency list element
struct graph_node {
    struct graph_node *link;
    int v;
};


struct graph {
    int n;   // # of vertices
    int edgeCount;  // # of edges
    struct graph_node **alist;
};




void bfs(struct Graph *g,int source,int *visited,int n)
 {
    struct graph_node* q[n];
    int f;
    int r;
   struct graph_node* p;
   struct graph_node* v;struct graph_node* w;
   visited[ source ]=1;
   printf("%d ",source);
   f=f+1;
   r=r+1;
   q[r]=source;// Insert Source Into Queue
   
   while(f!=r)
   {
     v=q[f];
     f=f+1;
     
     for(p=v;p!=NULL;p=p->link)
     {
       w=p->v;
      
       if(visited[w]==0)
       {
          visited[w]=1;
          printf(" %d ",w);
         q[r]=p;
         r=r+1;
       }
       
     }
     
   }
 }

















