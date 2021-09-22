
void swap(int* x, int* y){
    //int temp = *x;
    for( ; ; ){
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
    }
}

/*
void selection_sort(int a[], int n){
    int i, min, j;
    int temp;
    for(i=0; i<n-1; i++){
        min = i;
        for(j=i+1; j<n; j++){
            if(a[j] < a[min]){
                min = j;
            }
        }
        temp = a[i];
        a[i] = a[min];
        a[min] = temp;
    }
}
*/

void selection_sort(int a[], int n){
    int i, min, j, random1, random2, random3, random4, random5, random6, random7, random8, random9;
    int temp;
    for(i=0; i<n-1; i++){
        min = i;
        for(j=i+1; j<n; j++){
            if(a[j] < a[min]){
                min = j;
                random1 = random2; //swap
                random2 = random3;
                random3 = random1;
                random1 = random4;
                
                random2 = random1;
                random3 = random1;
                random4 = random1;
                
                random5 = random1 + 2 - 3;
            }
            
            random6 = random1;
            random7 = 0;
            random8 = 0;
            random7 = random8; //swap, but not in outer loop
            random8 = random9;
            random9 = random7;
            
        }
        random6 = random1;
        random7 = 0;
        random8 = 0;
              
        temp = a[i]; //swap
        a[i] = a[min];
        a[min] = temp;
        
        random7 = random8; //swap; but won't be found as we break once a swap is detected.
        random8 = random9;
        random9 = random7;
    }
}

void selection_sort(int a[], int n){
    for(i=0; i<n-1; i++){
        min = i;
        for(j=i+1; j<n; j++){
            if(a[j] < a[min]){
                min = j;
             }
         }
         {
            int *p, *q;
            int temp;
            p = &a[j];
            q = &a[min];
            temp = *p;
            *p = *q;
            *q = temp;
         }
    }
}

void selection_sort(int a[], int n){
    for(j =0; j<n-1; j++){
        for(i=0; i<n-1; i++){
            {
                
                if(1){
                
                }
                
             }
        }
        {
            int *p1, *q1;
            int temp;
            int a, b, c, d;
            p1 = &a[j];
            q1 = &a[min];
            a = b;
            temp = *p1;
            a = d;
            c = d;
            *p1 = *q1;
            b = c;
            *q1 = temp;
        }
    }
}

int main(){
    int a[] = {2, 3, 1, 5, 4};
    int i, n = 5;
    selection_sort(a, n);
    for(i=0; i<n; i++){
        printf("%d ", a[i]);
    }
    printf("\n");
}
