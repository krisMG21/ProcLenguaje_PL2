grammar MapaTesoro;

// Parser Rules
mapa            : titulo tamaño? puntos* localizacion* EOF ;
titulo          : STRING NEWLINE ;
tamaño          : STRING 'tiene' NUMBER 'filas' NUMBER 'columnas' NEWLINE ;
puntos          : STRING 'te da' NUMBER 'puntos' NEWLINE ;
localizacion    : STRING 'está enterrado en' coordenada NEWLINE ;
coordenada      : NUMBER ',' NUMBER;

// Lexer Rules
STRING          : '"' (~["\r\n])* '"' ;
NUMBER          : [0-9]+ ;
NEWLINE         : [\r\n]+ ;
WS              : [ \t]+ -> skip ;
