//insert at end without header node

struct node
{
	int key_;
	struct node* link_;
};


void init(struct node** ptr_list)
{
	*ptr_list = NULL;	
}

void deinit(struct node **ptr_list)
{
	struct node* prev = NULL;
	struct node* pres = *ptr_list;
	while(pres)
	{
		prev = pres;
		pres = pres->link_;
		free(prev);
	}
	*ptr_list = NULL;
}

//insert at end
void insert(struct node** ptr_list, int key)
{
	struct node *temp = (struct node*) malloc(sizeof(struct node));
	//struct node* prev = *ptr_list;
	struct node* prev = NULL;
	//struct node* pres = prev->link_;
	struct node* pres = *ptr_list;
	temp->key_ = key;
	temp->link_ = NULL;
	
	if(!pres){
	    *ptr_list = temp;
	}
	else{
	    while(pres)
	    {
		    prev = pres;
		    pres = pres->link_;
	    }
	    prev->link_ = temp;
	    temp->link_ = pres;
	}
}

void disp(struct node *ptr_list)
{
	struct node* temp = ptr_list;
	while(temp)
	{
		printf("%d ", temp->key_);
		temp = temp->link_;
	}
	printf("\n");
}

int main()
{
	//struct list l;
	struct node* head = NULL;
	int a[] = { 20, 10, 40, 30, 25};
	int n = 5;
	int i;
	init(&head);
	for(i = 0; i < n; ++i)
	{
		insert(&head, a[i]);
		disp(head);
	}
	deinit(&head);
}
