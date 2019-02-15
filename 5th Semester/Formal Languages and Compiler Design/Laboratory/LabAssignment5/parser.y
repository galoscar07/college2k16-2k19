%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1
%}

%token IDENTIFIER
%token CONSTANT
%token INT
%token BOOL
%token READ
%token WRITE
%token IF
%token ELSE
%token WHILE
%token SEMICOLON
%token ARRAY
%token LEFTBRACKET
%token RIGHTBRAKET
%token LEFTSQUAREBRACKET
%token RIGHTSQUAREBRACKET
%token LEFTPARANTHESIS
%token RIGHTPARANTHESIS
%token PLUS
%token MINUS
%token MULTIPLY
%token DEVIDE
%token GREATER
%token SMALLER
%token GREATEREQUAL
%token SMALLEREQUAL
%token EQUAL
%token DIFFERENT
%token ASSIGNMENT
%token TRUE
%token FALSE
%token MAIN

%start program

%%

program : MAIN compoundstmt ;
type : INT | BOOL ;
compoundstmt : LEFTBRACKET stmtlist RIGHTBRAKET ;
stmtlist : statement | statement stmtlist ;
statement : declstmt | assignstmt | iostmt | loopstmt | ifstmt | arraydeclstmt ;
declstmt : type IDENTIFIER | type IDENTIFIER ASSIGNMENT CONSTANT | type IDENTIFIER ASSIGNMENT TRUE | type IDENTIFIER ASSIGNMENT FALSE ;
arraydeclstmt : ARRAY LEFTSQUAREBRACKET IDENTIFIER RIGHTSQUAREBRACKET ;
assignstmt : IDENTIFIER ASSIGNMENT CONSTANT | IDENTIFIER ASSIGNMENT expr | IDENTIFIER ASSIGNMENT TRUE | IDENTIFIER ASSIGNMENT FALSE | IDENTIFIER LEFTSQUAREBRACKET CONSTANT RIGHTSQUAREBRACKET ASSIGNMENT expr ;
expr : IDENTIFIER | CONSTANT | expr op expr ;
op : PLUS | MINUS | MULTIPLY | DEVIDE ;
iostmt : input | output ;
input : READ LEFTPARANTHESIS IDENTIFIER RIGHTPARANTHESIS;
output : WRITE LEFTPARANTHESIS IDENTIFIER RIGHTPARANTHESIS | WRITE LEFTPARANTHESIS CONSTANT RIGHTPARANTHESIS ;
loopstmt : WHILE LEFTPARANTHESIS condition RIGHTPARANTHESIS compoundstmt ;
condition : IDENTIFIER relationop IDENTIFIER | IDENTIFIER relationop CONSTANT | CONSTANT relationop IDENTIFIER | CONSTANT relationop CONSTANT ;
relationop : GREATER | SMALLER | GREATEREQUAL | SMALLEREQUAL | EQUAL | DIFFERENT ;
ifstmt: IF LEFTPARANTHESIS condition RIGHTPARANTHESIS compoundstmt | IF LEFTPARANTHESIS condition RIGHTPARANTHESIS compoundstmt ELSE compoundstmt ;

%%

yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if (argc > 1) 
    yyin = fopen(argv[1], "r");
  if ( (argc > 2) && ( !strcmp(argv[2], "-d") ) ) 
    yydebug = 1;
  if ( !yyparse() ) 
    fprintf(stderr,"\t U GOOOOOD !!!\n");
}

