%{
#include<stdio.h>
#include "y.tab.h"
%}
%token IF ELSE KEY OP OB CB OC CC C SC CONST ID;
%start S;
%%
S: stmt {printf("Valid");};
stmt: IF OB exp CB OC body CC ELSE OC body CC;
exp: ID OP ID | ID OP CONST ;
body: KEY ID OP CONST SC ;
%%
yyerror()
{
printf("Error");
}
main()
{
yyparse();
}
