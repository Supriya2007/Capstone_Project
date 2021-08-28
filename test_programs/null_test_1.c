//For both malloc() and calloc()

void *malloc(int size);
void *calloc(int nmemb, int size);

int main(){
    int *ptr1;
    int *ptr2;
    int *ptr3;
    int *ptr4;
    int *ptr5;
    int var=10;
    ptr1 = malloc(sizeof(int)*10);
    if(ptr1 == NULL){
        //printf("malloc failed\n");
        exit(1);
    }
    ptr2 = &var;
    ptr3 = malloc(sizeof(int)*10);
    
    ptr4 = calloc(10, sizeof(int));
    if(ptr4 == NULL){
        //printf("malloc failed\n");
        exit(1);
    }
    ptr5 = calloc(10, sizeof(int));
    
}
