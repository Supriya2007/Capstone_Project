void compute(int opt, int a);

void compute(int opt, int a){
    int ans;
    switch(opt){
        int b = 5;
        case 1: {
            ans = a+b;
            break;
        }
        case 2: {
            ans = a-b;
            break;
        }
        case 3: {
            ans = a*b;
            break;
        }
        case 4: {
            ans = a/b;
            break;
        }
    }
}

int main(){
    compute(1, 2);
    compute(3, 2);
}

