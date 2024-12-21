# Generated from RustMiniLang.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RustMiniLangParser import RustMiniLangParser
else:
    from RustMiniLangParser import RustMiniLangParser

# This class defines a complete generic visitor for a parse tree produced by RustMiniLangParser.

class RustMiniLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RustMiniLangParser#program.
    def visitProgram(self, ctx:RustMiniLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#stmt.
    def visitStmt(self, ctx:RustMiniLangParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#minusNumExpr.
    def visitMinusNumExpr(self, ctx:RustMiniLangParser.MinusNumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#compExpr.
    def visitCompExpr(self, ctx:RustMiniLangParser.CompExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#plusMinusExpr.
    def visitPlusMinusExpr(self, ctx:RustMiniLangParser.PlusMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#boolExp.
    def visitBoolExp(self, ctx:RustMiniLangParser.BoolExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#andOrExpr.
    def visitAndOrExpr(self, ctx:RustMiniLangParser.AndOrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#parenthesisExpr.
    def visitParenthesisExpr(self, ctx:RustMiniLangParser.ParenthesisExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:RustMiniLangParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#numExpr.
    def visitNumExpr(self, ctx:RustMiniLangParser.NumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#idExpr.
    def visitIdExpr(self, ctx:RustMiniLangParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#varDecl.
    def visitVarDecl(self, ctx:RustMiniLangParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#assignment.
    def visitAssignment(self, ctx:RustMiniLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#compOperator.
    def visitCompOperator(self, ctx:RustMiniLangParser.CompOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#type.
    def visitType(self, ctx:RustMiniLangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#printId.
    def visitPrintId(self, ctx:RustMiniLangParser.PrintIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#printNum.
    def visitPrintNum(self, ctx:RustMiniLangParser.PrintNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#blockstmt.
    def visitBlockstmt(self, ctx:RustMiniLangParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#ifstmt.
    def visitIfstmt(self, ctx:RustMiniLangParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#elsestmt.
    def visitElsestmt(self, ctx:RustMiniLangParser.ElsestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#whilestmt.
    def visitWhilestmt(self, ctx:RustMiniLangParser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#forstmt.
    def visitForstmt(self, ctx:RustMiniLangParser.ForstmtContext):
        return self.visitChildren(ctx)



del RustMiniLangParser