
int main()
{
	int h; // digit in hundredth place
	int t; // digit in tenth place 
	int u; // unit digit
	int n;
	for(h = 1; h < 10; ++h)
	{
		for(t = 0; t < 10; ++t)
		{
			for(u = 0; u < 10; ++u)
			{
				n = h * 100 + t * 10 + u;
				if(h == u)
				{
					printf("%d\n", n);
				}
			}
		}
	}
}
