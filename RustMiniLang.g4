grammar RustMiniLang;

program: (stmt)* EOF;

stmt: varDecl
    | assignment
    | printId
    | printNum
    | ifstmt
    | blockstmt
    | whilestmt
    | forstmt
    ;

expr: '(' expr ')'                               #parenthesisExpr
    | left=expr op=(ASTERISK | SLASH) right=expr  #mulDivExpr
    | left=expr op=(PLUS | MINUS) right=expr      #plusMinusExpr
    | left=expr op=(AND | OR) right=expr          #andOrExpr
    | left=expr compOperator right=expr          #compExpr
    | BOOL                                          #boolExp
    | NUM                                         #numExpr
    | '-' NUM                                     #minusNumExpr
    | ID                                        #idExpr
    ;

varDecl: 'let' 'mut' ID ':' type '=' expr ';';
assignment: ID '=' expr ';';
compOperator: op=(LESS | LESS_OR_EQUAL | EQUAL | NOT_EQUAL | GREATER | GREATER_OR_EQUAL);
type: 'i32' | 'bool';

printId: 'println!' '(' '"' '{' ID '}' '"' ')' ';';
printNum: 'println!' '(' '"' NUM '"' ')' ';';
blockstmt: '{' (stmt)* '}';
ifstmt: 'if' '(' expr ')' stmt elsestmt?;
elsestmt: 'else' stmt;
whilestmt: 'while' '(' expr ')' stmt;
forstmt: 'for' ID 'in' NUM '..' NUM stmt;

BOOL: 'true' | 'false';
AND: '&';
OR: '|';
ASTERISK: '*';
SLASH: '/';
PLUS: '+';
MINUS: '-';
ASSIGN: '=';
EQUAL: '==' ;
NOT_EQUAL: '!=' ;
LESS: '<';
LESS_OR_EQUAL: '<=' ;
GREATER: '>';
GREATER_OR_EQUAL: '>=';
NUM: [0-9]+;
ID: [a-zA-Z_] [a-zA-Z_0-9]*;

SPACE: [ \r\n\t]+ -> skip;
LINE_COMMENT: '//' ~[\n\r]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;