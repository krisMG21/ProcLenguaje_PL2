grammar BasicMejorado;
// PARSER RULES
program:        (statement NEWLINE+)* statement? EOF;
statement:      letStmt | opStmt | printStmt | inputStmt | ifStmt | forStmt | whileStmt | repeatStmt | keyStmt;
letStmt:        LET ID '=' expression;
opStmt:         ID '=' expression;
printStmt:      PRINT expression;
inputStmt:      INPUT STRING_LITERAL ID;
ifStmt:         IF condition THEN NEWLINE (statement NEWLINE)* (ELSE NEWLINE (statement NEWLINE)*)? END;
forStmt:        FOR ID '=' expression TO expression NEWLINE (statement NEWLINE)* NEXT;
whileStmt:      WHILE condition NEWLINE (statement NEWLINE)* END;
repeatStmt:     REPEAT NEWLINE (statement NEWLINE)* UNTIL condition;
keyStmt:        CONTINUE | EXIT;

condition: 
expression comparisonOp expression | NOT condition | condition logicalOp condition | expression;

logicalOp: AND | OR;

comparisonOp:   '<' | '>' | '<=' | '>=' | '=';
expression:     expression op expression | '(' expression ')'  | functionCall | NUMBER | STRING_LITERAL | ID;
op:             '+' | '-' | '*' | '/' | MOD;
functionCall :  VAL '(' expression ')' | LEN '(' expression ')' | ISNAN '(' expression ')';


// LEXER RULES
NOT : 'NOT' | 'not';
AND: 'AND' | 'and';
OR: 'OR' | 'or';
LET : 'LET' | 'let';
PRINT : 'PRINT' | 'print' ;
INPUT : 'INPUT' | 'input' ;
IF : 'IF' | 'if' ;
ELSE : 'ELSE' | 'else' ;
FOR : 'FOR' | 'for' ;
TO : 'TO' | 'to' ;
NEXT : 'NEXT' | 'next' ;
WHILE : 'WHILE' | 'while' ;
REPEAT : 'REPEAT' | 'repeat' ;
UNTIL : 'UNTIL' | 'until' ;
CONTINUE : 'CONTINUE' | 'continue' ;
EXIT : 'EXIT' | 'exit' ;
END : 'END' | 'end' ;
THEN : 'THEN' | 'then' ;
MOD : 'MOD' | 'mod' ;
VAL : 'VAL' | 'val' ;
LEN : 'LEN' | 'len' ;
ISNAN : 'ISNAN' | 'isnan' ;

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING_LITERAL: '"' (~["\r\n])* '"';
NEWLINE: '\r'? '\n';
COMMENT: 'REM' ~[\r\n]* NEWLINE -> skip;
WS: [ \t]+ -> skip;
