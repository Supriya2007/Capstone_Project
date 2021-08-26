void search(char* pat, char* txt)
{
    int M = strlen(pat);
    int N = strlen(txt);
    int i, j;
 
    /* A loop to slide pat[] one by one */
    for (i = 0; i <= N - M; i++) {
         
        /* For current index i, check for pattern match */
        for (j = 0; j < M; j++)
            if (txt[i + j] != pat[j])
                break;
 
        if (j == M) 
            printf("Pattern found at index %d \n", i);
    }
}
 
int main()
{
    char txt[] = "AABAACAADAABAAABAA";
    char pat[4] = "AABA"; //no space for null char
    search(pat, txt);
    return 0;
}
