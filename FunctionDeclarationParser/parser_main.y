%{
    #include <stdio.h>
    void yyerror();
    int yylex();
%}

%token DATATYPE ID LOOKUP CONST QUOTED_STRING
%start s

%%
s: st { printf("Valid\n"); };
st: ID '(' ')' '{' stmtset '}' ;
stmtset: stmt ';' stmtset | ;
stmt: DATATYPE idlist | ID '=' expr | ID LOOKUP '=' expr | ID '(' arglist ')' ;
arglist: QUOTED_STRING ',' ID ;
idlist: decid ',' idlist | decid ;
decid: ID | '*' ID | ID LOOKUP ;
expr: expr op expr | '(' expr ')' | CONST | ID | '&' ID;
op: '+' | '-' | '*' | '/' ;
%%

void yyerror() {
    printf("Invalid\n");
}

int main() {
    yyparse();
    return 0;
}
