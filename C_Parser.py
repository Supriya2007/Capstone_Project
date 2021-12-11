import ply.yacc as yacc
from C_Lex import tokens
import copy
import re

start = 'translation_unit' #Sets the Start Symbol

#def before_parse_main():
#ADD

def p_primary_expression(p):
    '''
    primary_expression : variable_use
    | const_or_parenthesis
    '''
    p[0] = p[1]
    #print("p_primary_expression", p[0])
    
def p_const_or_parenthesis(p): 
    '''
    const_or_parenthesis : CONSTANT
    | CHARACTER
    | STRING_LITERAL
    | L_PAREN expression R_PAREN
    '''  
    p[0] = {}
    if(len(p)==2):
        LINE = p.lineno(1)
        #p[0]['name'] = p[1]
        p[0]['line'] = LINE
        p[0]['exp'] = [ p[1] ]
    elif(len(p)==4):
        LINE = p.lineno(1)
        p[0]['line'] = p[2]['line']
        p[0]['exp'] = [ p[1] ] + p[2]['exp'] + [ p[3] ]
        if('name' in p[2]):
            p[0]['name'] = p[2]['name']
    else:
        print("ERROR in p_const_or_parenthesis")
    #print("p_const_or_parenthesis:",p[0])

def p_variable_use(p):
    '''
    variable_use : IDENTIFIER
    '''
    NAME = p[1]
    LINE = p.lineno(1)
    p[0] = {}
    p[0]['name'] = NAME
    p[0]['line'] = LINE
    p[0]['exp'] = [ NAME ]
    #print("variable_use:", p[0])
    #ADD

def p_function_call(p):
    '''
    function_call : IDENTIFIER L_PAREN R_PAREN
    | IDENTIFIER L_PAREN argument_expression_list R_PAREN
    '''
    NAME = p[1]
    #print(NAME)
    LINE = p.lineno(1)
    p[0] = {}
    p[0]['line'] = LINE
    p[0]['name'] = NAME
    FUNC_ARGS = []
    if(len(p) == 4):
        p[0]['exp'] = [p[1]] + [p[2]] + [p[3]]
    elif(len(p) == 5):
        p[0]['exp'] = [p[1]] + [p[2]] + p[3]['exp'] + [p[4]]
        FUNC_ARGS = p[3]['name']
    EXP = p[0]['exp']
    #p[0]['func_args']=p[0]['exp'][2:-1:2]
    #FUNC_ARGS = p[0]['func_args']
    #example of adding an attribute can be:
    #FUNC_ARGS = [(type, arg_name)...] - for user to be able to use it in this production
    #p[0]['func_args'] = FUNC_ARGS - for user to be able to use it in parent productions
    
    #ADD    

def p_postfix_expression(p):
    '''
    postfix_expression : primary_expression
    | postfix_expression L_SQUARE expression R_SQUARE
    | postfix_expression DOT IDENTIFIER
    | postfix_expression PTR_OP IDENTIFIER
    | postfix_expression INC_OP
    | postfix_expression DEC_OP
    | function_call
    '''
    if(len(p)==2): 
        p[0] = p[1] #function_call case not handled 
    elif(len(p)==3): #INC_OP and DEC_OP
        LINE = p.lineno(2)
        p[0] = {}
        p[0]['line'] = LINE
        p[0]['exp'] = p[1]['exp'] + [p[2]]
        if('name' in p[1]):
             p[0]['name'] = p[1]['name']
    elif(len(p)==4): #DOT and PTR (->)
        LINE = p.lineno(2)
        p[0] = {}
        p[0]['lhs'] = p[1]['exp']
        p[0]['rhs'] = [p[3]]
        p[0]['exp'] = p[0]['lhs'] + [ p[2] ] + p[0]['rhs']
        p[0]['line'] = LINE
        p[0]['name'] = p[3] #setting name to var following '->'
    elif(len(p)==5): #ARRAY
        LINE = p.lineno(2)
        p[0] = {}
        p[0]['exp'] = p[1]['exp'] + [ p[2] ] + p[3]['exp'] + [p[4]]
        p[0]['line'] = LINE
        if 'name' in p[1]:
            p[0]['name'] = p[1]['name']
    else:
        print("ERROR in p_postfix_expression")
    #print("postfix exp:", p[0])
    #ADD

def p_argument_expression_list(p):
    '''
    argument_expression_list : assignment_expression
    | argument_expression_list COMMA assignment_expression
    '''
    p[0] = {}
    p[0]['name'] = []
    if(len(p) == 2):
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp']
        if('name' in p[1]):
            p[0]['name'] = [p[1]['name']]
        #NAME = p[1]['name']
    elif(len(p) == 4):
        p[0] = {}
        p[0]['exp'] = p[1]['exp'] + [p[2]] + p[3]['exp']
        p[0]['line'] = p[1]['line']
        p[0]['name'] = p[1]['name'] 
        if('name' in p[3]):
            p[0]['name'].append(p[3]['name'])
    
def p_unary_expression(p):
    '''
    unary_expression : postfix_expression
    | INC_OP unary_expression
    | DEC_OP unary_expression
    | unary_op_before_cast_exp
    | SIZEOF unary_expression
    | SIZEOF L_PAREN type_name R_PAREN
    '''
    NAME = ""
    if(len(p) == 2):
        p[0] = p[1] #NAME is empty in this case
    elif(len(p) == 3):
        p[0] = {}
        p[0]['line'] = p[2]['line'] 
        #line can also be got as p.lineno(1). Will be the same.
        #p[0]['name'] = p[2]['exp']
        p[0]['exp'] = [ p[1] ] + p[2]['exp']
        if(p[1] == 'sizeof'):
             p[0]['name'] = 'sizeof'
        elif('name' in p[2]):
            p[0]['name'] = p[2]['name']
    elif(len(p) == 5):
        p[0] = {}
        p[0]['line'] = p[3]['line']
        p[0]['exp'] = [ p[1] ] + [ p[2] ] + p[3]['exp'] + [ p[4] ]
        p[0]['name'] = "sizeof"
    else:
        print("ERROR in p_unary_expression")
    #print("p_unary_expression:", p[0])    
    if('name' in p[0]):
        NAME = p[0]['name']
        #print("name =", NAME)
    EXP = p[0]['exp']
    #Can handle name better, now that we have attribute grammar - check
    #ADD
    
