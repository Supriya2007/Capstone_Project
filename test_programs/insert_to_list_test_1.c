struct node
{
	int data;
	struct node *link;
};

void insert_front(int data,struct node **start)
{
	struct node *new_node;
	struct node *dstart;
	new_node = malloc(sizeof(struct node));
	new_node->data=data;
	new_node->link=NULL;
	
	
	dstart= *start;
	if(*start==NULL)
		*start=new_node;
	else
	{
		new_node->link=*start;
		*start=new_node;
	}
}