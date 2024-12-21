import sys
from antlr4 import *
from enum import Enum
from RustMiniLangParser import RustMiniLangParser
from RustMiniLangVisitor import RustMiniLangVisitor
from Util import *

class MyVisitorCompiler(RustMiniLangVisitor):
    
    data = ".data\n\n"
    text = "\n.text\n\n"
    cur_string = ""
    if_cnt, for_cnt, while_cnt = 0, 0, 0
    reg_map = [1] + [0] * 31

    def get_reg(self):
        for i in range(32):
            if self.reg_map[i] == 0:
                self.reg_map[i] = 1
                return i

    def free_reg(self, indices):
        for i in indices:
            self.reg_map[int(i)] = 0

    def is_const(self, cur_ctx):
        if isinstance(cur_ctx, (RustMiniLangParser.BoolExpContext, 
                            RustMiniLangParser.NumExprContext, 
                            RustMiniLangParser.MinusNumExprContext)):
            return True
        return False

    def is_variable(self, cur_ctx):
        if isinstance(cur_ctx, (RustMiniLangParser.IdExprContext)):
            return True
        return False

    def alu_op(self, ctx):
        addr1 = self.visit(ctx.getChild(0))
        addr2 = self.visit(ctx.getChild(2))
        if self.is_variable(ctx.getChild(0)):
            op1 = self.get_reg()
            self.text += f"lw x{op1}, 0(x{addr1})\n"
        else:
            op1 = addr1
        if self.is_variable(ctx.getChild(2)):
            op2 = self.get_reg()
            self.text += f"lw x{op2}, 0(x{addr2})\n"
        else:
            op2 = addr2

        rd = self.get_reg()
        if ctx.getChild(1).getText() == '+':
            self.text += f"add x{rd}, x{op1}, x{op2}\n"
        elif ctx.getChild(1).getText() == '-':
            self.text += f"sub x{rd}, x{op1}, x{op2}\n"
        elif ctx.getChild(1).getText() == '*':
            self.text += f"mul x{rd}, x{op1}, x{op2}\n"
        elif ctx.getChild(1).getText() == '/':
            self.text += f"div x{rd}, x{op1}, x{op2}\n"
        elif ctx.getChild(1).getText() == '&':
            self.text += f"and x{rd}, x{op1}, x{op2}\n"
        elif ctx.getChild(1).getText() == '|':
            self.text += f"or x{rd}, x{op1}, x{op2}\n"
        elif ctx.getChild(1).getText() == "==":
            self.text += f"xor x{rd}, x{op1}, x{op2}\n"
            self.text += f"seqz x{rd}, x{rd}\n"
        elif ctx.getChild(1).getText() == "!=":
            self.text += f"xor x{rd}, x{op1}, x{op2}\n"
            self.text += f"snez x{rd}, x{rd}\n"
        elif ctx.getChild(1).getText() == "<":
            self.text += f"slt x{rd}, x{op1}, x{op2}\n"
        elif ctx.getChild(1).getText() == "<=":
            self.text += f"slt x{rd}, x{op2}, x{op1}\n"
            self.text += f"xori x{rd}, x{rd}, 1\n" 
        elif ctx.getChild(1).getText() == ">":
            self.text += f"sgt x{rd}, x{op1}, x{op2}\n"
        elif ctx.getChild(1).getText() == ">=":
            self.text += f"slt x{rd}, x{op1}, x{op2}\n"
            self.text += f"xori x{rd}, x{rd}, 1\n"
            
        self.free_reg([op1, op2, addr1, addr2])
        return rd

    # Visit a parse tree produced by RustMiniLangParser#minusNumExpr.
    def visitMinusNumExpr(self, ctx:RustMiniLangParser.MinusNumExprContext):
        rd = self.get_reg()
        self.data += f"li x{rd}, {ctx.getText()}\n"
        return rd


    # Visit a parse tree produced by RustMiniLangParser#compExpr.
    def visitCompExpr(self, ctx:RustMiniLangParser.CompExprContext):
        return self.alu_op(ctx)

    # Visit a parse tree produced by RustMiniLangParser#plusMinusExpr.
    def visitPlusMinusExpr(self, ctx:RustMiniLangParser.PlusMinusExprContext):
        return self.alu_op(ctx)

    # Visit a parse tree produced by RustMiniLangParser#boolExp.
    def visitBoolExp(self, ctx:RustMiniLangParser.BoolExpContext):
        rd = self.get_reg()
        self.text += f"li x{rd}, {int(bool(ctx.getText()))}\n"
        return rd


    # Visit a parse tree produced by RustMiniLangParser#andOrExpr.
    def visitAndOrExpr(self, ctx:RustMiniLangParser.AndOrExprContext):
        return self.alu_op(ctx)


    # Visit a parse tree produced by RustMiniLangParser#parenthesisExpr.
    def visitParenthesisExpr(self, ctx:RustMiniLangParser.ParenthesisExprContext):
        return self.visit(ctx.getChild(1))


    # Visit a parse tree produced by RustMiniLangParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:RustMiniLangParser.MulDivExprContext):
        return self.alu_op(ctx)


    # Visit a parse tree produced by RustMiniLangParser#numExpr.
    def visitNumExpr(self, ctx:RustMiniLangParser.NumExprContext):
        rd = self.get_reg()
        self.text += f"li x{rd}, {ctx.getText()}\n"
        return rd


    # Visit a parse tree produced by RustMiniLangParser#idExpr.
    def visitIdExpr(self, ctx:RustMiniLangParser.IdExprContext):
        rd = self.get_reg()
        self.text += f"la x{rd}, {ctx.getText()}\n"
        return rd


    def visitVarDecl(self, ctx:RustMiniLangParser.VarDeclContext):
        if self.is_const(ctx.getChild(6)):
            self.data += f"{ctx.getChild(2).getText()}:\n.word {get_int(ctx.getChild(6).getText())}\n"
        else:
            result = self.visit(ctx.getChild(6))
            addr = self.get_reg()
            self.data += f"{ctx.getChild(2).getText()}:\n.word 0\n"
            self.text += f"la x{addr}, {ctx.getChild(2).getText()}\nsw x{result}, 0(x{addr})\n"
            self.free_reg([result, addr])

    # Visit a parse tree produced by RustMiniLangParser#assignment.
    def visitAssignment(self, ctx:RustMiniLangParser.AssignmentContext):
        result = self.visit(ctx.getChild(2))
        addr = self.get_reg()
        self.text += f"la x{addr}, {ctx.getChild(0).getText()}\nsw x{result}, 0(x{addr})\n"
        self.free_reg([result, addr])


    # Visit a parse tree produced by RustMiniLangParser#compOperator.
    def visitCompOperator(self, ctx:RustMiniLangParser.CompOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#type.
    def visitType(self, ctx:RustMiniLangParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#printId.
    def visitPrintId(self, ctx:RustMiniLangParser.PrintIdContext):
        self.text += f"li x11, {ord(ctx.getChild(4).getText())}\naddi x10, x0, 11\necall\n"
        self.text += f"li x11, {32}\naddi x10, x0, 11\necall\n"
        self.text += f"li x11, {61}\naddi x10, x0, 11\necall\n"
        self.text += f"li x11, {32}\naddi x10, x0, 11\necall\n"
        self.text += f"la x12, {ctx.getChild(4).getText()}\nlw x11, 0(x12)\naddi x10, x0, 1\necall\n"
        self.text += f"li x11, {10}\naddi x10, x0, 11\necall\n"

    # Visit a parse tree produced by RustMiniLangParser#printNum.
    def visitPrintNum(self, ctx:RustMiniLangParser.PrintNumContext):
        self.text += f"li x11, {ctx.getChild(3).getText()}\naddi x10, x0, 1\necall\n"
        self.text += f"li x11, {10}\naddi x10, x0, 11\necall\n"


    # Visit a parse tree produced by RustMiniLangParser#blockstmt.
    def visitBlockstmt(self, ctx:RustMiniLangParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#ifstmt.
    def visitIfstmt(self, ctx:RustMiniLangParser.IfstmtContext):
        result = self.visit(ctx.getChild(2))
        if ctx.getChildCount() == 5: # if
            self.text += f"beqz x{result}, endif{(self.if_cnt)}\n"
            self.visit(ctx.getChild(4))
        else: 
            self.text += f"beqz x{result}, else{(self.if_cnt)}\n"
            self.visit(ctx.getChild(4))
            self.text += f"j endif{(self.if_cnt)}\n"
            self.text += f"else{(self.if_cnt)}:\n"
            self.visit(ctx.getChild(5))
        self.text += f"endif{(self.if_cnt)}:\n"
        self.if_cnt+=1
        self.free_reg([result])

    # Visit a parse tree produced by RustMiniLangParser#elsestmt.
    def visitElsestmt(self, ctx:RustMiniLangParser.ElsestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RustMiniLangParser#whilestmt.
    def visitWhilestmt(self, ctx:RustMiniLangParser.WhilestmtContext):
        self.text += f"startwhile{(self.while_cnt)}:\n"
        rd = self.visit(ctx.getChild(2))
        self.text += f"beqz x{rd}, endwhile{(self.while_cnt)}\n"
        self.visit(ctx.getChild(4))
        self.text += f"j startwhile{(self.while_cnt)}\n"
        self.text += f"endwhile{(self.while_cnt)}:\n"
        self.while_cnt+=1
        self.free_reg([rd])


    # Visit a parse tree produced by RustMiniLangParser#forstmt.
    def visitForstmt(self, ctx:RustMiniLangParser.ForstmtContext):
        if ctx.getChild(1).getText() in self.data:
            addr = self.get_reg()
            result = self.get_reg()
            self.text += f"li x{result}, {get_int(ctx.getChild(3).getText())}\n"
            self.text += f"la x{addr}, {ctx.getChild(1).getText()}\nsw x{result}, 0(x{addr})\n"
            self.free_reg([result, addr])
        else:
            self.data += f"{ctx.getChild(1).getText()}:\n.word {get_int(ctx.getChild(3).getText())}\n"
        self.text += f"startfor{(self.for_cnt)}:\n"
        addr = self.get_reg()
        result = self.get_reg()
        self.text += f"la x{addr}, {ctx.getChild(1).getText()}\nlw x{result}, 0(x{addr})\n"
        self.text += f"addi x{result}, x{result}, -{ctx.getChild(5).getText()}\n"
        self.text += f"beq x{result}, x0, endfor{(self.for_cnt)} \n"
        self.visit(ctx.getChild(6))
        self.text += f"la x{addr}, {ctx.getChild(1).getText()}\nlw x{result}, 0(x{addr})\n"
        self.text += f"addi x{result}, x{result}, 1\n"
        self.text += f"sw x{result}, 0(x{addr})\n"
        self.free_reg([result, addr])
        self.text += f"j startfor{(self.for_cnt)}\n"
        self.text += f"endfor{(self.for_cnt)}:\n"
        self.for_cnt+=1


    def visitStmt(self, ctx:RustMiniLangParser.StmtContext):
        self.visit(ctx.getChild(0))
        return 0

    def visitProgram(self, ctx:RustMiniLangParser.ProgramContext):
        for i in range(0, ctx.getChildCount()):
            self.cur_string = ctx.getChild(i).getText()
            self.visit(ctx.getChild(i))

        my_file = open("output.S", "w+")
        my_file.write(self.data)
        my_file.write(self.text)
        my_file.write("\naddi a0, x0, 10\necall")
        my_file.close()
        
        return 0