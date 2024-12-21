# Generated from RustMiniLang.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RustMiniLangParser import RustMiniLangParser
else:
    from RustMiniLangParser import RustMiniLangParser

# This class defines a complete listener for a parse tree produced by RustMiniLangParser.
class RustMiniLangListener(ParseTreeListener):

    # Enter a parse tree produced by RustMiniLangParser#program.
    def enterProgram(self, ctx:RustMiniLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#program.
    def exitProgram(self, ctx:RustMiniLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#stmt.
    def enterStmt(self, ctx:RustMiniLangParser.StmtContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#stmt.
    def exitStmt(self, ctx:RustMiniLangParser.StmtContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#minusNumExpr.
    def enterMinusNumExpr(self, ctx:RustMiniLangParser.MinusNumExprContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#minusNumExpr.
    def exitMinusNumExpr(self, ctx:RustMiniLangParser.MinusNumExprContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#compExpr.
    def enterCompExpr(self, ctx:RustMiniLangParser.CompExprContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#compExpr.
    def exitCompExpr(self, ctx:RustMiniLangParser.CompExprContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#plusMinusExpr.
    def enterPlusMinusExpr(self, ctx:RustMiniLangParser.PlusMinusExprContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#plusMinusExpr.
    def exitPlusMinusExpr(self, ctx:RustMiniLangParser.PlusMinusExprContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#boolExp.
    def enterBoolExp(self, ctx:RustMiniLangParser.BoolExpContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#boolExp.
    def exitBoolExp(self, ctx:RustMiniLangParser.BoolExpContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#andOrExpr.
    def enterAndOrExpr(self, ctx:RustMiniLangParser.AndOrExprContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#andOrExpr.
    def exitAndOrExpr(self, ctx:RustMiniLangParser.AndOrExprContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#parenthesisExpr.
    def enterParenthesisExpr(self, ctx:RustMiniLangParser.ParenthesisExprContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#parenthesisExpr.
    def exitParenthesisExpr(self, ctx:RustMiniLangParser.ParenthesisExprContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#mulDivExpr.
    def enterMulDivExpr(self, ctx:RustMiniLangParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#mulDivExpr.
    def exitMulDivExpr(self, ctx:RustMiniLangParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#numExpr.
    def enterNumExpr(self, ctx:RustMiniLangParser.NumExprContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#numExpr.
    def exitNumExpr(self, ctx:RustMiniLangParser.NumExprContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#idExpr.
    def enterIdExpr(self, ctx:RustMiniLangParser.IdExprContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#idExpr.
    def exitIdExpr(self, ctx:RustMiniLangParser.IdExprContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#varDecl.
    def enterVarDecl(self, ctx:RustMiniLangParser.VarDeclContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#varDecl.
    def exitVarDecl(self, ctx:RustMiniLangParser.VarDeclContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#assignment.
    def enterAssignment(self, ctx:RustMiniLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#assignment.
    def exitAssignment(self, ctx:RustMiniLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#compOperator.
    def enterCompOperator(self, ctx:RustMiniLangParser.CompOperatorContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#compOperator.
    def exitCompOperator(self, ctx:RustMiniLangParser.CompOperatorContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#type.
    def enterType(self, ctx:RustMiniLangParser.TypeContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#type.
    def exitType(self, ctx:RustMiniLangParser.TypeContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#printId.
    def enterPrintId(self, ctx:RustMiniLangParser.PrintIdContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#printId.
    def exitPrintId(self, ctx:RustMiniLangParser.PrintIdContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#printNum.
    def enterPrintNum(self, ctx:RustMiniLangParser.PrintNumContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#printNum.
    def exitPrintNum(self, ctx:RustMiniLangParser.PrintNumContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#blockstmt.
    def enterBlockstmt(self, ctx:RustMiniLangParser.BlockstmtContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#blockstmt.
    def exitBlockstmt(self, ctx:RustMiniLangParser.BlockstmtContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#ifstmt.
    def enterIfstmt(self, ctx:RustMiniLangParser.IfstmtContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#ifstmt.
    def exitIfstmt(self, ctx:RustMiniLangParser.IfstmtContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#elsestmt.
    def enterElsestmt(self, ctx:RustMiniLangParser.ElsestmtContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#elsestmt.
    def exitElsestmt(self, ctx:RustMiniLangParser.ElsestmtContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#whilestmt.
    def enterWhilestmt(self, ctx:RustMiniLangParser.WhilestmtContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#whilestmt.
    def exitWhilestmt(self, ctx:RustMiniLangParser.WhilestmtContext):
        pass


    # Enter a parse tree produced by RustMiniLangParser#forstmt.
    def enterForstmt(self, ctx:RustMiniLangParser.ForstmtContext):
        pass

    # Exit a parse tree produced by RustMiniLangParser#forstmt.
    def exitForstmt(self, ctx:RustMiniLangParser.ForstmtContext):
        pass