def p_unary_op_before_cast_exp(p):
    '''
    unary_op_before_cast_exp : unary_operator cast_expression
    '''   
    p[0] = p[1]
    p[0]['line'] = p[1]['line']
    p[0]['exp'] = p[1]['exp'] + p[2]['exp']
    if('name' in p[2]):
        p[0]['name'] = p[2]['name']
    #print("p_unary_op_before_cast_exp:", p[0])

def p_unary_operator(p):
    '''
    unary_operator : AMP
    | STAR
    | PLUS
    | MINUS
    | TILDA
    | EXCLAIM
    '''
    LINE = p.lineno(1)
    p[0] = {}
    p[0]['line'] = LINE
    p[0]['exp'] = [ p[1] ]
    #print("p_unary_operator:", p[0])

def p_cast_expression(p):
    '''
    cast_expression : unary_expression
    | L_PAREN type_name R_PAREN cast_expression
    '''
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p)==5): 
        p[0] = {}
        p[0]['line'] = p.lineno(1)
        p[0]['exp'] = [p[1]] + p[2]['exp'] + [p[3]] + p[4]['exp']
        p[0]['name'] = p[4]['name']
    else:
        print("ERROR in p_cast_expression")
    #print("p_cast_expression:", p[0])

def p_multiplicative_expression(p):
    '''
    multiplicative_expression : cast_expression
    | multiplicative_expression STAR cast_expression
    | multiplicative_expression SLASH cast_expression
    | multiplicative_expression PERCENT cast_expression
    '''
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p)==4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['lhs'] = p[1]['exp']
        p[0]['rhs'] = p[3]['exp']
        p[0]['exp'] = p[0]['lhs'] + [ p[2] ] + p[0]['rhs']
    else:
        print("ERROR in p_multiplicative_expression")
    #print("p_multiplicative_expression:", p[0])


def p_additive_expression(p):
    '''
    additive_expression : multiplicative_expression
    | additive_expression PLUS multiplicative_expression
    | additive_expression MINUS multiplicative_expression
    '''
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p)==4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['lhs'] = p[1]['exp']
        p[0]['rhs'] = p[3]['exp']
        p[0]['exp'] = p[0]['lhs'] + [ p[2] ] + p[0]['rhs']
    else:
        print("ERROR in p_additive_expression")
    #print("In p_additive_expression:", p[0])

def p_shift_expression(p):
    '''
    shift_expression : additive_expression
    | shift_expression LEFT_OP additive_expression
    | shift_expression RIGHT_OP additive_expression
    '''
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p) == 4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['lhs'] = p[1]['exp']
        p[0]['rhs'] = p[3]['exp']
        p[0]['exp'] = p[0]['lhs'] + [ p[2] ] + p[0]['rhs']
    #Only handling 1st case in all these productions -- DONE
    #print("p_shift_expression:", p[0])

def p_relational_expression(p):
    '''
    relational_expression : shift_expression
    | relational_expression LESS shift_expression
    | relational_expression GREATER shift_expression
    | relational_expression LE_OP shift_expression
    | relational_expression GE_OP shift_expression
    '''
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p) == 4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['lhs'] = p[1]['exp']
        p[0]['rhs'] = p[3]['exp']
        p[0]['exp'] = p[0]['lhs'] + [ p[2] ] + p[0]['rhs']
    #print("p_relational_expression:", p[0])
    pass

def p_equality_expression(p):
    '''
    equality_expression : relational_expression
    | equality_exp_lhs EQ_OP relational_expression
    | equality_exp_lhs NE_OP relational_expression
    '''
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p) == 4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['lhs'] = p[1]['exp']
        p[0]['rhs'] = p[3]['exp']
        p[0]['exp'] = p[0]['lhs'] + [ p[2] ] + p[0]['rhs']
    #print("p_equality_expression:", p[0])
    EXP = p[0]['exp']
    #ADD   

def p_equality_exp_lhs(p):
    '''
    equality_exp_lhs : equality_expression
    '''
    p[0] = {}
    p[0]['line'] = p[1]['line']
    p[0]['exp'] = p[1]['exp']
    #print("p_equality_exp_lhs:", p[0])
    #ADD

def p_and_expression(p):
    '''
    and_expression : equality_expression
    | and_expression AMP equality_expression
    '''
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p) == 4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['lhs'] = p[1]['exp']
        p[0]['rhs'] = p[3]['exp']
        p[0]['exp'] = p[0]['lhs'] + [ p[2] ] + p[0]['rhs']
    #print("p_and_expression:", p[0])
    #ADD

def p_exclusive_or_expression(p):
    '''
    exclusive_or_expression : and_expression
    | exclusive_or_expression CARET and_expression
    '''
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p) == 4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['lhs'] = p[1]['exp']
        p[0]['rhs'] = p[3]['exp']
        p[0]['exp'] = p[0]['lhs'] + [ p[2] ] + p[0]['rhs']
    #print("p_exclusive_or_expression:", p[0])
    #ADD

def p_inclusive_or_expression(p):
    '''
    inclusive_or_expression : exclusive_or_expression
    | inclusive_or_expression PIPE exclusive_or_expression
    '''
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p) == 4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['lhs'] = p[1]['exp']
        p[0]['rhs'] = p[3]['exp']
        p[0]['exp'] = p[0]['lhs'] + [ p[2] ] + p[0]['rhs']
    #print("p_inclusive_or_expression:", p[0])
    #ADD

