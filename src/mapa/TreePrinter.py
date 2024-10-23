from antlr4 import ParseTreeListener
from MapaTesoroParser import MapaTesoroParser


class TreePrinter(ParseTreeListener):
    def __init__(self):
        self.indent = 0

    def enterEveryRule(self, ctx):
        rule_name = ctx.__class__.__name__.replace("Context", "")
        print("|  " * self.indent + rule_name)
        self.indent += 1

    def exitEveryRule(self, ctx):
        self.indent -= 1

    def visitTerminal(self, node):
        token_text = node.getText()
        token_type = node.getSymbol().type if hasattr(node, "getSymbol") else None
        if token_type is not None:
            token_name = (
                MapaTesoroParser.symbolicNames[token_type]
                if token_type >= 0 and token_type < len(MapaTesoroParser.symbolicNames)
                else str(token_type)
            )

            if token_name == "<INVALID>":
                print("|  " * self.indent + token_text)
            elif (
                token_name != "<EOF>" and token_text != "<EOF>"
            ):  # Only print EOF if not at root
                print("|  " * self.indent + f"{token_name}: {token_text}")
