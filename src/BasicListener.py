# Generated from Basic.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BasicParser import BasicParser
else:
    from BasicParser import BasicParser

# This class defines a complete listener for a parse tree produced by BasicParser.
class BasicListener(ParseTreeListener):

    # Enter a parse tree produced by BasicParser#program.
    def enterProgram(self, ctx:BasicParser.ProgramContext):
        pass

    # Exit a parse tree produced by BasicParser#program.
    def exitProgram(self, ctx:BasicParser.ProgramContext):
        pass


    # Enter a parse tree produced by BasicParser#statement.
    def enterStatement(self, ctx:BasicParser.StatementContext):
        pass

    # Exit a parse tree produced by BasicParser#statement.
    def exitStatement(self, ctx:BasicParser.StatementContext):
        pass


    # Enter a parse tree produced by BasicParser#letStmt.
    def enterLetStmt(self, ctx:BasicParser.LetStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#letStmt.
    def exitLetStmt(self, ctx:BasicParser.LetStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#opStmt.
    def enterOpStmt(self, ctx:BasicParser.OpStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#opStmt.
    def exitOpStmt(self, ctx:BasicParser.OpStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#printStmt.
    def enterPrintStmt(self, ctx:BasicParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#printStmt.
    def exitPrintStmt(self, ctx:BasicParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#inputStmt.
    def enterInputStmt(self, ctx:BasicParser.InputStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#inputStmt.
    def exitInputStmt(self, ctx:BasicParser.InputStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#ifStmt.
    def enterIfStmt(self, ctx:BasicParser.IfStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#ifStmt.
    def exitIfStmt(self, ctx:BasicParser.IfStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#forStmt.
    def enterForStmt(self, ctx:BasicParser.ForStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#forStmt.
    def exitForStmt(self, ctx:BasicParser.ForStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#whileStmt.
    def enterWhileStmt(self, ctx:BasicParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#whileStmt.
    def exitWhileStmt(self, ctx:BasicParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#repeatStmt.
    def enterRepeatStmt(self, ctx:BasicParser.RepeatStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#repeatStmt.
    def exitRepeatStmt(self, ctx:BasicParser.RepeatStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#keyStmt.
    def enterKeyStmt(self, ctx:BasicParser.KeyStmtContext):
        pass

    # Exit a parse tree produced by BasicParser#keyStmt.
    def exitKeyStmt(self, ctx:BasicParser.KeyStmtContext):
        pass


    # Enter a parse tree produced by BasicParser#condition.
    def enterCondition(self, ctx:BasicParser.ConditionContext):
        pass

    # Exit a parse tree produced by BasicParser#condition.
    def exitCondition(self, ctx:BasicParser.ConditionContext):
        pass


    # Enter a parse tree produced by BasicParser#comparisonOp.
    def enterComparisonOp(self, ctx:BasicParser.ComparisonOpContext):
        pass

    # Exit a parse tree produced by BasicParser#comparisonOp.
    def exitComparisonOp(self, ctx:BasicParser.ComparisonOpContext):
        pass


    # Enter a parse tree produced by BasicParser#expression.
    def enterExpression(self, ctx:BasicParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BasicParser#expression.
    def exitExpression(self, ctx:BasicParser.ExpressionContext):
        pass


    # Enter a parse tree produced by BasicParser#functionCall.
    def enterFunctionCall(self, ctx:BasicParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by BasicParser#functionCall.
    def exitFunctionCall(self, ctx:BasicParser.FunctionCallContext):
        pass



del BasicParser