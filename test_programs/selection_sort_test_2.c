int selection_sort(int a[], int n){
    int i, min, j;
    i=0;
    while(i<n-1){
        min = i;
        j=i+1;
        while(j<n){
            if(a[j] < a[min]){
                min = j;
            }
            j++;
        }
        swap(&a[i], &a[min]);
        i++;
    }
}


void selection_sort(int a[], int n){
    int i, min, j;
    for(i=0; i<n-1; i++){
        min = i;
        j=i+1;
        while(j<n){
            if(a[j] < a[min]){
                min = j;
            }
            j++;
        }
        swap(&a[i], &a[min]);
    }
}



void selection_sort(int a[], int n){
    int i, min, j;
    i=0;
    while(i<n-1){
        min = i;
        for(j=i+1; j<n; j++){
            if(a[j] < a[min]){
                min = j;
            }
        }
        swap(&a[i], &a[min]);
        i++;
    }
}

