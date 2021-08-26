void *malloc(int size);

int main(){
    int *p;
    int *q;
    int *r;
    int var=10;
    p = malloc(sizeof(int)*10);
    if(p == NULL){
        //printf("malloc failed\n");
        exit(1);
    }
    q = &var;
    r = malloc(sizeof(int)*10);
    
}
