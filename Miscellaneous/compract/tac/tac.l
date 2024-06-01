%{
#include "y.tab.h"
%}

%%
[a-zA-Z0-9_]+ { yylval.txtval = strdup(yytext); return ID; }
[\t ] ;
"\n" return 0;
. return yytext[0];
%%
