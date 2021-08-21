extern foo;

int main(){
    auto var;
    var = 5;
    
    return 0;
}

sum(int a, int b){
    return a + b;
}

static diff(int a, int b){
    return a - b;
}

display(char *str){
    int i;
    for(i=0; i<strlen(str); i++){
        printf("%c", str[i]);
    }
}


square(int n){
    return n*n;
}
