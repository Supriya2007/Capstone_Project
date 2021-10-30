int *p;
int size;

void swap(int *xp, int *yp)
{
	int temp = *xp;
	*xp = *yp;
	*yp = temp;
}

// A function to implement bubble sort
void bubbleSort(int arr[], int n)
{
    int i, j;
    int arr_sorted[n];
    //copy arr[] into arr_sorted[]
    for(i=0; i<n; i++){
        arr_sorted[i] = arr[i];
    }
    
    for (i = 0; i < n-1; i++)	
        // Last i elements are already in place
    	for (j = 0; j < n-i-1; j++)
	    	if (arr_sorted[j] > arr_sorted[j+1])
	    		swap(&arr_sorted[j], &arr_sorted[j+1]);
	    		
	p = arr_sorted;
	size = n;
}

/* Function to print an array */
void  printArray()
{
	int i;
	for (i=0; i < size; i++)
		printf("%d ", p[i]); //value undefined
	printf("\n");
}

int main(){
    int arr[100];
    int n, i;
    scanf("%d", &n);
    for(i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }
    bubbleSort(arr, n);
    printArray();
    return 0;
}

