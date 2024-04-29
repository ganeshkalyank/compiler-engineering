%{
#include "y.tab.h"
%}

%%
[0-9]+ { yylval.txt = strdup(yytext); return NUM; }
[a-zA-Z_][a-zA-Z0-9_]* { yylval.txt = strdup(yytext); return ID; }
[ \t] ;
\n return 0;
. return yytext[0];
%%