def p_logical_and_expression(p):
    '''
    logical_and_expression : inclusive_or_expression
    | logical_and_expression AND_OP inclusive_or_expression
    '''
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p) == 4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['lhs'] = p[1]['exp']
        p[0]['rhs'] = p[3]['exp']
        p[0]['exp'] = p[0]['lhs'] + [ p[2] ] + p[0]['rhs']
    #print("p_logical_and_expression:", p[0])
    #ADD

def p_logical_or_expression(p):
    '''
    logical_or_expression : logical_and_expression
    | logical_or_expression OR_OP logical_and_expression
    '''
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p)==4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['lhs'] = p[1]['exp']
        p[0]['rhs'] = p[3]['exp']
        p[0]['exp'] = p[0]['lhs'] + [ p[2] ] + p[0]['rhs']
    else:
        print("ERROR in p_logical_or_expression")
    #print("p_logical_and_expression:", p[0])
    #ADD

def p_conditional_expression(p):
    '''
    conditional_expression : logical_or_expression
    | logical_or_expression QUEST expression COLON conditional_expression
    '''
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p)==6):
        p[0] = {}
        p[0]['line'] = p.lineno(1)
        p[0]['exp'] = p[1]['exp'] + [p[2]] + p[3]['exp'] + [p[4]] + p[5]['exp']
    else:
        print("ERROR in p_conditional_expression")
    #print("p_conditional_expression:", p[0])
    #ADD

def p_assignment_expression(p):
    '''
    assignment_expression : conditional_expression
    | assignment_lhs assignment_operator assignment_expression
    '''
    LHS = RHS = EXP = []
    NAME = ''
    RHS_NAME = ''
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p)==4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['lhs'] = p[1]['exp']
        p[0]['rhs'] = p[3]['exp']
        p[0]['exp'] = p[1]['exp']+ p[2]['exp'] + p[3]['exp']
        LHS = p[0]['lhs']
        RHS = p[0]['rhs']
        NAME = LHS[-1] #LHS may have * operator, hence assigning to the last element, which must be the identifier name
        if('name' in p[3]):
            RHS_NAME = p[3]['name']
    else:
        print("ERROR in p_assignment_expression")    
    #print("assignment_expression:", p[0])
    EXP = p[0]['exp']
    LINE = p[0]['line']
    #print("RHS_NAME", RHS_NAME)
    #ADD
    
def p_assignment_lhs(p):
    '''
    assignment_lhs : unary_expression
    ''' 
    p[0] = p[1]  #Support NAME here?
    #print("p_assignment_lhs:", p[0])
    #ADD

def p_assignment_operator(p):
    '''
    assignment_operator : EQUAL
    | MUL_ASSIGN
    | DIV_ASSIGN
    | MOD_ASSIGN
    | ADD_ASSIGN
    | SUB_ASSIGN
    | LEFT_ASSIGN
    | RIGHT_ASSIGN
    | AND_ASSIGN
    | XOR_ASSIGN
    | OR_ASSIGN
    '''
    p[0] = {}
    LINE = p.lineno(1)
    p[0]['line'] = LINE
    p[0]['exp'] = [ p[1] ]
    #print("p_assignment_operator:", p[0])
    #ADD

def p_expression(p):
    '''
    expression : assignment_expression
    | expression COMMA assignment_expression
    '''
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p)==4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp'] + [p[2]] + p[3]['exp']
    #print("In p_expression: ", p[0])
    EXP = p[0]['exp']
    LINE = p[0]['line']
    #ADD

def p_constant_expression(p):
    '''
    constant_expression : conditional_expression
    '''
    p[0] = p[1]
    #print("p_constant_expression:", p[0])
    #ADD

def p_declaration(p):
    '''
    declaration : declaration_specifiers SEMI
    | declaration_specifiers init_declarator_list SEMI
    '''
    p[0] = copy.deepcopy(p[1])
    NAME = []
    INITIAL_VALUES = {} #not part of p[0]
    #p[0]['line'] = p.lineno(1)
    if(len(p) == 3):
        p[0]['exp'] = p[1]['exp'] + [ p[2] ]
    elif(len(p) == 4):
        p[0]['exp'] = p[1]['exp'] + p[2]['exp'] + [ p[3] ]
        p[0]['name'] = p[2]['name']
        #print("init_declarator_list:", p[2]) 
        #for term in p[2]['exp']:
        #    if(term.isidentifier()):
        #        NAMES.append(term)
        if('initial_value' in p[2]):
            INITIAL_VALUES = p[2]['initial_value']
        NAME = p[0]['name']
    EXP = p[0]['exp']
    TYPE = p[1]['exp'] #not part of p[0]
    #ADD

