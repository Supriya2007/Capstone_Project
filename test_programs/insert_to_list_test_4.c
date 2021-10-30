struct node
{
	int key_;
	struct node* link_;
};
struct list
{
	struct  node *head_;
};


void init(struct list *ptr_list)
{
	ptr_list->head_ = NULL;
}

void deinit(struct list *ptr_list)
{
	struct node * prev = NULL;
	struct node * pres = ptr_list->head_;
	while(pres)
	{
		prev = pres;
		pres = pres->link_;
		free(prev);
	}
}



// empty
// insert in the beginning
// insert in middle
// insert in end
void insert(struct list *ptr_list, int key)
{
	struct node * temp ;
    struct node * prev = NULL;
	struct node * pres = ptr_list->head_;
    temp = malloc(sizeof(struct node) );
	temp->key_ = key;
	// empty list
	if(ptr_list->head_ == NULL)
	{
		ptr_list->head_ = temp;
		temp->link_ = NULL;
	}
	else
	{
		
	//	while(pres && pres->key_ < temp->key_)
		while(pres && pres->key_ < key)
		{
			prev = pres;
			pres = pres->link_;
		}
		if(prev == NULL) // begin
		{
			ptr_list->head_ = temp;
			//temp->link_ = pres;
		}
		else // middle or end
		{
			prev->link_ = temp;
			//temp->link_ = pres;
		}
		temp->link_ = pres;
	}
}

// void delete(struct list *ptr_list, int key); // not implemented
void disp(struct list *ptr_list)
{
	struct node * temp = ptr_list->head_;
	while(temp)
	{
		printf("%d ", temp->key_);
		temp = temp->link_;
	}
	printf("\n");
}
