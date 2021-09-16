int main(){
    //int **p = (int**) malloc(sizeof(int*)*4);
    int **p;
    int ***q = &p;
    int ***r;
    int a;
    r = &p;
    *r = malloc(sizeof(int)*2); //*p on heap 
    {
        //int a;
        *p = &a; //invalid
    }
    
    {
        int **p;
        int *q;
        int a;
        p = &q;
        *p = &a;
    }
    *p = &a; //invalid; as *p is on heap
    
    {
        int **p = (int**) malloc(sizeof(int*)*3);
        int ***q = &p;
        int a;
        int *b = &a;
        *p = &a; //invalid
        *q = &b; //p changed too
        *p = &a; //valid
    }
    
    {
        int **p;
        int **q;
        int **r;
        int a;
        int b;
        p = (int *)malloc(sizeof(int*)*3);
        q = p;
        r = q;
        *q = &a; //invalid
        *p = &b; //invalid
    }
}
