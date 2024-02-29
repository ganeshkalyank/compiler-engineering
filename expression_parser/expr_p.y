%{
    #include <stdio.h>
    void yyerror();
    int yylex();
%}

%token FUNC ID NUM
%start s

%%
s: e { printf("Valid\n"); };
e: e op e | '(' op ')' | FUNC '(' e ')' | ID | NUM;
op: '+' | '-' | '*' | '/' ;
%%

void yyerror() {
    printf("Invalid\n");
}

int main() {
    yyparse();
    return 0;
}
