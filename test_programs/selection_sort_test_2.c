int selection_sort(int a[], int n){
    int i, min, j, temp;
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
        temp = a[i];
        a[i] = a[min];
        a[min] = temp;
        i++;
    }
}


void selection_sort(int a[], int n){
    int i, min, j, temp;
    for(i=0; i<n-1; i++){
        min = i;
        j=i+1;
        while(j<n){
            if(a[j] < a[min]){
                min = j;
            }
            j++;
        }
        temp = a[i];
        a[i] = a[min];
        a[min] = temp;
        i++;
    }
}



void selection_sort(int a[], int n){
    int i, min, j, temp;
    i=0;
    while(i<n-1){
        min = i;
        for(j=i+1; j<n; j++){
            if(a[j] < a[min]){
                min = j;
            }
        }
        temp = a[i];
        a[i] = a[min];
        a[min] = temp;
        i++;
    }
}

