grammar Basic;

// PARSER
program: (statement (NEWLINE+ | EOF)?)*;

statement: 
    letStmt | opStmt | printStmt | inputStmt | ifStmt | forStmt | whileStmt | repeatStmt | keyStmt;

letStmt:
    ('LET' | 'let') ID '=' expression;

opStmt:
    ID '=' expression;

printStmt: 
    ('PRINT' | 'print') expression;

inputStmt: 
    ('INPUT' | 'input') STRING_LITERAL ID;

ifStmt:
    ('IF' | 'if') condition ('THEN' | 'then') NEWLINE (statement NEWLINE)* (('ELSE' | 'else') NEWLINE (statement NEWLINE)*)? ('END' | 'end');

forStmt: 
    ('FOR' | 'for') ID '=' expression ('TO' | 'to') expression NEWLINE (statement NEWLINE)* 'NEXT';

whileStmt: 
    ('WHILE' | 'while') condition NEWLINE (statement NEWLINE)* 'END';

repeatStmt: 
    ('REPEAT' | 'repeat') NEWLINE (statement NEWLINE)* ('UNTIL' | 'until') condition;

keyStmt:
    ('CONTINUE' | 'continue') | ('EXIT' | 'exit') ;

condition: 
    expression comparisonOp expression | expression;

comparisonOp: '<' | '>' | '<=' | '>=' | '=';

expression: 
    expression ('+' | '-' | '*' | '/' | 'MOD') expression 
    | '(' expression ')'  | functionCall | NUMBER | STRING_LITERAL | ID;

functionCall : 
    'VAL' '(' expression ')' | 'LEN' '(' expression ')' | 'ISNAN' '(' expression ')';

// LEXER
ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING_LITERAL: '"' (~["\r\n])* '"';
NEWLINE: '\r'? '\n';
COMMENT: 'REM' ~[\r\n]* NEWLINE -> skip;
WS: [ \t]+ -> skip;
