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
	*ptr_list = calloc(1, sizeof(struct node));	
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
	struct node *temp = (struct node*) calloc(1, sizeof(struct node)); //calloc or malloc accepted
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

void demo(struct node** head_ptr, int* a, int n){
    int i;
    for(i = 0; i < n; ++i)
	{
	    init(&head_ptr);
		insert(head_ptr, a[i]); 
		disp(*head_ptr);
	}
}

int main()
{
	//struct list l;
	struct node* head = NULL;
	struct node* head2;
	//struct node* head = (struct node *) malloc(sizeof(struct node));
	int a[] = { 20, 10, 40, 30, 25};
	int n = 5;
	int i;
	//init((struct node**)&head); //type casts in function call cause no issues
	
	
	//init(head);
	//head = (struct node *) malloc(sizeof(struct node));
	//demo((struct node**)&head, (int *) a, n);
	demo(&head, a, n);
	//demo(&head2, a, n);
	deinit(&head);
}
