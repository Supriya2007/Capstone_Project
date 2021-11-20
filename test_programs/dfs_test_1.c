struct node {
  int vertex;
  struct node* next;
};

struct Graph {
  int numVertices;
  int* visited;
  struct node** adjLists;
};

void DFS(struct Graph* graph, int vertex) 
{
  struct node* adjList = graph->adjLists[vertex];
  struct node* temp = adjList;
  int connectedVertex;
  graph->visited[vertex] = 1;
  printf("Visited %d \n", vertex);

  while (temp != NULL) {
    connectedVertex = temp->vertex;
    if (graph->visited[connectedVertex] == 0) {
      DFS(graph, connectedVertex);
    }
    temp = temp->next;
  }
}

struct Graph* createGraph(int vertices) 
{
  struct Graph* graph = malloc(sizeof(struct Graph));
  int i;
  graph->numVertices = vertices;

  graph->adjLists = malloc(vertices * sizeof(struct node*));

  graph->visited = malloc(vertices * sizeof(int));
  for (i = 0; i < vertices; i++) {
    graph->adjLists[i] = NULL;
    graph->visited[i] = 0;
  }
  return graph;
}

void addEdge(struct Graph* graph, int src, int dest) 
{
  struct node* newNode = malloc(sizeof(struct node));
  newNode->vertex = dest;
  newNode->next = NULL;
  newNode->next = graph->adjLists[src];
  graph->adjLists[src] = newNode;
  newNode = malloc(sizeof(struct node));
  newNode->vertex = src;
  newNode->next = NULL;
  newNode->next = graph->adjLists[dest];
  graph->adjLists[dest] = newNode;
}

void printGraph(struct Graph* graph) {
  int v;
  for (v = 0; v < graph->numVertices; v++) {
    struct node* temp = graph->adjLists[v];
    printf("\n Adjacency list of vertex %d\n ", v);
    while (temp) {
      printf("%d -> ", temp->vertex);
      temp = temp->next;
    }
    printf("\n");
  }
}

int main() {
  struct Graph* graph = createGraph(4);
  addEdge(graph, 0, 1);
  addEdge(graph, 0, 2);
  addEdge(graph, 1, 2);
  addEdge(graph, 2, 3);

  printGraph(graph);

  DFS(graph, 2);

  return 0;
}