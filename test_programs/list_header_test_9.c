//#include <stdio.h>
//#include <stdlib.h>
//insert at end with header node
//not for demo
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
	struct node* prev = *ptr_list;
	struct node* pres = prev->link_;
	temp->key_ = key;
	temp->link_ = NULL;
	while(pres)
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
	struct node* list1 = NULL;
	struct node* list2 = NULL;
	struct node* list3;
	//struct node* list3 = (struct node *) malloc(sizeof(struct node)), *list4 = NULL, *list5, non_list;
	int *v1 = NULL, v2 = 10;
	//struct node* head = (struct node *) malloc(sizeof(struct node));
	int a[] = { 20, 10, 40, 30, 25};
	int n = 5;
	int i;
	//list3->link_ = NULL;
	//init(&head);
	//list1 = (struct node *) malloc(sizeof(struct node));
	//list1->link_ = NULL;
	init(&list1);
	for(i = 0; i < n; ++i)
	{
		insert(&list1, a[i]);
		disp(list1);
	}
	
	init(&list2);
	//list2 = (struct node *) malloc(sizeof(struct node));
	//list2->link_ = NULL;
	for(i = 0; i < n; ++i)
	{
		insert(&list2, a[i]);
		disp(list2);
	}
	
	for(i = 0; i < n; ++i)
	{
		insert(&list1, a[i]); //inserting into list-1 again
		disp(list1);
	}
	
	init(&list3);
	for(i = 0; i < n; ++i)
	{
		insert(&list3, a[i]); //inserting into list-3, no header
		disp(list3);
	}
	//init(&list3);
	deinit(&list1);
	deinit(&list2);
	deinit(&list3);
	
}
