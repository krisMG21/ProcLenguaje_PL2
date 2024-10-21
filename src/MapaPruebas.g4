grammar MapaPruebas;

mapa: 
    titulo puntos+ coordenadas+; // El mapa tiene un título, seguido de puntos y coordenadas

titulo: 
    STRING; // "Mapa de pruebas"

puntos: 
    STRING 'te da' INT 'puntos'; // Ejemplo: "El Titanic" te da 50 puntos

coordenadas: 
    STRING 'está enterrado en' INT ',' INT; // Ejemplo: "El Titanic" está enterrado en 3,1


STRING: 
    '"' ('El' | 'La') (' '[A-Z][a-z]+)+ '"'; // "El" o "La" seguidos de una o varias palabras con mayúscula al principio
INT: 
    [0-9]+; // Captura números enteros
WS: 
    [ \t\r\n]+ -> skip; // Ignorar espacios en blanco y saltos de línea