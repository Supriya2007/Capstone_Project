//bubble sort

void selection_sort(int a[], int n){
    int i, j, temp;
    //bubble sort
    for(i=0; i<n-1; i++){
        for(j=0; j<n-i-1; j++){
            if(a[j] > a[j+1]){
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
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
