%{
#include <stdio.h>
int counter = 0;
void yyerror();
int yylex();
%}

%union {
  char* txtval;
}

%token <txtval> ID
%type <txtval> s
%type <txtval> e

%left '+' '-'
%left '*' '/'

%start s

%%
s: e { printf("t = %s\n", $1); };
e: e '+' e { printf("t%d = %s + %s\n", counter, $1, $3); sprintf($$, "t%d",counter); counter++; };
 | e '-' e { printf("t%d = %s - %s\n", counter, $1, $3); sprintf($$, "t%d",counter); counter++; };
 | e '*' e { printf("t%d = %s * %s\n", counter, $1, $3); sprintf($$, "t%d",counter); counter++; };
 | e '/' e { printf("t%d = %s / %s\n", counter, $1, $3); sprintf($$, "t%d",counter); counter++; };
 | ID { $$ = $1; };
%%

void yyerror() {
  printf("invalid\n");
}

int main() {
  yyparse();
  return 0;
}
