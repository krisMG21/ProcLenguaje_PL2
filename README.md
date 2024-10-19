# ProcLenguaje_PL2

Este es el repositorio que contiene tanto info de las herramientas a usar como
el código en sí, en principio en `Python`

## Herramientas

### ANTLR

[ANTLR](https://www.antlr.org/) es un generador de parsers a partir de una gramática.

Fuentes de interés:

* [ANTLR3 Cheat Sheet](https://theantlrguy.atlassian.net/wiki/spaces/ANTLR3/pages/2687036/ANTLR+Cheat+Sheet)
* [Libro ANTLR4](https://github.com/Monarch510/antlr-v4/blob/master/The%20Definitive%20ANTLR%204%20Reference%2C%202nd%20Edition.pdf)
* [Mega tutorial ANTLR](https://tomassetti.me/antlr-mega-tutorial)

## Descargas

Para descargar el ANTLR para `Python` se puede usar el siguiente comando:

```bash
$ pip install antlr4-python3-runtime
```

## Uso del ANTLR

El ANTLR se usa para generar un parser a partir de una gramática.
Esta gramática la vamos a definir en un archivo cualquiera con extensión `.g4`.

Por ejemplo, podemos tener el siguiente archivo `Expr.g4`:

```antlr
grammar Expr;

start_ : expr (';' expr)* EOF;
expr : atom | ('+' | '-') expr | expr '**' expr | expr ('*' | '/') expr | expr
('+' | '-') expr | '(' expr ')' | atom ;
atom : INT ;

INT : [0-9]+ ;
WS : [ \t\n\r]+ -> skip ;
```

Una vez definida la gramática, se puede generar un parser con el siguiente comando:

```bash
antlr4 -Dlanguage=Python3 Expr.g4
```

Esto generará un archivo llamado `ExprLexer.py` y `ExprParser.py` (entre otros),
que usaríamos en nuestro código para generar árboles de sintáxis y parsear expresiones.

El siguiente es un ejemplo de uso en código de las herramientas que hemos generado:

```python
from ExprParser import ExprParser
from ExprLexer import ExprLexer

text = input("> ")

# Generar el parser
lexer = ExprLexer(InputStream(text))
stream = CommonTokenStream(lexer)
parser = ExprParser(stream)

# Generar el árbol de sintáxis
tree = parser.start_()

# Imprimir el árbol de sintáxis
print(tree.toStringTree(recog=parser))
```

Este código generará el siguiente árbol de sintáxis:

```bash
$ python3 ExprMain.py
> 2+2*4
(prog (expr (expr 2) + (expr (expr 2) * (expr 4))) <EOF>)
```

Otra manera es usar las herramientas de `ANTLR` desde la consola:

```bash
$ antlr4-parse Expr.g4 prog -gui
```
