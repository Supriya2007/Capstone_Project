//ordered list without header node and a separate list structure having pointer to list head

struct node
{
	int key_;
	struct node* link_;
};

struct list
{
	struct node* head_;
};

void init(struct list *ptr_list)
{
    ptr_list->head_ = NULL;
	//ptr_list->head_ = (struct node *) malloc(sizeof(struct node));
	//ptr_list->head_->link_ = NULL;	
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
}

void insert(struct list *ptr_list, int key)
{
	struct node *temp = (struct node*) malloc(sizeof(struct node));
	temp->key_ = key;
	temp->link_ = NULL;
	
	// empty list
	if(ptr_list->head_ == NULL)
	{
		ptr_list->head_ = temp;
		temp->link_ = NULL;
	}
	else
	{
		struct node* prev = NULL;
		struct node* pres = ptr_list->head_;
		while(pres && pres->key_ < key)
		{
			prev = pres;
			pres = pres->link_;
		}
		if(prev == NULL) // begin
		{
			ptr_list->head_ = temp;
		}
		else // middle or end
		{
			prev->link_ = temp;
		}
		temp->link_ = pres;
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

int main()
{
	struct list l;
	int a[] = { 20, 10, 40, 30, 25};
	int n = 5;
	int i;
	init(&l);
	for(i = 0; i < n; ++i)
	{
		insert(&l, a[i]);
		disp(&l);
	}
	deinit(&l);
}
