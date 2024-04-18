%{
    #include <stdio.h>
    #include <stdlib.h>
%}

%union {char dval;}
%token <dval> NUM
%type <dval> E
%left '+' '-'
%left  '*' '/'

%%
S : E { printf("\nt=%c\n",$1); }
  ;
E : E'+'E { $$ = GenCode($$, $1,'+',$3); }
  | E'-'E { $$ = GenCode($$, $1,'-',$3); }
  | E'*'E { $$ = GenCode($$, $1,'*',$3); }
  | E'/'E { $$ = GenCode($$, $1,'/',$3); }
  | '('E')' { $$ = $2; }
  | NUM { $$ = $1; }
  ;
%%

int yywrap() {
    return 0;
}

void yyerror(char* str) {
    printf("\n%s",str);
}

int main() {
    yyparse();
    return 0;
}
