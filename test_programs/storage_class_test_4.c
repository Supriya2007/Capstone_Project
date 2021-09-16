
int main(){
    int *p;
    {
        int a;
        p = &a; //invalid
        {
            int *p;
            p = &a; //valid
                {
                    int a;
                    p = &a; //invalid
                }
            p = &a; //valid
        }
       p = &a; //invalid 
    }
}
