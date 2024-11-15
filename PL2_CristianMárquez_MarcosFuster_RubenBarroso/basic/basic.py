import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from antlr4.ParserRuleContext import ParseTree
from BasicLexer import BasicLexer
from BasicParser import BasicParser
from BasicListener import BasicListener
from ToStrTreeListener import ToStrTreeListener

def as_tree(tree):
    """
    Recorre e imprime el mapa en forma de árbol detallado.
    Args:
        tree (ParseTree): El árbol de análisis sintáctico a recorrer.
    Returns:
        str: La representación del árbol en forma de cadena.
    """
    printer = ToStrTreeListener(BasicParser)
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    return printer.output

def main(argv):
    """
    Función principal que procesa el archivo de entrada y recorre el árbol de análisis sintáctico.
    Args:
        argv (list): Lista de argumentos de la línea de comandos. Se espera que el segundo argumento sea el nombre del archivo de entrada.
    """
    input_stream: FileStream = FileStream(argv[1])
    lexer: BasicLexer = BasicLexer(input_stream)
    stream: CommonTokenStream = CommonTokenStream(lexer)
    parser: BasicParser = BasicParser(stream)
    tree: ParseTree = parser.program()
        
    listener: BasicListener = BasicListener()
    walker: ParseTreeWalker = ParseTreeWalker()
    walker.walk(listener, tree)

    print("as_tree: \n" + as_tree(tree))

if __name__ == "__main__":
    main(sys.argv)