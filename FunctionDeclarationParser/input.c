main()
{
float a, *b, c[10], x, y, z[2][2];
a = 9;
b = &a;
c[a]=20;
x = a - b / 3 + c * 2 - 1;
y = a - b / (3 + c) * (2 - 1);
printf("x = %f\n", x);
printf("y = %f\n", y);
z[0][0]=x+y;
}