def p_declaration_specifiers(p):
    '''
    declaration_specifiers : storage_class_specifier
    | storage_class_specifier declaration_specifiers
    | type_specifier
    | type_specifier declaration_specifiers
    | type_qualifier
    | type_qualifier declaration_specifiers
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 3):
        p[0] = {}
        p[0]['line'] = p.lineno(1)
        p[0]['exp'] = p[1]['exp'] + p[2]['exp']
    LINE = p[0]['line']
    EXP = p[0]['exp']
    #ADD

def p_init_declarator_list(p):
    '''
    init_declarator_list : init_declarator
    | init_declarator_list COMMA init_declarator
    '''
    #p[0] = {}
    #p[0]['line'] = p[1]['line']
    p[0] = copy.deepcopy(p[1])
    p[0]['initial_value'] = {} # will overwrite if p[1] had 'initial_value' attribute
    NAMES=[]
    if(len(p)==2):
        p[0]['name'] = [p[1]['name']]
        if('initial_value' in p[1]):
            p[0]['initial_value'] = {p[1]['name']:p[1]['initial_value']} 
    elif(len(p)==4):
        p[0]['exp'] = p[1]['exp'] + [ p[2] ] + p[3]['exp']
        p[0]['name'] = p[1]['name'] + [p[3]['name']]
        p[0]['initial_value'] = p[1]['initial_value']
        if('initial_value' in p[3]):
            p[0]['initial_value'][p[3]['name']] = p[3]['initial_value']
    else:
        print("ERROR in p_init_declarator_list")
    #print("p_init_declarator_list", p[0])  
    #ADD  
    
def p_init_declarator(p):
    '''
    init_declarator : uninitialized_declaration
    | initialized_declaration
    '''
    p[0] = p[1]
    #print("p_init_declarator", p[0])
    #ADD
    
def p_initialized_declaration(p):
    '''
    initialized_declaration : declarator EQUAL initializer
    '''
    p[0] = copy.deepcopy(p[1])
    p[0].update(p[3])
    p[0]['lhs'] = p[1]['exp']
    p[0]['rhs'] = p[3]['exp']
    p[0]['exp'] = p[1]['exp'] + [ p[2] ] + p[3]['exp']; 
    p[0]['name'] = p[1]['name']
    p[0]['initial_value'] = p[3]['exp']
    LHS = p[0]['lhs']
    RHS = p[0]['rhs']
    EXP = p[0]['exp']
    ARR_SIZE = ''
    LINE = p[0]['line']
    NAME = p[1]['name']
    if(p[0].get('arr_size')): #None returned in case LHS is not an array
        ARR_SIZE = p[0]['arr_size']
    #p[] = dict with 2 keys lhs, rhs
    #print("p_initialized_declaration", p[0])
    #ADD 
       
def p_uninitialized_declaration(p):   
    '''
    uninitialized_declaration : declarator
    '''  
    NAME = p[1]['name']
    p[0] = p[1]
    #print("p_uninitialized_declaration", p[0])
    #ADD  

def p_storage_class_specifier(p):
    '''
    storage_class_specifier : TYPEDEF
    | EXTERN
    | STATIC
    | AUTO
    | REGISTER
    '''
    p[0] = {}
    p[0]['line'] = p.lineno(1)
    p[0]['exp'] = [ p[1] ]
    #print("p_storage_class_specifier:", p[0])
    #ADD

def p_type(p):
    '''
    type : VOID
    | CHAR
    | SHORT
    | INT
    | LONG
    | FLOAT
    | DOUBLE
    | SIGNED
    | UNSIGNED
    '''
    p[0] = {}
    p[0]['line'] = p.lineno(1)
    p[0]['type'] = p[1]
    TYPE =p[1]
    p[0]['exp'] = [ p[1] ]

def p_type_specifier(p):
    '''
    type_specifier : type
    | struct_or_union_specifier
    | enum_specifier
    '''
    p[0] = p[1]
    EXP=p[0]['exp']
    if('name' in p[0]):
        NAME=p[0]['name']
    #print("p_type_specifier:", p[0])
    #ADD

def p_struct_or_union_specifier(p):
    '''
    struct_or_union_specifier : struct_or_union IDENTIFIER L_BRACE struct_declaration_list R_BRACE
    | struct_or_union L_BRACE struct_declaration_list R_BRACE
    | struct_or_union IDENTIFIER
    '''
    if(len(p) == 6):
        p[0] ={}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp'] + [p[2]] + [p[3]] + p[4]['exp'] + [p[5]]
        p[0]['name'] = p[2]
        p[0]['struct_members'] = p[4]['struct_members']
    elif(len(p) == 5):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp'] + [p[2]] + p[3]['exp'] + [p[4]]
        p[0]['struct_members'] = p[3]['struct_members']
    elif(len(p) == 3):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp'] + [p[2]]
        p[0]['name'] = p[2]
    LINE = p[0]['line']
    EXP = p[0]['exp']
    NAME = ''
    if('name' in p[0]):
        NAME = p[0]['name']
    STRUCT_MEMBERS = []    
    if('struct_members' in p[0]):
        STRUCT_MEMBERS = p[0]['struct_members']
    #print("p_struct_or_union_specifier:", p[0])
    #ADD

def p_struct_or_union(p):
    '''
    struct_or_union : STRUCT
    | UNION
    '''
    p[0] = {}
    p[0]['line'] = p.lineno(1)
    p[0]['exp'] = [ p[1] ]
    p[0]['type'] = p[1]
    TYPE = p[1]
    #print("p_struct_or_union:", p[0])
    #ADD

def p_struct_declaration_list(p):
    '''
    struct_declaration_list : struct_declaration
    | struct_declaration_list struct_declaration
    '''
    if(len(p) == 2):
        p[0] = p[1]
        p[0]['struct_members'] = [{'type':p[1]['type'], 'declarators':p[1]['declarators']}]
    elif(len(p) == 3):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp'] + p[2]['exp']
        p[0]['struct_members'] = p[1]['struct_members']+[{'type':p[2]['type'], 'declarators':p[2]['declarators']}]
    EXP=p[0]['exp']

    #print("p_struct_declaration_list:", p[0])
    #ADD

def p_struct_declaration(p):
    '''
    struct_declaration : specifier_qualifier_list struct_declarator_list SEMI
    '''
    p[0] = {}
    p[0]['line'] = p[1]['line']
    p[0]['exp'] = p[1]['exp'] + p[2]['exp'] + [p[3]]
    #print("p_struct_declaration:", p[0])
    p[0]['type'] = p[1]['exp']
    p[0]['declarators'] = p[2]['exp'] #variable name and '*' if its a pointer
    #ADD

def p_specifier_qualifier_list(p):
    '''
    specifier_qualifier_list : type_specifier specifier_qualifier_list
    | type_specifier
    | type_qualifier specifier_qualifier_list
    | type_qualifier
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 3):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp'] + p[2]['exp']
    #print("p_specifier_qualifier_list:", p[0])
    #ADD

