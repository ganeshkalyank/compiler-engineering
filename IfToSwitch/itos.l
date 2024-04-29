%{
#include "y.tab.h"
%}

%%
"if" return IF;
"else" return ELSE;
"printf" return PRINTF;
[0-9]+ { yylval.str = strdup(yytext); return NUM; }
[a-zA-Z]+ { yylval.str = strdup(yytext); return ID; }
"==" return EQ;
\".*\" return STRING;
[ \t\n] ;
. return yytext[0];
%%
