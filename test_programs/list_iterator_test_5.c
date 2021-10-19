struct student
{
	char name_[30];
	char srn_[14]; //13 char srn + null char
	int sem_;
	char sec_;
	struct student* link_;
};

struct list
{
	struct student* head_;
};

struct iterator
{
	struct student* ptr_stud_;
};

//search without iterator on student list: v-4; without has_next() function

void init_iterator(struct iterator* ptr_it, struct list* ptr_list)
{
	ptr_it->ptr_stud_ = ptr_list->head_;
}

char* get(struct iterator* ptr_it) // gets the key
{
	return ptr_it->ptr_stud_->srn_; //valid addr returned as struct has been malloced
}

void next(struct iterator* ptr_it)
{
	ptr_it->ptr_stud_ = ptr_it->ptr_stud_->link_;
}

void init(struct list *ptr_list)
{
	ptr_list->head_ = NULL;
}

struct student *make_node_(char* name, char* srn, int sem, char sec)
{
	struct student* temp = (struct student*) malloc(sizeof(struct student));
	strcpy(temp->name_, name);
	strcpy(temp->srn_, srn);
	temp->sem_ = sem;
	temp->sec_ = sec;
	return temp;
}

void insert(struct list *ptr_list, char* name, char* srn, int sem, char sec)
{
	struct student *temp = make_node_(name, srn, sem, sec);
	if(ptr_list->head_ == NULL)
	{
		ptr_list->head_ = temp;
		temp->link_ = NULL;
	}
	else
	{
		struct student* prev = NULL;
		struct student* pres = ptr_list->head_;
		while(pres && strcmp(pres->srn_, srn)<=0)
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

struct iterator search(struct list *ptr_list, char* key){
    struct iterator it;
    init_iterator(&it, ptr_list);
    while(it.ptr_stud_ && strcmp(get(&it), key)){
        next(&it);
    }
    return it; //it points to NULL if val not found in list.
}

void deinit(struct list *ptr_list)
{
	struct student* prev = NULL;
	struct student* pres = ptr_list->head_;
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
	char *names[] = {"anjali", "supriya", "afreen"};	
	char *srns[14] = {"PES2201800032", "PES2201800270", "PES2201800680"};
	int sems[] = {7, 7, 7};
	int secs[] = {'D', 'B', 'B'};
	int n = 3, i;
	struct iterator it;
	
    init(&l);	
	for(i = 0; i < n; ++i)
	{
		insert(&l, names[i], srns[i], sems[i], secs[i]);
	}
	
	it = search(&l, "PES2201800032");

	printf("%s\n", get(&it));
	it = search(&l, "PES2201800270");
	printf("%s\n", get(&it));
	it = search(&l, "PES2201800680");
	printf("%s\n", get(&it));
	it = search(&l, "PES2201800000");
	printf("has_next() is %d\n", it.ptr_stud_!=NULL);
	deinit(&l);
}





