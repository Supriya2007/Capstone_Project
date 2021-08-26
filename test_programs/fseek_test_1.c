int f3(int a, int b){
    int a;
    int b;
    int c;
    c = a + b;
    if(a<b)
        c=c+1;
    rewind(fp);
    fseek(fp);
}

int f4(){
    int d;
    int e;
    e = d+e;
}

int main(){
    int a;
    int b;
    f1();
    f3(a, b);
    f4(1);
    
    f5(a, b, c);
    a = f6(1, 3, 4, a, b, c);
    
}

