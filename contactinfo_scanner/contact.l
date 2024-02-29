%{
    #include <stdio.h>
%}

%%
[a-zA-Z]+". "[a-zA-Z]+ { printf("Name: %s\n", yytext); }
[0-9]+ { printf("Mobile: %s\n", yytext); }
[A-Z0-9]+ { printf("Room No: %s\n", yytext); }
[a-zA-Z]+ { printf("Dept: %s\n", yytext); }
[A-Z ]+ { printf("University: %s\n", yytext); }
[0-9]+"-"[0-9]+ { printf("Landline: %s\n", yytext); }
[a-zA-Z0-9_.+-]+"@"[a-zA-Z0-9-]+"."[a-zA-Z0-9.]+ { printf("Email: %s\n", yytext); }
\n {}
%%

int main() {
    yylex();
    return 0;
}
