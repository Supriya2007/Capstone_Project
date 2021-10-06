//#include <stdio.h>
//#include <stdlib.h>
//list structure with header node

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
//typedef struct list struct list;

//#define ALLOC(x) (x*)malloc(sizeof(x))


//struct node *make_node_(int key) //fix issue: not allowing funcs with pointer return type
struct node make_node_(int key)

{
	struct node* temp = (struct node *) malloc(sizeof(struct node));
	temp->key_ = key;
	return temp;
}

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
	struct node *temp = make_node_(key);
	struct node* prev = ptr_list->head_;
	struct node* pres = prev->link_;
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
