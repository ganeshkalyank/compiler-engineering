%{
#include <stdio.h>
char c = 'a';
void yyerror();
%}

%union {
  char* txt;
}
%token <txt> NUM
%token <txt> ID
%type <txt> e
%left '+' '-'
%left  '*' '/'

%%
st: e { printf("t = %s\n", $1); };
e: e '+' e { printf("t%c = %s + %s\n", c, $1, $3); sprintf($$, "t%c", c); c++; }
 | e '-' e { printf("t%c = %s - %s\n", c, $1, $3); sprintf($$, "t%c", c); c++; }
 | e '*' e { printf("t%c = %s * %s\n", c, $1, $3); sprintf($$, "t%c", c); c++; }
 | e '/' e { printf("t%c = %s / %s\n", c, $1, $3); sprintf($$, "t%c", c); c++; }
 | NUM { $$ = $1; };
 | ID { $$ = $1; };
%%

void yyerror() {
    printf("invalid\n");
}

int main() {
    yyparse();
    return 0;
}
