//insertion sort

void selection_sort(int a[], int n){
    int i, j, key;
    
    for(i=1; i<n; i++){
        key = a[i];
        j = i - 1;
        while(j >=0 && a[j] > key){
            a[j + 1] = a[j];
            j = j - 1;
        }
        a[j+1] = key;
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