def p_struct_declarator_list(p):
    '''
    struct_declarator_list : struct_declarator
    | struct_declarator_list COMMA struct_declarator
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp'] + [p[2]] + p[3]['exp']
    #print("p_struct_declarator_list:", p[0])
    #ADD

def p_struct_declarator(p):
    '''
    struct_declarator : declarator
    | COLON constant_expression
    | declarator COLON constant_expression
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 3):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = [p[1]] + p[2]['exp']
    elif(len(p) == 4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp'] + [p[2]] + p[3]['exp']
    #ADD
    
def p_enum_specifier(p):
    '''
    enum_specifier : ENUM L_BRACE enumerator_list R_BRACE
    | ENUM IDENTIFIER L_BRACE enumerator_list R_BRACE
    | ENUM IDENTIFIER
    '''
    p[0] = {}
    p[0]['line'] = p.lineno(1)
    p[0]['type'] = p[1]
    TYPE = p[1]
    if(len(p) == 3):
        p[0]['exp'] = [p[1]] + [p[2]]
        p[0]['name'] = p[2]
    elif(len(p) == 5):
        p[0]['exp'] = [p[1]] + [p[2]] + p[3]['exp'] + [p[4]]
    elif(len(p) == 6):
        p[0]['exp'] = [p[1]] + [p[2]] + [p[3]] + p[4]['exp'] + [p[5]]
        p[0]['name'] = p[2]
    #ADD

def p_enumerator_list(p):
    '''
    enumerator_list : enumerator
    | enumerator_list COMMA enumerator
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp'] + [p[2]] + p[3]['exp']
    #ADD

def p_enumerator(p):
    '''
    enumerator : IDENTIFIER
    | IDENTIFIER EQUAL constant_expression
    '''
    p[0] = {}
    p[0]['line'] = p.lineno(1)
    if(len(p) == 2):
        p[0]['exp'] = [p[1]]
    elif(len(p) == 4):
        p[0]['lhs'] = p[1]
        p[0]['rhs'] = p[3]['exp']
        p[0]['exp'] = [p[1]] + [p[2]] + p[3]['exp']
    #ADD    

def p_type_qualifier(p):
    '''
    type_qualifier : CONST
    | VOLATILE
    '''
    p[0] = {}
    p[0]['line'] = p.lineno(1)
    p[0]['exp'] = [p[1]]
    #print("p_type_qualifier:",p[0])
    #ADD

def p_declarator(p):
    '''
    declarator : pointer direct_declarator 
    | direct_declarator
    '''
    POINTER = 0
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p)==3):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp']+p[2]['exp']
        p[0]['name'] = p[2]['name']
        p[0]['pointer'] = True
        POINTER = 1
    else:
        print("ERROR in p_declarator: len of p neither 1 nor 3")
    NAME = p[0]['name']
    LINE = p[0]['line']
    EXP = p[0]['exp']
    #print("p_declarator:", p[0])
    #ADD
    
def p_direct_declarator(p):
    '''
    direct_declarator : variable_declaration
    | function_declaration
    '''
    p[0] = p[1] 
    #print("p_direct_declarator:", p[0])
    
def  p_variable_declaration(p):
    '''
    variable_declaration : variable_declaration1
    | variable_declaration2
    '''    
    p[0] = p[1]
    NAME = p[0]['name']
    LINE = p[0]['line']
    EXP = p[0]['exp']
    ARRAY_SIZE = 0
    if('arr_size' in p[0]):
        ARRAY_SIZE = p[0]
    #print("variable_declaration:", p[0])
    #ADD
    
def p_variable_declaration1(p):
    '''
    variable_declaration1 : IDENTIFIER
    | IDENTIFIER L_SQUARE constant_expression R_SQUARE
    | IDENTIFIER L_SQUARE R_SQUARE
    '''
    NAME = p[1]
    LINE = p.lineno(1)
    p[0] = {}
    p[0]['name'] = NAME
    p[0]['line'] = LINE
    if(len(p)==2):
        p[0]['exp'] = [ p[1] ]
    elif(len(p)==5):
        p[0]['exp'] = [ p[1] ] + [ p[2] ] + p[3]['exp'] + [ p[4] ]
        #print("const_expression:", p[3]['exp'])
        if(p[3]['exp'][0].isdigit()):
            p[0]['arr_size'] = int(p[3]['exp'][0])
        else:
            p[0]['arr_size'] = p[3]['exp'][0]
    elif(len(p)==4):
        p[0]['exp'] = [ p[1] ] + [ p[2] ] + [ p[3] ]
        p[0]['arr_size'] = 'unspecified'
    else:
        print("ERROR in p_variable_declaration1")
    #print("variable_declaration1:", p[0])
    #2nd & 3rd rules - arrays, 4th rule - function pointers
    #ADD   
    
def p_variable_declaration2(p):
   '''
   variable_declaration2 : L_PAREN declarator R_PAREN
   '''
   p[0] = {}
   p[0]['line'] = p.lineno(1)
   p[0]['name'] = p[2]['name']
   p[0]['exp'] = [ p[1] ] + p[2]['exp'] + [ p[3] ]
   #print("p_variable_declaration2: ", p[0])
   #ADD
       
def p_function_declaration(p):
    '''
    function_declaration : IDENTIFIER L_PAREN parameter_type_list R_PAREN
    | IDENTIFIER L_PAREN identifier_list R_PAREN
    | IDENTIFIER L_PAREN R_PAREN   
    ''' 
    #2nd rule - paramter names without types are allowed
    NAME = p[1]
    LINE = p.lineno(1)
    p[0] = {}
    p[0]['name'] = NAME
    p[0]['line'] = LINE
    FUNC_PARAMS = {}
    ORDERED_NAMES = []
    if(len(p) == 4):
        p[0]['exp'] = [p[1]] + [p[2]] + [p[3]]
    elif(len(p) == 5):
        p[0]['exp'] = [p[1]] + [p[2]] + p[3]['exp'] + [p[4]]
        if('parameters' in p[3]):
            FUNC_PARAMS = p[3]['parameters']
            p[0]['parameters'] = FUNC_PARAMS
        if('ordered_names' in p[3]):
            ORDERED_NAMES = p[3]['ordered_names']
            p[0]['ordered_names'] = ORDERED_NAMES
    #ADD   

def p_pointer(p):
    '''
    pointer : STAR
    | STAR type_qualifier_list
    | STAR pointer
    | STAR type_qualifier_list pointer
    '''
    LINE = p.lineno(1)
    p[0] = {}
    p[0]['line'] = LINE
    if(len(p)==2):
        p[0]['exp'] = [ p[1] ]
    elif(len(p)==3):  #NOT HANDLED  
        p[0]['exp'] = [ p[1] ] + p[2]['exp'] 
    elif(len(p)==4): #NOT HANDLED 
        p[0]['exp'] = [ p[1] ] + p[2]['exp'] + p[3]['exp']
    else:
        print("ERROR in p_pointer:")
    #print("p_pointer:", p[0])

def p_type_qualifier_list(p):
    '''
    type_qualifier_list : type_qualifier
    | type_qualifier_list type_qualifier
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 3):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp'] + p[2]['exp']
    #print("p_type_qualifier_list:", p[0])
    pass

