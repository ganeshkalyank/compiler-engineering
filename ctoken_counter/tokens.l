%{
    #include <stdio.h>
    
    int tokens = 0;
%}

%%
"int"|"char" { printf("DATA_TYPE: %s\n", yytext); tokens++; }
"if"|"else"|"return" { printf("KEYWORD: %s\n", yytext); tokens++; }
"("|")"|"{"|"}"|"["|"]"|"<"|">" { printf("BRACES: %s\n", yytext); tokens++; }
"\"".*"\""|"'"[a-zA-Z]*"'" { printf("QUOTED_TEXT: %s\n", yytext); tokens++; }
"\/\/".*|"\/*".*"*\/" { printf("COMMENT: %s\n", yytext); }
[a-z]*"."[a-z]* { printf("FILE: %s\n", yytext); }
[a-zA-Z_][a-zA-Z_0-9]* { printf("IDENTIFIER: %s\n", yytext); tokens++; }
[0-9]+ { printf("CONSTANT: %s\n", yytext); tokens++; }
[,;] { printf("SEPARATOR: %s\n", yytext); tokens++; }
"=="|"||"|"=" { printf("OPERATOR: %s\n", yytext); tokens++; }
"#" { printf("SPECIAL_CHAR: %s\n", yytext); }
[ \n\t] {}
%%

int main() {
    yylex();
    printf("\nTotal tokens: %d\n", tokens);
}
