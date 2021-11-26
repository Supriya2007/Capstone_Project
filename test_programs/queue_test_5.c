

//array impl
//Queue struct
//dequeue with loop
//with capacity limit
//front is never changed in enqueue

struct Queue {
    int front, rear, capacity;
    int* queue;
};


void init(struct Queue* q, int c)
{
    q->front = q->rear = 0;
    q->capacity = c;
    q->queue = (int*) malloc(sizeof(int)*c);
}

//~Queue() { delete[] queue; }

// function to insert an element
// at the rear of the queue
void queueEnqueue(struct Queue *q, int data)
{
    // check queue is full or not
    if (q->capacity == q->rear) {
        printf("\nQueue is full\n");
        return;
    }

    // insert element at the rear
    else {
        q->queue[q->rear] = data;
        q->rear++;
    }
    return;
}

// function to delete an element
// from the front of the queue
void queueDequeue(struct Queue* q)
{
    int i;
    // if queue is empty
    if (q->front == q->rear) {
        printf("\nQueue is  empty\n");
        return;
    }

    // shift all the elements from index 2 till rear
    // to the left by one
    else {
        for (i = 0; i < q->rear - 1; i++) {
            q->queue[i] = q->queue[i + 1];
        }

        // decrement rear
        q->rear--;
    }
    return;
}

// print queue elements
void queueDisplay(struct Queue* q)
{
    int i;
    if (q->front == q->rear) {
        printf("\nQueue is Empty\n");
        return;
    }

    // traverse front to rear and print elements
    for (i = q->front; i < q->rear; i++) {
        printf(" %d <-- ", q->queue[i]);
    }
    return;
}

// print front of queue
void queueFront(struct Queue *q)
{
    if (q->front == q->rear) {
        printf("\nQueue is Empty\n");
        return;
    }
    printf("\nFront Element is: %d", q->queue[q->front]);
    return;
}

 
// Driver code
int main(void)
{
    // Create a queue of capacity 4
    struct Queue q;
    init(&q, 4);
    // print Queue elements
    queueDisplay(&q);
 
    // inserting elements in the queue
    queueEnqueue(&q, 20);
    queueEnqueue(&q, 30);
    queueEnqueue(&q, 40);
    queueEnqueue(&q, 50);
 
    // print Queue elements
    queueDisplay(&q);
 
    // insert element in the queue
    queueEnqueue(&q, 60);
 
    // print Queue elements
    queueDisplay(&q);
 
    queueDequeue(&q);
    queueDequeue(&q);
 
    printf("\n\nafter two node deletion\n\n");
 
    // print Queue elements
    queueDisplay(&q);
 
    // print front of the queue
    queueFront(&q);
 
    return 0;
}
