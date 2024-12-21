import sys
from antlr4 import *
from RustMiniLangLexer import RustMiniLangLexer
from RustMiniLangParser import RustMiniLangParser
from MyVisitorInterpreter import MyVisitorInterpreter
from MyVisitorCompiler import MyVisitorCompiler

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = RustMiniLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RustMiniLangParser(stream)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        print("=== START INTERPRETER ===")
        vinterp = MyVisitorInterpreter()
        vinterp.visit(tree)
        print("=== START COMPILER ===")
        vinterp = MyVisitorCompiler()
        vinterp.visit(tree)


if __name__ == '__main__':
    main(sys.argv)