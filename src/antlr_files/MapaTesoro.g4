grammar MapaTesoro;

// Parser Rules
nivel           : mapa jugador | jugador mapa;
mapa            : 'Mapa:' NEWLINE titulo tamaño? puntos* daño* localizacion*;
jugador         : 'Jugador:' NEWLINE vida NEWLINE;

titulo          : STRING NEWLINE ;
tamaño          : 'El mapa tiene' NUMBER 'filas y' NUMBER 'columnas' NEWLINE ;
puntos          : STRING 'te da' NUMBER 'puntos' NEWLINE ;
daño            : STRING 'hace ' NUMBER 'puntos de daño' NEWLINE ;
localizacion    : STRING 'está enterrado en' coordenada NEWLINE ;
coordenada      : NUMBER ',' NUMBER;

vida            : 'Tiene ' INT ' puntos de vida' NEWLINE; 

// Lexer RulesMapa de pruebas
STRING          : '"' (~["\r\n])* '"' ;
NUMBER          : [0-9]+ ;
NEWLINE         : [\r\n]+ ;
WS              : [ \t]+ -> skip ;
