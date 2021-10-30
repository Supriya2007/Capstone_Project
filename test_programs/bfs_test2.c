void bfs(struct Graph g,int source,int *visited,int n)
 {
   struct Graph_node *p;
   int v,w;
   struct Queue* q = createQueue(n);
   visited[source]=1;
   printf("%d ",source);
   
   enqueue(q,source);// Insert Source Into Queue
   
   while(!isEmpty(q))
   {
     v=dequeue(q);
     for(p=g->alist[v];p!=NULL;p=p->link)
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