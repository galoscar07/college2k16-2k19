/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     IDENTIFIER = 258,
     CONSTANT = 259,
     INT = 260,
     BOOL = 261,
     READ = 262,
     WRITE = 263,
     IF = 264,
     ELSE = 265,
     WHILE = 266,
     SEMICOLON = 267,
     ARRAY = 268,
     LEFTBRACKET = 269,
     RIGHTBRAKET = 270,
     LEFTSQUAREBRACKET = 271,
     RIGHTSQUAREBRACKET = 272,
     LEFTPARANTHESIS = 273,
     RIGHTPARANTHESIS = 274,
     PLUS = 275,
     MINUS = 276,
     MULTIPLY = 277,
     DEVIDE = 278,
     GREATER = 279,
     SMALLER = 280,
     GREATEREQUAL = 281,
     SMALLEREQUAL = 282,
     EQUAL = 283,
     DIFFERENT = 284,
     ASSIGNMENT = 285,
     TRUE = 286,
     FALSE = 287,
     MAIN = 288
   };
#endif
/* Tokens.  */
#define IDENTIFIER 258
#define CONSTANT 259
#define INT 260
#define BOOL 261
#define READ 262
#define WRITE 263
#define IF 264
#define ELSE 265
#define WHILE 266
#define SEMICOLON 267
#define ARRAY 268
#define LEFTBRACKET 269
#define RIGHTBRAKET 270
#define LEFTSQUAREBRACKET 271
#define RIGHTSQUAREBRACKET 272
#define LEFTPARANTHESIS 273
#define RIGHTPARANTHESIS 274
#define PLUS 275
#define MINUS 276
#define MULTIPLY 277
#define DEVIDE 278
#define GREATER 279
#define SMALLER 280
#define GREATEREQUAL 281
#define SMALLEREQUAL 282
#define EQUAL 283
#define DIFFERENT 284
#define ASSIGNMENT 285
#define TRUE 286
#define FALSE 287
#define MAIN 288




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

