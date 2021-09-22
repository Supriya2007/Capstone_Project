//selection sort

void selection_sort(int a[], int n){
    int i, min, j, temp;
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

int main(){
    int a[] = {2, 3, 1, 5, 4};
    int i, n = 5;
    selection_sort(a, n);
    for(i=0; i<n; i++){
        printf("%d ", a[i]);
    }
    printf("\n");
}
