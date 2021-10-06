//#include <stdio.h>
//#include <stdlib.h>
//ordered list with header node

struct node
{
	int key_;
	struct node* link_;
};
//typedef struct node struct node;

//struct list
//{
//	struct node* head_;
//};
//typedef struct list struct list;

//#define ALLOC(x) (x*)malloc(sizeof(x))


//struct node *make_node_(int key) //fix issue: not allowing funcs with pointer return type

void init(struct node** ptr_list)
{
	*ptr_list = malloc(sizeof(struct node));	

	//struct node* other;
	//*ptr_list = NULL;
	//other =  malloc(sizeof(struct node));	
	

	//*ptr_list = malloc(sizeof(struct not_exists));	//assumed valid. Only cehcking for malloc(), not for type allocated.
	
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

void insert(struct node** ptr_list, int key)
{
	struct node *temp = (struct node*) malloc(sizeof(struct node));
	struct node* prev = *ptr_list;
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

void disp(struct node *ptr_list)
{
	struct node* temp = ptr_list->link_;
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
