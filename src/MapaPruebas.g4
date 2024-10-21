grammar MapaPruebas;

// Parser Rules
mapa            : titulo (puntos | localizacion)* EOF ;
titulo          : STRING NEWLINE ;
puntos          : STRING 'te da' NUMBER 'puntos' NEWLINE ;
localizacion    : STRING 'está enterrado en' coordenada NEWLINE? ;
coordenada      : NUMBER ',' NUMBER; 

// Lexer Rules
STRING          : '"' ([A-Z][a-z]+)+ '"' ;
NUMBER          : [0-9]+ ;
NEWLINE         : '\r'? '\n' | '\r' ;
WS              : [ \t]+ -> skip ;
