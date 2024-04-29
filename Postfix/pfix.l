%{
#include "y.tab.h"
%}

%%
[0-9]+ {
    yylval.num = atoi(yytext);
    return NUM;
}
[a-zA-Z_][a-zA-Z0-9_]* {
    yylval.id = strdup(yytext);
    return ID;
}
[ \t] ;
\n return 0;
. return yytext[0];
%%
