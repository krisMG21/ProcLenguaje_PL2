from antlr4 import ParseTreeListener


class ToStrTreeListener(ParseTreeListener):
    def __init__(self, parser):
        self.indent = 0
        self.output = ""
        self.parser = parser

    def enterEveryRule(self, ctx):
        rule_name = ctx.__class__.__name__.replace("Context", "")
        self.output += "| " * self.indent + rule_name + "\n"
        self.indent += 1

    def exitEveryRule(self, ctx):
        self.indent -= 1

    def visitTerminal(self, node):
        token_text = node.getText()
        token_type = node.getSymbol().type
        token_name = (
            self.parser.symbolicNames[token_type]
            if token_type < len(self.parser.symbolicNames)
            else str(token_type)
        )

        if token_name == "<INVALID>" or token_text == "<EOF>":
            self.output += "| " * self.indent + f"{token_text}\n"
        elif token_text == "\n":
            self.output += "| " * self.indent + f"{token_name}\n"
            self.output += "| " * (self.indent - 1) + "\n"
        else:
            self.output += "| " * self.indent + f"{token_name}: {token_text}\n"
