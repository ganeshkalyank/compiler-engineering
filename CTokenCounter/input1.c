main()
{
int a,b[100]; // Declaration
char answer;
printf("Would you like to know my name?\n");
printf("Type Y for YES and N for NO: ");
answer = getchar(); /* .... Reading a character...*/
if(answer == 'Y' || answer == 'y')
printf("\n\nMy name is BUSY BEE\n");
else
printf("\n\nYou are good for nothing\n");
return 0;
}
