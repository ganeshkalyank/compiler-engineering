%{
    #include <stdio.h>
    void yyerror();
    int yylex();
%}

%token FUNC ID NUM
%start s

%%
s: e { printf("Valid\n"); };
e: FUNC '(' e ')' | e op e | '(' op ')' | ID | NUM;
op: '+' | '-' | '*' | '/' ;
%%

void yyerror() {
    printf("Invalid\n");
}

int main() {
    yyparse();
    return 0;
}
