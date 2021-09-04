import ply.lex as lex

tokens = (
    'IDENTIFIER', 'CONSTANT', 'STRING_LITERAL', 'SIZEOF', 'PTR_OP', 'CHARACTER',
    'INC_OP', 'DEC_OP', 'LEFT_OP', 'RIGHT_OP', 'LE_OP',
    'GE_OP', 'EQ_OP', 'NE_OP', 'AND_OP', 'OR_OP',
    'TYPEDEF', 'EXTERN', 'STATIC', 'CHAR', 'SHORT', 'INT', 'LONG',
    'SIGNED', 'UNSIGNED', 'FLOAT', 'DOUBLE', 'CONST', 'VOLATILE',
    'VOID', 'STRUCT', 'UNION', 'ENUM', 'CASE', 'DEFAULT', 'IF', 
    'ELSE', 'SWITCH', 'WHILE',  'FOR', #'DO',
    'CONTINUE', 'BREAK', 'RETURN', 'SEMI', 'L_BRACE', 'R_BRACE',
    'COMMA', 'COLON', 'EQUAL', 'L_PAREN',
    'R_PAREN', 'R_SQUARE', 'L_SQUARE', 'DOT', 'AMP', 'EXCLAIM', 'TILDA',
    'MINUS', 'PLUS', 'STAR', 'SLASH', 'PERCENT', 'CARET', 'LESS',
    'GREATER', 'PIPE', 'QUEST', 
    'MUL_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN', 'ADD_ASSIGN', 'SUB_ASSIGN',
    'LEFT_ASSIGN', 'RIGHT_ASSIGN', 'AND_ASSIGN',
    'XOR_ASSIGN', 'OR_ASSIGN', 'ELLIPSIS', 'AUTO', 'REGISTER', 'GOTO',
)

reserved = {
    'typedef':'TYPEDEF',
    'break': 'BREAK',
    'case':'CASE',
    'char':'CHAR',
    'const':'CONST',
    'continue':'CONTINUE',
    'default':'DEFAULT',
    'do':'DO',
    'double':'DOUBLE',
    'else':'ELSE',
    'enum':'ENUM',
    "extern" : "EXTERN",
    "float" : "FLOAT", 
    "for" : "FOR",
#    "goto": "GOTO",
    "if"	: "IF",
    "int" : "INT",
    "long"	: "LONG",
#    "register"	: "REGISTER",
    "return" : "RETURN",
    "short"	: "SHORT",
    "signed" :	"SIGNED",
    "sizeof" : "SIZEOF",
    "static" : "STATIC",
    "struct" : "STRUCT",
    "switch" : "SWITCH",
    "typedef" : "TYPEDEF",
    "union"	: "UNION", 
    "unsigned"	: "UNSIGNED",
    "void"	: "VOID",
    "volatile"	: "VOLATILE",
    "while"	: "WHILE",
    "auto" : "AUTO",
    "register" : "REGISTER",
    "goto" : "GOTO",
}

D = r'[0-9]'
L = r'[a-zA-Z_]'
H = r'[a-fA-F0-9]'
#E = r'[Ee][+-]?{D}+'
E = r'[Ee][+-]?'+D
FS = r'(f|F|l|L)'
IS = r'(u|U|l|L)*'

identifier = L+r'('+L+r'|'+D+r')*'
#print("identifier reg exp = ", identifier)
const_exp1 = r'0[xX]'+H+IS+r'?'
const_exp2 = r'0'+D+r'+'+IS+r'?'
const_exp3 = D+r'+'+IS+r'?'
const_exp4 = D+r'+'+E+FS+r'?'
const_exp5 = D+r'*\.'+D+r'+('+E+r')?'+FS+r'?'
const_exp6 = D+r'+\.'+D+r'*('+E+r')?'+FS+r'?'
all_const_exp = r'('+const_exp1 + r')|(' + const_exp2 + r')|(' + const_exp3 + r')|('+const_exp4+r')|('+const_exp5+r')|('+const_exp6+')'



#Maintaining in descending order of length - same order in which the regular expressions are matched by PLY
t_ELLIPSIS = r'\.\.\.'
t_RIGHT_ASSIGN = r'>>='
t_LEFT_ASSIGN = r'<<='
t_ignore = ' \t'
t_ADD_ASSIGN = r'\+='
t_SUB_ASSIGN = r'-='
t_MUL_ASSIGN = r'\*='
t_DIV_ASSIGN = r'/='
t_AND_ASSIGN = r'&='
t_XOR_ASSIGN = r'\^='
t_OR_ASSIGN = r'\|='
t_RIGHT_OP = r'>>'
t_LEFT_OP = r'<<'
t_INC_OP = r'\+\+'
t_DEC_OP = r'--'
t_PTR_OP = r'->'
t_AND_OP = r'&&'
t_OR_OP = r'\|\|'
t_LE_OP = r'<='
t_GE_OP = r'>='
t_EQ_OP = r'=='
t_NE_OP = r'!='
t_SEMI = r';'
t_L_BRACE = r'{'
t_R_BRACE = r'}'
t_COMMA = r','
t_COLON = r':'
t_EQUAL = r'='
t_L_PAREN = r'\('
t_R_PAREN = r'\)'
t_L_SQUARE = r'\['
t_R_SQUARE = r'\]'
t_DOT = r'\.'
t_AMP = r'&'
t_EXCLAIM = r'!'
t_TILDA = r'~'
t_MINUS = r'-'
t_PLUS = r'\+'
t_STAR = r'\*'
t_SLASH = r'\/'
t_PERCENT = r'%'
t_CARET = r'\^'
t_LESS = r'<'
t_GREATER = r'>'
t_PIPE = r'\|'
t_QUEST = r'\?'

def t_CHARACTER(t):
    ''' \'[^\']\' '''
    t.value = t.value[1:-1]
    return t

@lex.TOKEN(identifier)
def t_IDENTIFIER(t):
     t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
     #print(t)
     return t
     
def t_COMMENT(t):
     r'(/\*(.|\n)*?\*/)|(//.*)'
     pass  #token ignored 
     
#t_STRING_LITERAL = '\"[^\\"]*\"'

def t_STRING_LITERAL(t):
    ''' \"[^\"]*\" '''
    t.value = t.value[1:-1]
    #Removing the enclosing double quotes from the string
    #print(t)
    return t
    
@lex.TOKEN(all_const_exp)
def t_CONSTANT(t):
    #print("t.type = ", t.type)
    #print(t)
    t.type = 'CONSTANT'
    return t
    
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)    
    

# Error handling rule
def t_error(t):
     print("Illegal character '%s' at line %d" % (t.value[0], t.lexer.lineno))
     t.lexer.skip(1)
 
'''     
# EOF handling rule
def t_eof(t):
     # Get more input (Example)
     #more = raw_input('... ')
     try:
        next_line = input()
     except EOFError:
        return None
     else:
         print("In t_eof")  
         lexer.input(next_line)
         return lexer.token()
'''

lexer = lex.lex() 
'''    
for tok in lexer:
    print(tok)
'''

