struct node
{
	int data;
	struct node *link;
};

void insert_rear(int data,struct node **start)
{
	struct node *new_node;
	struct node *dstart=*start;
    new_node = malloc(sizeof(struct node));
	new_node->data=data;
	new_node->link=NULL;
	if(dstart==NULL)
		*start=new_node;
	else
	{
		while(dstart->link!=NULL)
			dstart=dstart->link;
		dstart->link=new_node;
	}
}