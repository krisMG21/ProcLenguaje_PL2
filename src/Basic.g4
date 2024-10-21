grammar Basic;

program: (statement NEWLINE)* EOF;

statement: 
    letStmt | printStmt | inputStmt | ifStmt | forStmt | whileStmt | repeatStmt;

letStmt:
    'LET' ID '=' expression;

printStmt: 
    'PRINT' (expression (',' expression)* )?;

inputStmt: 
    'INPUT' STRING_LITERAL ID;

ifStmt: 
    'IF' condition 'THEN' NEWLINE (statement NEWLINE)* ('ELSE' NEWLINE (statement NEWLINE)*)? 'END';

forStmt: 
    'FOR' ID '=' expression 'TO' expression NEWLINE (statement NEWLINE)* 'NEXT';

whileStmt: 
    'WHILE' condition NEWLINE (statement NEWLINE)* 'END';

repeatStmt: 
    'REPEAT' NEWLINE (statement NEWLINE)* 'UNTIL' condition;

condition: 
    expression comparisonOp expression | expression;

comparisonOp: '<' | '>' | '<=' | '>=' | '=';

expression: 
    expression ('+' | '-' | '*' | '/' | 'MOD') expression 
    | '(' expression ')'  | functionCall | NUMBER | STRING_LITERAL | ID;

functionCall : 
    'VAL' '(' expression ')' | 'LEN' '(' expression ')' | 'ISNAN' '(' expression ')';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING_LITERAL: '"' (~["\r\n])* '"';
NEWLINE: '\r'? '\n';
WS: [ \t]+ -> skip;
