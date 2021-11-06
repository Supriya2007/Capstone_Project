//no separate list structure, passing single pointer

struct StackNode{
	int data;
	struct StackNode *next;
};

struct StackNode *newNode(int num){
	struct StackNode *s=(struct StackNode *) malloc(sizeof(struct StackNode));
	s->data=num;
	s->next=NULL;
	return s;
}

int isEmpty(struct StackNode *s){
	return s==NULL;	//Note !s is not good practice. As of now NULL is defined as = 0. Later, they may change that.
}

struct StackNode* push(struct StackNode *s_p, int num){
	//s_p is a pointer to a pointer to a stack obj.
	struct StackNode *new_node=(struct StackNode *)malloc(sizeof(struct StackNode));
	new_node->data=num;
	new_node->next=s_p;	//Handles empty list case too.
	s_p=new_node;
	return s_p;
}

struct StackNode* pop(struct StackNode *s_p){ //pop does not return any value
	int top=-1;	//Returning -1 on failure
	if(! isEmpty(s_p)){
		struct StackNode *temp=s_p;
		s_p=s_p->next;
		free(temp);
	}
	return s_p;
}

int peek(struct StackNode *s){
	int top=-1;
	if(! isEmpty(s)){
		top=s->data;
	}
	return top;
}

int main(){
	struct StackNode *s=NULL;
	int num;
	char opt='a';
	while(opt != 'q'){
		printf("Menu:\n\
u - push\no - pop\ne - peek\nq - Quit\n");
		scanf(" %c", &opt);
		switch(opt){
			case 'u': printf("Enter new number: "); 
					scanf("%d", &num);
					s = push(s, num);
					break;
			case 'o': s = pop(s);
					
			case 'e': num=peek(s);
					if(num==-1){
						printf("STACK UNDERFLOW\n");
					}
					else{
						printf("%d\n", num);
					}
					break;
			case 'q': break;
			default: printf("Invalid Option\n");							
		}
		
	}
	
	return 0;
}


