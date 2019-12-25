#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


int main()
{
	FILE* file = fopen("t.txt","w+");
	if (file == NULL)
	{
		return 0;
	}

	char buf[20]="hello world!!!\n";
	int len = strlen(buf);

	while(1)
	{
		fputs(buf,file);
		fflush(file);
	//	printf("%s",buf);
		sleep(1);
	}

	fclose(file);

	return 0;
}
