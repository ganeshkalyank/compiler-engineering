%{
    #include "y.tab.h"    
%}

%%
"float" { return DATATYPE; }
[0-9]+ { return CONST; }
[a-zA-Z_][a-zA-Z0-9_]* { return ID; }
("["[0-9]+"]")+|("["[a-zA-Z_][a-zA-Z0-9_]*"]")+ { return LOOKUP; }
"\"".*"\"" { return QUOTED_STRING; }
"//".* ;
[ \t\n] ;
. { return yytext[0]; }
%%
