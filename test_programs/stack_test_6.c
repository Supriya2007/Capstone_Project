//Stack struct contains an array member
//++ and -- operators not used in push() and pop()
//No separate function to check isEmpty().

struct Stack{
	int top;
	int array[1000];
};

int isFull(struct Stack *s){
	int status=0;
	if(s->top == 1000-1){
		status=1;
	}
	return status;
}

struct Stack *createStack(unsigned capacity){
	struct Stack *s=(struct Stack *) malloc(sizeof(struct Stack));
	s->top=-1;
	//s->array=(int *)malloc(sizeof(int)*capacity);
	return s;
}

void push(struct Stack *s, int num){
	if(! isFull(s)){
		(s->top)+=1;
		s->array[s->top]=num;
	}
}

//returns 1 on sucess, 0 on failure
int pop(struct Stack *s){
	//int last=-1;
	if(s->top != -1){
		//last=s->array[s->top];
		s->top-=1;
		return 1;
	}
	else{
	    return 0;
	}
}

int peek(struct Stack *s){
	if(s->top == -1){
		return INT_MIN;
	}
	else{
		return (s->array)[s->top];
	}
}

int main(int argc, char *argv[]){
	if(argc!=2){
		printf("Invalid Usage!\n");
		printf("Syntax:\n");
		printf("%s struct Stack_size\n", argv[0]);
		return -1;
	}
	else{
		int size=atoi(argv[1]);
		struct Stack *s=createStack(size);
	    char opt;
	    int num;
		printf("Menu:\n\
s-PUSH\no-POP\ne-peek\nq-Quit\n");
		scanf(" %c", &opt);

		while(opt != 'q'){
			switch(opt){
				case 's': printf("Enter new element:");
						scanf("%d", &num);
						push(s, num);
						break;
						
				case 'o': num = pop(s);
						if(num==0){
							printf("ERROR: struct Stack Underflow\n");
						}
						else{
							printf("Last element popped\n");
						}
						break;
				case 'e': num=peek(s);
						printf("Top = %d\n", num);
						break;
							
				default: printf("Invalid Entry! Try again!\n");
			}
			scanf(" %c", &opt);
		}
		return 0;
	}
}
	
