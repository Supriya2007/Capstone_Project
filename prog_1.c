int v;
int w;

int f1();
int f2();
int f3(int a, int b);

int f3(int a, int b){
    int a;
    int b;
    int c;
    c = a + b;
}

int f4(int a){
    int d;
    int e;
    e = d+e;
}

int main(){
    int *m1;
    int *matrix1;
    int a;
    int b;
    int c;
    int* matrix;
    int* m;
    m=calloc(100,sizeof(int));
    matrix=calloc(100,4);
    m1=malloc(sizeof(int)*100);
    matrix1=malloc(100*4);
    f1();
    f3(a, b);
}