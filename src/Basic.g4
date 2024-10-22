grammar Basic;

// PARSER RULES
program: (statement NEWLINE+)* statement? EOF;

statement: 
    letStmt | opStmt | printStmt | inputStmt | ifStmt | forStmt | whileStmt | repeatStmt | keyStmt;

letStmt:
    LET_KW ID '=' expression;

opStmt:
    ID '=' expression;

printStmt: 
    PRINT_KW expression;

inputStmt: 
    INPUT_KW STRING_LITERAL ID;

ifStmt:
    IF_KW condition THEN_KW NEWLINE (statement NEWLINE)* (ELSE_KW NEWLINE (statement NEWLINE)*)? END_KW;

forStmt: 
    FOR_KW ID '=' expression TO_KW expression NEWLINE (statement NEWLINE)* NEXT_KW;

whileStmt: 
    WHILE_KW condition NEWLINE (statement NEWLINE)* END_KW;

repeatStmt: 
    REPEAT_KW NEWLINE (statement NEWLINE)* UNTIL_KW condition;

keyStmt:
    CONTINUE_KW | EXIT_KW;

condition: 
    expression comparisonOp expression | expression;

comparisonOp: '<' | '>' | '<=' | '>=' | '=';

expression: 
    expression ('+' | '-' | '*' | '/' | MOD_KW) expression 
    | '(' expression ')'  | functionCall | NUMBER | STRING_LITERAL | ID;

functionCall : 
    VAL_KW '(' expression ')' | LEN_KW '(' expression ')' | ISNAN_KW '(' expression ')';

// LEXER RULES
LET_KW : 'LET' | 'let';
PRINT_KW : 'PRINT' | 'print' ;
INPUT_KW : 'INPUT' | 'input' ;
IF_KW : 'IF' | 'if' ;
ELSE_KW : 'ELSE' | 'else' ;
FOR_KW : 'FOR' | 'for' ;
TO_KW : 'TO' | 'to' ;
NEXT_KW : 'NEXT' | 'next' ;
WHILE_KW : 'WHILE' | 'while' ;
REPEAT_KW : 'REPEAT' | 'repeat' ;
UNTIL_KW : 'UNTIL' | 'until' ;
CONTINUE_KW : 'CONTINUE' | 'continue' ;
EXIT_KW : 'EXIT' | 'exit' ;
END_KW : 'END' | 'end' ;
THEN_KW : 'THEN' | 'then' ;
MOD_KW : 'MOD' | 'mod' ;
VAL_KW : 'VAL' | 'val' ;
LEN_KW : 'LEN' | 'len' ;
ISNAN_KW : 'ISNAN' | 'isnan' ;

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING_LITERAL: '"' (~["\r\n])* '"';
NEWLINE: '\r'? '\n';
COMMENT: 'REM' ~[\r\n]* NEWLINE -> skip;
WS: [ \t]+ -> skip;
