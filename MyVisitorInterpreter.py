import sys
from antlr4 import *
from enum import Enum
from RustMiniLangParser import RustMiniLangParser
from RustMiniLangVisitor import RustMiniLangVisitor
from Util import *

class MyVisitorInterpreter(RustMiniLangVisitor):

    var_map = {}

    def visitVarDecl(self, ctx:RustMiniLangParser.VarDeclContext):
        if (ctx.getChild(2).getText() in self.var_map):
            sys.exit("VarDecl Error: This variable has already been declared")
        else:
            self.var_map[ctx.getChild(2).getText()] = [ctx.getChild(4).getText(), self.visit(ctx.getChild(6))]
        return 0

    def visitAssignment(self, ctx:RustMiniLangParser.AssignmentContext):
        val = self.visit(ctx.getChild(2))
        if (ctx.getChild(0).getText() in self.var_map):
            if self.var_map[ctx.getChild(0).getText()][0] == get_data_type(val):
                self.var_map[ctx.getChild(0).getText()][1] = val
            else:
                sys.exit("Assignment Error: Different types of assigned data")
        else:
            sys.exit("Assignment Error: this variable does not exist ")
        return 0

    def visitParenthesisExpr(self, ctx:RustMiniLangParser.ParenthesisExprContext):
        return self.visit(ctx.getChild(1))

    def visitPlusMinusExpr(self, ctx:RustMiniLangParser.PlusMinusExprContext):
        op1 = self.visit(ctx.getChild(0))
        op2 = self.visit(ctx.getChild(2))
        if (get_data_type(str(op1)) == get_data_type(str(op2)) == "i32"):
            if (ctx.getChild(1).getText() == '-'): return int(op1 - op2)
            else: return int(op1 + op2)
        else: sys.exit("PlusMinusExpr Error: Invalid types of operands")

    def visitMulDivExpr(self, ctx:RustMiniLangParser.MulDivExprContext):
        op1 = self.visit(ctx.getChild(0))
        op2 = self.visit(ctx.getChild(2))
        if (get_data_type(str(op1)) == get_data_type(str(op2)) == "i32"):
            if (ctx.getChild(1).getText() == '*'): return int(op1 * op2)
            else: return int(op1 / op2)
        else: sys.exit("MulDivExpr Error: Invalid types of operands")

    def visitAndOrExpr(self, ctx:RustMiniLangParser.AndOrExprContext):
        op1 = self.visit(ctx.getChild(0))
        op2 = self.visit(ctx.getChild(2))
        if (get_data_type(str(op1)) == get_data_type(str(op2)) == "bool"):
            if (ctx.getChild(1).getText() == '&'): return (op1 & op2)
            else: return (op1 | op2)
        else: sys.exit("AndOrExpr Error: Invalid types of operands")

    def visitNumExpr(self, ctx:RustMiniLangParser.NumExprContext):
        return int(ctx.getText())

    def visitMinusNumExpr(self, ctx:RustMiniLangParser.MinusNumExprContext):
        return int(ctx.getText())

    def visitBoolExp(self, ctx:RustMiniLangParser.BoolExpContext):
        return get_bool(ctx.getText())

    def visitIdExpr(self, ctx:RustMiniLangParser.IdExprContext):
        if (ctx.getText() in self.var_map):
            if self.var_map[ctx.getText()][0] == "bool":
                return bool(self.var_map[ctx.getText()][1])
            else: return int(self.var_map[ctx.getText()][1])
        sys.exit("visitIdExp Error: this variable does not exist ")

    def visitPrintId(self, ctx:RustMiniLangParser.PrintIdContext):
        print(self.visitIdExpr(ctx.getChild(4)))

    def visitPrintNum(self, ctx:RustMiniLangParser.PrintNumContext):
        print(ctx.getChild(3).getText())

    def visitCompExpr(self, ctx:RustMiniLangParser.CompExprContext):        
        return comp_result(str(self.visit(ctx.getChild(0))), str(self.visit(ctx.getChild(2))), ctx.getChild(1).getText())

    def visitIfstmt(self, ctx:RustMiniLangParser.IfstmtContext):
        if (self.visit(ctx.getChild(2))):
            self.visit(ctx.getChild(4))
        elif (ctx.getChildCount() > 5):
            self.visit(ctx.getChild(5))

    def visitElsestmt(self, ctx:RustMiniLangParser.ElsestmtContext):
        self.visit(ctx.getChild(1))

    def visitWhilestmt(self, ctx:RustMiniLangParser.WhilestmtContext):
        while (self.visit(ctx.getChild(2))):
            self.visit(ctx.getChild(4))

    def visitForstmt(self, ctx:RustMiniLangParser.ForstmtContext):
        self.var_map[ctx.getChild(1).getText()] = ["i32", int(ctx.getChild(3).getText())]
        for i in range(int(ctx.getChild(3).getText()), int(ctx.getChild(5).getText())):
            self.var_map[ctx.getChild(1).getText()][1] = i
            self.visit(ctx.getChild(6))

    def visitStmt(self, ctx:RustMiniLangParser.StmtContext):
        self.visit(ctx.getChild(0))
        return 0

    def visitProgram(self, ctx:RustMiniLangParser.ProgramContext):
        for i in range(0, ctx.getChildCount()):
            self.visit(ctx.getChild(i))
        return 0