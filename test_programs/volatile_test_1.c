//#include <stdio.h>
  
void func(void) {
  static volatile int **ipp;
  static int *ip;
  static volatile int i = 0;
 
  printf("i = %d.\n", i);
 
  ipp = &ip; /* May produce a warning diagnostic */
  ipp = (int**) &ip; /* Constraint violation; may produce a warning diagnostic */
  *ipp = &i; /* Valid */
  if (*ip != 0) { /* Can be optimized away by the compiler as i is set to 0 a few lines above. Say, in this program, i might get modified by an external process that changes its value from 0. To prevent the optimization, i must be declared as volatile.  */
    /* ... */
  }
}

int main(){
    volatile int a;
    func();
}
