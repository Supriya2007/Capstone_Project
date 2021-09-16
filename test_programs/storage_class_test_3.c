//#include <stdio.h>

int main(){
    int a, b, c, d;
    int *p;
    {
        int *p = &a; //valid, a has greater scope that p
    }
    {
        int *q;
        {
            int u, v, w;
            int *r = &v; //valid, same scope
            q = &u; //invalid
            {
                int *s = &w; //valid, w has greater scope that s
                int* t;
                int *l = &c; //valid, c has greater scope that l
                t = &b; //valid, b has greater scope that t
                q = &v; //invalid
            }
        }
    }
    
    
    {
        int a;
        {
            p = &a; //invalid
            {
                int *q;
                {
                    q = &a; //valid
                    {
                        int b;
                        q = &b; //invalid
                    }
                }
            }
        }
    }
}
