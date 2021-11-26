
//linked list impl
//only front pointer
//enqueue - loop to get last node
//dequeue - l->head = l->head->next

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

void show_queue (struct Queue *q)
{
    struct Node *tmp;

    if (q != NULL)
    {
        for (tmp = q->front; tmp != NULL; tmp=tmp->link)
            printf ("%d ", tmp->val);
    }
    printf("\n");
}

int main(){
    struct Queue* q = createQueue();
    int val;
    
    printf("enqueue:\n");
    enQueue(q, 10);
    show_queue(q);
    enQueue(q, 5);
    show_queue(q);
    enQueue(q, 2);
    show_queue(q);
    enQueue(q, 15);
    show_queue(q);
    
    printf("dequeue:\n");
    val = deQueue(q);
    show_queue(q);
    val = deQueue(q);
    show_queue(q);
    val = deQueue(q);
    show_queue(q);
    val = deQueue(q);
    show_queue(q);
}


