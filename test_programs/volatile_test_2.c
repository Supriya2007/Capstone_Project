int main(){
    volatile int a=0;
    int* a_ptr;
    a_ptr = &a; //invalid
    if(*a_ptr!=0){
        a+=1;
    }
    
    //variable assignment
    {
        int b =5;
        int volatile *b_ptr;
        int volatile **b_ptr_ptr;
        volatile int volatile *a_ptr2;
        volatile int volatile **a_ptr2_ptr;
        b_ptr = &b;
        //int* volatile* b_ptr_ptr;
        b_ptr_ptr = &b_ptr;        
        a_ptr2 = &a;
        a_ptr2_ptr = &a_ptr2;
    }
    
    {
        int* volatile* p;
    }
    
    {
        char ch;
        char* ch_ptr;
        char **volatile ch_ptr_ptr;
        ch_ptr = &ch;
        ch_ptr_ptr = &ch_ptr;
        {
            double ch; //check to see if scope is handled correctly
            double* ch_ptr;
            ch_ptr = &ch;
        }
    }
    
    //variable initialization
    {
        int b =5;
        int volatile *b_ptr = &b;
        //int* volatile* b_ptr_ptr;
        int volatile **b_ptr_ptr = &b_ptr;
    
    
        volatile int volatile *a_ptr2 = &a;
        volatile int volatile **a_ptr2_ptr = &a_ptr2;
    }
    
    {
        int* volatile* p;
    }
    
    {
        char ch;
        char* ch_ptr = &ch;
        char **volatile ch_ptr_ptr = &ch_ptr;
        {
            double ch; //check to see if scope is handled correctly
            double* ch_ptr = &ch;
        }
    }
    
}
