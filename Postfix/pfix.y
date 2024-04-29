%{
#include <stdio.h>
#include <stdlib.h>
void yyerror();
%}

%union {
  int num;
  char *id;
}

%token <num> NUM
%token <id> ID
%start s

%%
s: e ;
e: e '+' t { printf("+"); }
 | e '-' t { printf("-"); }
 | t ;
t: t '*' f { printf("*"); }
 | t '/' f { printf("/"); }
 | f ;
f: NUM { printf("%d", $1); }
 | ID { printf("%s", $1); }
%%

void yyerror() {
    printf("error\n");
}

int main() {
  yyparse();
  return 0;
}
