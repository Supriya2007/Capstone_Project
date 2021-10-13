//without tailer: v-1; with tail pointer

struct node
{
	int key_;
	struct node* link_;
};

struct list
{
	struct node* head_;
	struct node* tail_;
};

void init(struct list* ptr_list)
{
    ptr_list->head_ = NULL;
    ptr_list->tail_ = NULL;
}

void deinit(struct list *ptr_list)
{
	struct node* prev = NULL;
	struct node* pres = ptr_list->head_;
	while(pres)
	{
		prev = pres;
		pres = pres->link_;
		free(prev);
	}
	ptr_list->head_ = NULL;
}

//insert at end
void insert(struct list* ptr_list, int key)
{
	struct node *temp = (struct node*) malloc(sizeof(struct node));
	//struct node* prev = *ptr_list;
	//struct node* prev = NULL;
	//struct node* pres = prev->link_;
	//struct node* pres = ptr_list->head_;
	if(!temp){
	    exit(-1);
	}
	
	temp->key_ = key;
	temp->link_ = NULL;
	
	if(ptr_list->head_){
	    ptr_list->tail_->link_ = temp;
	    ptr_list->tail_ = temp;
	}
	else{
	    ptr_list->head_ = temp;
	    ptr_list->tail_ = temp;
	}
	
}

void disp(struct list *ptr_list)
{
	struct node* temp = ptr_list->head_;
	while(temp)
	{
		printf("%d ", temp->key_);
		temp = temp->link_;
	}
	printf("\n");
}

struct node* search(struct list *ptr_list, int key){
    struct node* temp = ptr_list->head_;
    while(temp && temp->key_ != key){
        temp = temp->link_;
    }
    return temp;
}

int main()
{
	struct list l;
	struct node* nd;
	int a[] = { 20, 10, 40, 30, 25};
	int n = 5;
	int i;
	init(&l);
	for(i = 0; i < n; ++i)
	{
		insert(&l, a[i]);
	}
    disp(&l);
	nd = search(&l, 10); //search at beginning
	if(nd){
	    printf("%d\n", nd->key_);
	}
	else{
	    printf("not found\n");
	}
	nd = search(&l, 11); //search at beginning
	if(nd){
	    printf("%d\n", nd->key_);
	}
	else{
	    printf("not found\n");
	}
	deinit(&l);
}
