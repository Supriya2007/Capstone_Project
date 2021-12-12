//#include <stdio.h>
//#include <stdlib.h>
//#include "mergeSort.h"

//#define SIZE 100

void mergeSortedHalfs(int *a, int start, int mid, int end){ 
	int i, j, k, size=end-start+1;
	int *a_copy=(int *) malloc(sizeof(int)*(end+1));
	//allocating (end+1) elements. So, that array values can be stored in same indices in copy as in a. 
	//NOTE: Should have malloc outside array and passed it as argument to function. Same copy could have been used.
	
	if(! a_copy){
		printf("malloc failed!\nAborting!\n");
		return;
	}
	
	//Copying a into array copy.
	for(i=start; i<=end; i++){
		a_copy[i]=a[i];
	}
	
	i=start; j=mid+1; k=start;
	while(i<=mid && j<=end){
		if(a_copy[i]<a_copy[j]){
			a[k]=a_copy[i];
			i++;
		}
		else{
			a[k]=a_copy[j];
			j++;
		}
		k++;
	}
	if(i==mid+1){ //2nd part of array yet to be copied
		while(j<=end){
			a[k]=a_copy[j];
			j++; k++;
		}
	}
	else{ //1st part of array yet to be copied
		while(i<=mid){
			a[k]=a_copy[i];
			i++; k++;
		}
	}
	//printf("before free: a_copy = %p\n", a_copy);
	free(a_copy);
}

void mergeSort(int *a, int start, int end){
	int mid, size=end-start+1;
	if(size<=1){
		return;
	}
	else{
		mid=(start+end)/2;
		mergeSort(a, start, mid);
		mergeSort(a, mid+1, end);
		mergeSortedHalfs(a, start, mid, end);
	}
}

void insertionSort(int *a, int start, int end){
	int i, j, temp, size=end-start+1;
	//long int count=0;//in long int a, b;->does long (or const) apply to b?
	//Record temp;
	for(i=start+1; i<=end; i++){
		temp=a[i];
		j=i-1;
		while(j>=start && a[j]> temp){
			a[j+1]=a[j];
			j=j-1;
			//count++;
		}
		a[j+1]=temp;
	}
	//return count;
}

void selectiveMergeSort(int *a, int start, int end, int parameter){
	int mid, size=end-start+1;
	
	if(size<=parameter){
		insertionSort(a, start, end);
	}
	
	else if(size<=1){ //in case parameter =0.
		return;
	}
	else{
		mid=(start+end)/2;
		selectiveMergeSort(a, start, mid, parameter);
		selectiveMergeSort(a, mid+1, end, parameter);
		mergeSortedHalfs(a, start, mid, end);
	}
}