def p_parameter_type_list(p):
    '''
    parameter_type_list : parameter_list
    | parameter_list COMMA ELLIPSIS
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp'] + [p[2]] + [p[3]]
        p[0]['parameters'] = p[1]['parameters']
        p[0]['ordered_names'] = p[1]['ordered_names']
    #ADD

def p_parameter_list(p):
    '''
    parameter_list : parameter_declaration
    | parameter_list COMMA parameter_declaration
    '''
    if(len(p) == 2):
        p[0] = p[1]
        if('name' in p[1]):
            p[0]['parameters'] = {tuple(p[0]['name']):p[0]['type']} #type casting list to tuple as lists can not be used as dict key
            p[0]['ordered_names'] = [p[1]['name']]
        else:
            p[0]['parameters'] = {}
            p[0]['ordered_names'] = []
    elif(len(p) == 4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp'] + [p[2]] + p[3]['exp']
        p[0]['parameters'] = p[1]['parameters']
        p[0]['ordered_names'] = p[1]['ordered_names']
        if('name' in p[3]):
            p[0]['parameters'][tuple(p[3]['name'])] = p[3]['type']
            p[0]['ordered_names'] = p[1]['ordered_names']+[p[3]['name']]
            
    #print("p_parameter_list:", p[0])
    FUNC_PARAMS = p[0]['parameters']
    ORDERED_NAMES = p[0]['ordered_names']
    #print("parameters:", p[0]['parameters'])
    #ADD

def p_parameter_declaration(p):
    '''
    parameter_declaration : declaration_specifiers declarator
    | declaration_specifiers abstract_declarator
    | declaration_specifiers
    '''
    NAME = []
    if(len(p) == 2):
        p[0] = p[1]
        p[0]['type'] = p[1]['exp']
    elif(len(p) == 3):
        p[0] = {}
        p[0]['line'] = p.lineno(1)
        p[0]['exp'] = p[1]['exp'] + p[2]['exp']
        p[0]['type'] = p[1]['exp']
        p[0]['name'] = p[2]['exp']
        NAME = p[2]['exp']
    EXP = p[0]['exp']
    LINE = p[0]['line']
    TYPE = p[0]['type']
    #print("p_parameter_declaration:", p[0])
    #ADD

def p_identifier_list(p):
    '''
    identifier_list : IDENTIFIER
    | identifier_list COMMA IDENTIFIER
    '''
    if(len(p) == 2):
        p[0] = [p[1]]
        NAME = p[1]
    elif(len(p) == 4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp'] + [p[2]] + [p[3]]
        p[0]['name'] = p[3]
        NAME = p[3]
    #print("p_identifier_list:", p[0])
    #ADD

def p_type_name(p):
    '''
    type_name : specifier_qualifier_list
    | specifier_qualifier_list abstract_declarator
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 3):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp'] + p[2]['exp']
    #print("p_type_name:", p[0])
    #ADD

