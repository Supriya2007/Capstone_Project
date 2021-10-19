int count( int *S, int m, int n )         
{                  
 int table[n+1];   
 int i;  
 int j;           
 table[0] = 1;                 
 for(i=0; i<m; i++)
 {
     for(j=S[i]; j<=n; j++)         
        table[j] += table[j-S[i]];
 }                
 return table[n];         
} 