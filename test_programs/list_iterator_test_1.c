struct node
{
	int key_;
	struct node* link_;
};

struct list
{
	struct node* head_;
};

struct iterator
{
	struct node* ptr_node_;
};

//search with iterator: v-1

void init_iterator(struct iterator* ptr_it, struct list* ptr_list)
{
	ptr_it->ptr_node_ = ptr_list->head_;
}

int get(struct iterator* ptr_it) // gets the key
{
	return ptr_it->ptr_node_->key_;
}


void next(struct iterator* ptr_it)
{
	ptr_it->ptr_node_ = ptr_it->ptr_node_->link_;
}


int has_next(struct iterator* ptr_it)
{
	return ptr_it->ptr_node_ != NULL;
}

void init(struct list *ptr_list)
{
	ptr_list->head_ = NULL;
}

struct node *make_node_(int key)
{
	struct node* temp = (struct node*) malloc(sizeof(struct node));
	temp->key_ = key;
	return temp;
}

void insert(struct list *ptr_list, int key)
{
	struct node *temp = make_node_(key);
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
		if(prev == NULL) 
		{
			ptr_list->head_ = temp;
		}
		else 
		{
			prev->link_ = temp;
		}
		temp->link_ = pres;
	}
}

struct iterator search(struct list *ptr_list, int key){
    struct iterator it;
    init_iterator(&it, ptr_list);
    while(has_next(&it) && get(&it)!=key){
        next(&it);
    }
    return it; //it points to NULL if val not found in list.
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

int main()
{
	struct list l;
	int a[] = { 20, 10, 40, 30, 25};
	int n = 5, i;
	struct iterator it;
	
    init(&l);	
	for(i = 0; i < n; ++i)
	{
		insert(&l, a[i]);
	}
	
	it = search(&l, 20);

	printf("%d\n", get(&it));
	it = search(&l, 30);
	printf("%d\n", get(&it));
	it = search(&l, 25);
	printf("%d\n", get(&it));
	it = search(&l, 11);
	printf("has_next() is %d\n", has_next(&it));
	deinit(&l);
}





