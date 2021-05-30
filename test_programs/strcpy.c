int main() 
{
  char str1[20];
  char str2[20] = "Hello World";
  char str3[20];
  strcpy(str1, str2);
  strncpy(str3, str1);
  return 0;
}