def p_abstract_declarator(p):
    '''
    abstract_declarator : pointer
    | direct_abstract_declarator
    | pointer direct_abstract_declarator
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 3):
        p[0] = {}
        p[0]['line'] = p.lineno(1)
        p[0]['exp'] = p[1]['exp'] + p[2]['exp']
    #print("p_abstract_declarator:", p[0])
    #ADD

def p_direct_abstract_declarator(p):
    '''
    direct_abstract_declarator : L_SQUARE R_SQUARE
    | L_PAREN R_PAREN
    | L_SQUARE constant_expression R_SQUARE
    | L_PAREN abstract_declarator R_PAREN
    | L_PAREN parameter_type_list R_PAREN
    | direct_abstract_declarator L_PAREN R_PAREN
    | direct_abstract_declarator L_SQUARE R_SQUARE
    | direct_abstract_declarator L_SQUARE constant_expression R_SQUARE
    | direct_abstract_declarator L_PAREN parameter_type_list R_PAREN
    '''
    p[0] = {}
    p[0]['line'] = p.lineno(1)
    if(len(p) == 3):
        p[0]['exp'] = [p[1]] + [p[2]]
    elif(len(p) == 4 and ( p[1] == '[' or p[1] == '(')):
        p[0]['exp'] = [p[1]] + p[2]['exp'] + [p[3]]
    elif(len(p) == 4 and ( p[1] == '[' or p[1] == '(')):
        p[0]['exp'] = p[1]['exp'] + [p[2]] + [p[3]]
    elif(len(p) == 5):
        p[0]['exp'] = p[1]['exp'] + [p[2]] + p[3]['exp'] + [p[4]]
    #print("p_direct_abstract_declarator:", p[0])
    pass

def p_initializer(p):
    '''
    initializer : assignment_expression
    | L_BRACE initializer_list R_BRACE
    | L_BRACE initializer_list COMMA R_BRACE
    '''
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p) == 4):
        p[0] = {}
        p[0]['line'] = p.lineno(1)
        p[0]['exp'] = [p[1]] + p[2]['exp'] + [p[3]]
    elif(len(p) == 5):
        p[0] = {}
        p[0]['line'] = p.lineno(1)
        p[0]['exp'] = [p[1]] + p[2]['exp'] + [p[3]] + [p[4]]
    #print("p_initializer:", p[0])
    pass

def p_initializer_list(p):
    '''
    initializer_list : initializer
    | initializer_list COMMA initializer
    '''
    if(len(p)==2):
        p[0] = p[1]
    elif(len(p) == 4):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp'] + [p[2]] + p[3]['exp']
    #print("p_initializer_list:", p[0])
    pass

def p_statement(p):
    '''
    statement : labeled_statement
    | compound_statement
    | expression_statement
    | selection_statement
    | iteration_statement
    | jump_statement
    '''
    p[0] = p[1]
    EXP = p[0]['exp']
    LINE = p[0]['line']
    #print("p_statement:", p[0])
    #ADD

def p_labeled_statement(p):
    '''
    labeled_statement : IDENTIFIER COLON statement
    | CASE constant_expression COLON statement
    | DEFAULT COLON statement
    '''
    p[0] = {}
    p[0]['line'] = p.lineno(1)
    if(len(p) == 4):
        p[0]['exp'] = [p[1]] + [p[2]] + p[3]['exp']
    elif(len(p) == 5):
        p[0]['exp'] = [p[1]] + p[2]['exp'] + [p[3]] + p[4]['exp']
    #print("p_labeled_statement:", p[0])
    #ADD

#C 89 allows variable declarations at the beginning of the block only. 
def p_compound_statement(p):
    '''
    compound_statement : compound_statement_begin R_BRACE
    | compound_statement_begin statement_list R_BRACE
    | compound_statement_begin declaration_list R_BRACE
    | compound_statement_begin declaration_list statement_list R_BRACE
    '''
    p[0] = {}
    p[0]['line'] = p[1]['line']
    if(len(p) == 3):
        p[0]['exp'] = p[1]['exp'] + [p[2]]
    elif(len(p) == 4):
        p[0]['exp'] = p[1]['exp'] + p[2]['exp'] + [p[3]]
    elif(len(p) == 5):
        p[0]['exp'] = p[1]['exp'] + p[2]['exp'] + p[3]['exp'] + [p[4]]
    #print("p_compound_statement:", p[0])
    LINE = p[0]['line']
    EXP = p[0]['exp']
    #ADD
    
    
def p_compound_statement_begin(p):
    '''
    compound_statement_begin : L_BRACE
    '''
    p[0] = {}
    p[0]['exp'] = ['{']
    p[0]['line'] = p.lineno(1)
    #ADD

def p_declaration_list(p):
    '''
    declaration_list : declaration
    | declaration_list declaration
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 3):
        #p[0] = {}
        #p[0]['line'] = p[1]['line']
        p[0] = p[1]
        p[0]['exp'] = p[1]['exp'] + p[2]['exp']
    #print("p_declaration_list:", p[0])
    NAME = p[0]['name']
    LINE = p[0]['line']
    EXP = p[0]['exp']
    #ADD

def p_statement_list(p):
    '''
    statement_list : statement
    | statement_list statement
    '''
    if(len(p) == 2):
        p[0] = p[1]
    elif(len(p) == 3):
        p[0] = {}
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp'] + p[2]['exp']
    #print("p_statement_list:", p[0])
    pass

def p_expression_statement(p):
    '''
    expression_statement : SEMI
    | expression SEMI
    '''
    p[0] = {}
    if(len(p)==2):
        p[0]['line'] = p.lineno(1)
        p[0]['exp'] = [ p[1] ]
    elif(len(p)==3):
        p[0]['line'] = p[1]['line']
        p[0]['exp'] = p[1]['exp'] + [ p[2] ]
    else:
        print("ERROR in p_expression_statement")
    EXPR = p[0]['exp']
    LINE = p[0]['line']
    #print("p_expression_statement:", p[0])
    #ADD

def p_selection_statement(p):
    '''
    selection_statement : IF L_PAREN expression R_PAREN statement
    | IF L_PAREN expression R_PAREN statement ELSE statement
    | SWITCH L_PAREN expression R_PAREN statement
    '''
    p[0] = {}
    p[0]['line'] = p.lineno(1)
    LINE=p[0]['line']
    BLOCK=[]
    CONDITION = []
    HAS_ELSE_CLAUSE = False
    if(len(p) == 6):
        CONDITION = p[3]['exp']
        BLOCK.append(p[5]['exp'])
        p[0]['exp'] = [p[1]] + [p[2]] + p[3]['exp'] + [p[4]] + p[5]['exp']
    elif(len(p) == 8):
        CONDITION = p[3]['exp']
        BLOCK.append(p[5]['exp'])
        BLOCK.append(p[7]['exp'])
        p[0]['exp'] = [p[1]] + [p[2]] + p[3]['exp'] + [p[4]] + p[5]['exp'] + [p[6]] + p[7]['exp']
        HAS_ELSE_CLAUSE = True
    EXP=p[0]['exp']
    #print("p_selection_statement:", p[0])
    #ADD

