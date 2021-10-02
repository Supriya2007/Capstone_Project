//list with header node

struct node
{
	int key_;
	struct node* link_;
};
typedef struct node node_t;

struct list
{
	node_t* head_;
};
typedef struct list list_t;

//#define ALLOC(x) (x*)malloc(sizeof(x))

/*
node_t *make_node_(int key)
{
	node_t* temp = (node_t *) malloc(sizeof(node_t));
	temp->key_ = key;
	
	return temp;
}
*/



void init(list_t *ptr_list)
{
	ptr_list->head_ = (node_t *) malloc(sizeof(node_t));
	ptr_list->head_->link_ = NULL;
	
	
}

void deinit(list_t *ptr_list)
{
	node_t* prev = NULL;
	node_t* pres = ptr_list->head_;
	while(pres)
	{
		prev = pres;
		pres = pres->link_;
		free(prev);
	}
}

void insert(list_t *ptr_list, int key)
{
	node_t *temp = make_node_(key);
	node_t* prev = ptr_list->head_;
	node_t* pres = prev->link_;
	while(pres && pres->key_ < key)
	{
		prev = pres;
		pres = pres->link_;
	}
	prev->link_ = temp;
	temp->link_ = pres;

}

void disp(list_t *ptr_list)
{
	node_t* temp = ptr_list->head_->link_;
	while(temp)
	{
		printf("%d ", temp->key_);
		temp = temp->link_;
	}
	printf("\n");
}

int main()
{
	list_t l;
	init(&l);
	int a[] = { 20, 10, 40, 30, 25};
	int n = 5;
	for(int i = 0; i < n; ++i)
	{
		insert(&l, a[i]);
		disp(&l);
	}
	deinit(&l);
}
