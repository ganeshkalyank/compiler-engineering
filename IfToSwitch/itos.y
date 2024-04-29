%{
#include <stdio.h>
int yylex();
void yyerror();
%}

%union {
    char *str;
}

%token IF ELSE EQ
%token <str> ID
%token <str> NUM
%token <str> PRINTF
%token <str> STRING

%%
stmt: if elifset else { printf("valid\n"); } ;
if: IF '(' ID EQ NUM ')' '{' { printf("switch (%s) {\ncase %s:\n", $3, $5); } pf '}' ;
elifset: | elifset elif ;
elif: ELSE IF '(' ID EQ NUM ')' '{' { printf("case %s:\n", $6); } pf '}' ;
else: ELSE '{' { printf("default: \n}\n"); } pf '}' ;
pf: PRINTF '(' STRING ',' ID ')' ';' { printf("printf(%s, %s);\n", $3, $5); };
%%

void yyerror() {
    printf("invalid\n");
}

int main() {
    yyparse();
    return 0;
}
