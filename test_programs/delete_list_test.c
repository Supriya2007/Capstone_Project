struct node
{
	int key_;
	struct node* link_;
};


struct list
{
	struct node* head_;
};


void deinit(struct list *ptr_list)
{
	struct node* prev = NULL;
	struct node* pres = ptr_list->head_;
	while(pres!=NULL)
	{
		prev = pres;
		pres = pres->link_;
		free(prev);
	}
}