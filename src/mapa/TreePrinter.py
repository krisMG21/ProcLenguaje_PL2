from io import StringIO
from antlr4 import ParseTreeListener, TerminalNode
from MapaTesoroLexer import MapaTesoroLexer
from MapaTesoroParser import MapaTesoroParser


class TreePrinter(ParseTreeListener):
    def __init__(self):
        self.indent = 0
        self.output = StringIO()

    def enterEveryRule(self, ctx):
        rule_name = ctx.__class__.__name__.replace("Context", "")
        self.output.write("|  " * self.indent + rule_name + "\n")
        self.indent += 1

    def exitEveryRule(self, ctx):
        self.indent -= 1

    def visitTerminal(self, node):
        if isinstance(node, TerminalNode):
            token_text = node.getText()
            token_type = node.getSymbol().type
            token_name = (
                MapaTesoroParser.symbolicNames[token_type]
                if token_type < len(MapaTesoroParser.symbolicNames)
                else str(token_type)
            )
            if token_name != "EOF" or self.indent > 0:  # Only print EOF if not at root
                self.output.write("|  " * self.indent + f"{token_name}: {token_text}\n")
