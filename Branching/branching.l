%{
#include<stdio.h>
#include "y.tab.h"
%}
%%
[ \t\n] ;
"if" return IF;
"else" return ELSE;
int|float|char|double|long|switch|break|void {return KEY;}
[0-9]+ return CONST;
[a-z][a-z0-9]* {return ID;}
[ > < = ] return OP;
"(" return OB;
")" return CB;
"{" return OC;

"}" return CC;
"," {return C;}
";" {return SC;}
. {printf("%c\n",yytext[0]);}
%%