def p_iteration_statement(p):
    '''iteration_statement : iteration_header iteration_body '''
    p[0] = {}
    p[0]['line'] = p.lineno(1)
    p[0]['exp'] = p[1]['exp'] + p[2]['exp']
    EXP = p[0]['exp']
    #ADD

def p_iteration_header(p):
    '''
    iteration_header : WHILE L_PAREN expression R_PAREN 
    | FOR L_PAREN expression_statement expression_statement R_PAREN 
    | FOR L_PAREN expression_statement expression_statement expression R_PAREN 
    '''
    LINE = p.lineno(1)
    p[0] = {}
    p[0]['line'] = LINE
    if(len(p) == 5):
        CONDITION=p[3]['exp']
        p[0]['type']='while'
        p[0]['exp'] = [p[1]] + [p[2]] + p[3]['exp'] + [p[4]]
    elif(len(p) == 6):
        CONDITION=p[4]['exp']
        p[0]['type']='for'
        p[0]['exp'] = [p[1]] + [p[2]] + p[3]['exp'] + p[4]['exp'] + [p[5]]
    elif(len(p) == 7):
        CONDITION=p[4]['exp']
        p[0]['type']='for'
        p[0]['exp'] = [p[1]] + [p[2]] + p[3]['exp'] + p[4]['exp'] + p[5]['exp'] + [p[6]]
    EXP = p[0]['exp']
    #print("iteration header", EXP)
    #do while not supported
    #ADD

def p_iteration_body(p):
    '''iteration_body : statement '''
    LINE = p[1]['line']
    p[0] = p[1]
    EXP = p[0]['exp']
    BLOCK = p[1]['exp']
    #ADD

def p_jump_statement(p):
    '''
    jump_statement : GOTO IDENTIFIER SEMI
    | CONTINUE SEMI
    | BREAK SEMI
    | RETURN SEMI
    | RETURN expression SEMI
    '''
    p[0] = {}
    NAME = p[1]
    LINE = p.lineno(1)
    p[0]['line'] = LINE
    #if(p[1] == 'return' and p[3] == ';'):
    if(p[1]=='return' and len(p)==4):
        p[0]['exp'] = [p[1]] + p[2]['exp'] + [p[3]]
    elif(len(p) == 3):
        p[0]['exp'] = [p[1]] + [p[2]]
    elif(len(p) == 4):
        p[0]['exp'] = [p[1]] + [p[2]] + [p[3]]
    EXP = p[0]['exp']
    #ADD

def p_translation_unit(p):
    '''
    translation_unit : external_declaration
    |  external_declaration translation_unit
    '''
    AT_PROG_END = False #works because above production is right-recursive
    if(len(p) == 2):
        p[0] = p[1]
        AT_PROG_END = True
    elif(len(p) == 3):
        p[0] = {}
        p[0]['line'] = p.lineno(1)
        #print(p[1], p[2])
        p[0]['exp'] = p[1]['exp'] + p[2]['exp']
    LINE = p[0]['line']
    #print("Translation Unit:",p[0])
    #ADD

def p_external_declaration(p):
    '''
    external_declaration : function_definition
    | other_declarations
    '''
    p[0] = p[1]
    #print("External declaration:",p[0])
    #ADD
    
def p_other_declarations(p):
    '''
    other_declarations : declaration
    '''
    #Function prototypes and global variables
    p[0] = p[1]
    #print("Other declaration:",p[0])
    #ADD

def p_function_header(p):
    '''
    function_header : fheader_type1
    | fheader_type2
    | fheader_type3
    '''
    NAME = p[1]['name']
    LINE = p[1]['line']
    p[0] = p[1]
    EXP = p[0]['exp']
    #print("Function header:",p[0])
    #ADD
    
def p_fheader_type1(p):
    '''
    fheader_type1 : declaration_specifiers function_declaration
    '''
    p[0] = {}
    LINE = p[2]['line']
    NAME = p[2]['name']
    p[0]['line'] = LINE
    p[0]['exp'] = p[1]['exp'] + p[2]['exp']
    p[0]['name'] = NAME
    #print("p_fheader_type1:",p[0])
    #ADD

def p_fheader_type2(p):   
    '''
    fheader_type2 : function_declaration
    '''
    NAME = p[1]['name']
    LINE = p[1]['line']
    p[0] = p[1]
    #print("p_fheader_type2:",p[0])
    #ADD    
    
def p_fheader_type3(p):
    '''
    fheader_type3 : declaration_specifiers pointer function_declaration
    '''
    NAME = p[3]['name']
    LINE = p[3]['line']
    p[0] = {}
    p[0]['line'] = LINE
    p[0]['name'] = NAME
    p[0]['exp'] = p[1]['exp'] + p[2]['exp'] + p[3]['exp']
       
def p_function_definition(p):
    '''
    function_definition : function_header compound_statement
    | function_header declaration_list compound_statement
    '''
    NAME = p[1]['name']
    LINE = p[1]['line']
    p[0] = {}
    p[0]['line'] = LINE
    if(len(p) == 3):
        FUNC_BODY=p[2]['exp']
        p[0]['exp'] = p[1]['exp'] + p[2]['exp']
    elif(len(p) == 4):
        FUNC_BODY=p[3]['exp']
        p[0]['exp'] = p[1]['exp'] + p[2]['exp'] + p[3]['exp']
    EXP=p[0]['exp']
    #print("p_function_definition:",p[0])
    #print("p_function_BODY:",FUNC_BODY)

    #ADD      
    
def p_error(p):
    if p:
        print("Syntax error at token", p)
    else:
        print("Syntax error at EOF")
        

parser = yacc.yacc()

input_prog = []
while(True):
    try:
        next_line = input()
    except EOFError:
        #print("Going to Parse Input now!")
        break
    else:
        input_prog.append(next_line)
    
input_prog_str = "\n".join(input_prog) 
result = parser.parse(input_prog_str)
#def after_parse_main():
#ADD
