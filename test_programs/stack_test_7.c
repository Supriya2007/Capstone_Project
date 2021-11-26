
//Stack struct contains a pointer member
//++ and -- operators used in push() and pop()
//isEmpty() is checked in a separate function
//top points to index at which next element will be inserted, top=0 initially

struct Stack{
	int top; 
	unsigned int capacity;
	int *array;
};

int isFull(struct Stack *s){
	int status=0;
	if(s->top == s->capacity){
		status=1;
	}
	return status;
}

int isEmpty(struct Stack *s){
	int status=0;
	if(s->top == 0){
		status=1;
	}
	return status;
}

struct Stack *createStack(unsigned capacity){
	struct Stack *s=(struct Stack *) malloc(sizeof(struct Stack));
	s->top=0;
	s->array=(int *)malloc(sizeof(int)*capacity);
	s->capacity=capacity;
	return s;
}

void push(struct Stack *s, int num){
	if(! isFull(s)){
		(s->top)++;
		s->array[s->top]=num;
	}
}

int pop(struct Stack *s){
	int last=-1;
	if(!isEmpty(s)){
		last=s->array[s->top];
		s->top--;
	}
	return last;
}

int peek(struct Stack *s){
	if(isEmpty(s)){
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
						
				case 'o': num=pop(s);
						if(num==-1){
							printf("ERROR: struct Stack Underflow\n");
						}
						else{
							printf("Top = %d\n", num);
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
	
