//heap not used

void bubble_sort_descending(int a[], int n){
    int i, j, temp;
    //bubble sort
    for(i=0; i<n-1; i++){
        for(j=0; j<n-i-1; j++){
            if(a[j] < a[j+1]){
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }
}

void printArray(int my_heap[], int n){
    int i;
    for(i=0; i<n; i++){
        printf("%d ", my_heap[i]);
    }
    printf("\n");
}


int main() 
{ 
    
    int arr_len = 7;
    int arr[] = { 10, 2, 3, 5, 4, 8, 15};  
 
    bubble_sort_descending(arr, arr_len);
    printArray(arr, arr_len);
    
    return 0; 
} 
