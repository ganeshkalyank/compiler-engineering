%{
    #include "y.tab.h"
%}

%%
"sin"|"cos" return FUNC;
[0-9]+ return NUM;
[a-zA-Z_][a-zA-Z0-9_]* return ID;
[ \t\n] ;
. return *yytext;
%%
