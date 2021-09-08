//#include <stdio.h>
int var = 5;
int *p = &var, *q, *r;
extern int u;
int main(){
    int a, b, c, d;
    int arr[] = {1, 2, 3, 4};
    static e = 10;
    int *l, *m, *n;
    static int* s;
    int** t;
    
    p = &a; //invalid
    q = p+1; //invalid
    r = &c; //invalid
    *p =  a+1;
    
    p = arr+1; //invalid
    q = arr+3-2; //invalid
    r = p+2; //invalid
    
    p = &e;
    l = &a;
    n = malloc(sizeof(int)*4);
    m = n+2;
    *m = 10;
    free(n);
    
    p = &u;
    
    s = &var;
    
    {
        int *v;
        int w;
        t = &v; //invalid
        *t = &w; 
    }
    
    
}
