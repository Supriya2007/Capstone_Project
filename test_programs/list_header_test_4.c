//ordered list with header node and a separate list structure having pointer to list head
//list initialized & inserted in a function called from main()
struct node
{
	int key_;
	struct node* link_;
};
//typedef struct node struct node;

struct list
{
	struct node* head_;
};

void init(struct list *ptr_list)
{
	ptr_list->head_ = (struct node *) malloc(sizeof(struct node));
	ptr_list->head_->link_ = NULL;
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
	struct node* prev = ptr_list->head_;
	struct node* pres = prev->link_;
	temp->key_ = key;
	temp->link_ = NULL;
	while(pres && pres->key_ < key)
	{
		prev = pres;
		pres = pres->link_;
	}
	prev->link_ = temp;
	temp->link_ = pres;

}

void disp(struct list *ptr_list)
{
	struct node* temp = ptr_list->head_->link_;
	while(temp)
	{
		printf("%d ", temp->key_);
		temp = temp->link_;
	}
	printf("\n");
}

void test(struct list *ptr_list, int* a, int n){
    int i;
    init(ptr_list);
    for(i = 0; i < n; ++i)
	{
		insert(ptr_list, a[i]);
	}
	disp(ptr_list);
}

int main()
{
	struct list l;
	int a[] = { 20, 10, 40, 30, 25};
	int n = 5;
	test(&l, a, n);	
	insert(&l, 50); //not a violation as l is initialized inside test()
	deinit(&l);
}
