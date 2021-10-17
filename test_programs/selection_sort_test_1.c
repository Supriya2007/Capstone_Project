
void swap(int* x, int* y){
    //int temp = *x;
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}
//says selection_sort not followed as the swap steps are in another function
void selection_sort(int a[], int n){
    int i, min, j;
    for(i=0; i<n-1; i++){
        min = i;
        for(j=i+1; j<n; j++){
            if(a[j] < a[min]){
                min = j;
            }
        }
        swap(&a[i], &a[min]);
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
