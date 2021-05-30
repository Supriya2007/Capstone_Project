import ply.yacc as yacc
from C_Lex import tokens
#import C_Lex

start = 'translation_unit' #Sets the Start Symbol

#def before_parse_main():
#ADD

def p_primary_expression(p):
    '''
    primary_expression : variable_use
    | CONSTANT
    | STRING_LITERAL
    | L_PAREN expression R_PAREN
    '''
    pass

def p_variable_use(p):
    '''
    variable_use : IDENTIFIER
    '''
    NAME = p[1]
    LINE = p.lineno(1)
    #ADD

#def p_postfix_expression(p):
#    '''
#    postfix_expression : primary_expression
#    | postfix_expression L_SQUARE expression R_SQUARE
#    | postfix_expression L_PAREN R_PAREN
#    | postfix_expression L_PAREN argument_expression_list R_PAREN
#    | postfix_expression DOT IDENTIFIER
#    | postfix_expression PTR_OP IDENTIFIER
#    | postfix_expression INC_OP
#    | postfix_expression DEC_OP
#    '''
#    pass

#def p_function_call(p):
#    '''
#    function_call : postfix_expression L_PAREN R_PAREN
#    | postfix_expression L_PAREN argument_expression_list R_PAREN
#    '''
#    #ADD
    
def p_function_call(p):
    '''
    function_call : IDENTIFIER L_PAREN R_PAREN
    | IDENTIFIER L_PAREN argument_expression_list R_PAREN
    '''
    NAME = p[1]
    LINE = p.lineno(1)
    if (NAME == "rewind") :
        print(LINE)
        print(' Use fseek instead of rewind')
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
    #ADD
    pass

def p_argument_expression_list(p):
    '''
    argument_expression_list : assignment_expression
    | argument_expression_list COMMA assignment_expression
    '''
    pass
    
def p_unary_expression(p):
    '''
    unary_expression : postfix_expression
    | INC_OP unary_expression
    | DEC_OP unary_expression
    | unary_operator cast_expression
    | SIZEOF unary_expression
    | SIZEOF L_PAREN type_name R_PAREN
    '''
    NAME = p[1]
    #ADD
    pass

def p_unary_operator(p):
    '''
    unary_operator : AMP
    | STAR
    | PLUS
    | MINUS
    | TILDA
    | EXCLAIM
    '''
    pass

def p_cast_expression(p):
    '''
    cast_expression : unary_expression
    | L_PAREN type_name R_PAREN cast_expression
    '''
    pass

def p_multiplicative_expression(p):
    '''
    multiplicative_expression : cast_expression
    | multiplicative_expression STAR cast_expression
    | multiplicative_expression SLASH cast_expression
    | multiplicative_expression PERCENT cast_expression
    '''
    pass

def p_additive_expression(p):
    '''
    additive_expression : multiplicative_expression
    | additive_expression PLUS multiplicative_expression
    | additive_expression MINUS multiplicative_expression
    '''
    pass

def p_shift_expression(p):
    '''
    shift_expression : additive_expression
    | shift_expression LEFT_OP additive_expression
    | shift_expression RIGHT_OP additive_expression
    '''
    pass

def p_relational_expression(p):
    '''
    relational_expression : shift_expression
    | relational_expression LESS shift_expression
    | relational_expression GREATER shift_expression
    | relational_expression LE_OP shift_expression
    | relational_expression GE_OP shift_expression
    '''
    pass

def p_equality_expression(p):
    '''
    equality_expression : relational_expression
    | equality_exp_lhs EQ_OP relational_expression
    | equality_exp_lhs NE_OP relational_expression
    '''
    #ADD   

def p_equality_exp_lhs(p):
    '''
    equality_exp_lhs : equality_expression
    '''
    #ADD

def p_and_expression(p):
    '''
    and_expression : equality_expression
    | and_expression AMP equality_expression
    '''
    pass

def p_exclusive_or_expression(p):
    '''
    exclusive_or_expression : and_expression
    | exclusive_or_expression CARET and_expression
    '''
    pass

def p_inclusive_or_expression(p):
    '''
    inclusive_or_expression : exclusive_or_expression
    | inclusive_or_expression PIPE exclusive_or_expression
    '''
    pass

def p_logical_and_expression(p):
    '''
    logical_and_expression : inclusive_or_expression
    | logical_and_expression AND_OP inclusive_or_expression
    '''
    pass

def p_logical_or_expression(p):
    '''
    logical_or_expression : logical_and_expression
    | logical_or_expression OR_OP logical_and_expression
    '''
    pass

def p_conditional_expression(p):
    '''
    conditional_expression : logical_or_expression
    | logical_or_expression QUEST expression COLON conditional_expression
    '''
    pass

def p_assignment_expression(p):
    '''
    assignment_expression : conditional_expression
    | assignment_lhs assignment_operator assignment_expression
    '''
    #ADD
    
def p_assignment_lhs(p):
    '''
    assignment_lhs : unary_expression
    ''' 
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
    pass

def p_expression(p):
    '''
    expression : assignment_expression
    | expression COMMA assignment_expression
    '''
    pass

def p_constant_expression(p):
    '''
    constant_expression : conditional_expression
    '''
    pass

def p_declaration(p):
    '''
    declaration : declaration_specifiers SEMI
    | declaration_specifiers init_declarator_list SEMI
    '''
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
    pass

def p_init_declarator_list(p):
    '''
    init_declarator_list : init_declarator
    | init_declarator_list COMMA init_declarator
    '''
    pass
    
def p_init_declarator(p):
    '''
    init_declarator : declarator
    | declarator EQUAL initializer
    '''
    #p[0] = p[1]
    pass

def p_storage_class_specifier(p):
    '''
    storage_class_specifier : TYPEDEF
    | EXTERN
    | STATIC
    | AUTO
    | REGISTER
    '''
    pass

def p_type_specifier(p):
    '''
    type_specifier : VOID
    | CHAR
    | SHORT
    | INT
    | LONG
    | FLOAT
    | DOUBLE
    | SIGNED
    | UNSIGNED
    | struct_or_union_specifier
    | enum_specifier
    | TYPE_NAME
    '''
    pass

def p_struct_or_union_specifier(p):
    '''
    struct_or_union_specifier : struct_or_union IDENTIFIER L_BRACE struct_declaration_list R_BRACE
    | struct_or_union L_BRACE struct_declaration_list R_BRACE
    | struct_or_union IDENTIFIER
    '''
    pass

def p_struct_or_union(p):
    '''
    struct_or_union : STRUCT
    | UNION
    '''
    pass

def p_struct_declaration_list(p):
    '''
    struct_declaration_list : struct_declaration
    | struct_declaration_list struct_declaration
    '''
    pass

def p_struct_declaration(p):
    '''
    struct_declaration : specifier_qualifier_list struct_declarator_list SEMI
    '''
    pass

def p_specifier_qualifier_list(p):
    '''
    specifier_qualifier_list : type_specifier specifier_qualifier_list
    | type_specifier
    | type_qualifier specifier_qualifier_list
    | type_qualifier
    '''
    pass

def p_struct_declarator_list(p):
    '''
    struct_declarator_list : struct_declarator
    | struct_declarator_list COMMA struct_declarator
    '''
    pass

def p_struct_declarator(p):
    '''
    struct_declarator : declarator
    | COLON constant_expression
    | declarator COLON constant_expression
    '''
    pass
    
def p_enum_specifier(p):
    '''
    enum_specifier : ENUM L_BRACE enumerator_list R_BRACE
    | ENUM IDENTIFIER L_BRACE enumerator_list R_BRACE
    | ENUM IDENTIFIER
    '''
    pass


def p_enumerator_list(p):
    '''
    enumerator_list : enumerator
    | enumerator_list COMMA enumerator
    '''
    pass

def p_enumerator(p):
    '''
    enumerator : IDENTIFIER
    | IDENTIFIER EQUAL constant_expression
    '''
    pass    

def p_type_qualifier(p):
    '''
    type_qualifier : CONST
    | VOLATILE
    '''
    pass

def p_declarator(p):
    '''
    declarator : pointer direct_declarator
    | direct_declarator
    '''
    pass
    
#def p_direct_declarator(p):
#    '''
#    direct_declarator : IDENTIFIER
#    | L_PAREN declarator R_PAREN
#    | direct_declarator L_SQUARE constant_expression R_SQUARE
#    | direct_declarator L_SQUARE R_SQUARE
#    | direct_declarator L_PAREN parameter_type_list R_PAREN
#    | direct_declarator L_PAREN identifier_list R_PAREN
#    | direct_declarator L_PAREN R_PAREN
#    '''
#    pass    

#def p_direct_declarator(p):
#    '''
#    direct_declarator : IDENTIFIER
#    | L_PAREN declarator R_PAREN
#    | direct_declarator L_SQUARE constant_expression R_SQUARE
#    | direct_declarator L_SQUARE R_SQUARE
#    | function_prototype
#    '''
#    pass
    
def p_direct_declarator(p):
    '''
    direct_declarator : variable_declaration
    | function_declaration
    '''
    #p[0] = p[1] 
    
#def p_variable_declaration(p):
#    '''
#    variable_declaration : IDENTIFIER
#    | direct_declarator L_SQUARE constant_expression R_SQUARE
#    | direct_declarator L_SQUARE R_SQUARE
#    | L_PAREN declarator R_PAREN
#    '''
    #2nd & 3rd rules - arrays, 4th rule - function pointers
    #ADD  
 
   
#def p_variable_declaration(p):
#    '''
#    variable_declaration : IDENTIFIER
#    | IDENTIFIER L_SQUARE constant_expression R_SQUARE
#    | IDENTIFIER L_SQUARE R_SQUARE
#    | L_PAREN declarator R_PAREN
#    '''
    #2nd & 3rd rules - arrays, 4th rule - function pointers
    #ADD  
    
def  p_variable_declaration(p):
    '''
    variable_declaration : variable_declaration1
    | variable_declaration2
    '''    
    #p[0] = p[1]
    
def p_variable_declaration1(p):
    '''
    variable_declaration1 : IDENTIFIER
    | IDENTIFIER L_SQUARE constant_expression R_SQUARE
    | IDENTIFIER L_SQUARE R_SQUARE
    '''
    NAME = p[1]
    LINE = p.lineno(1)
    #p[0] = (NAME, LINE)
    #2nd & 3rd rules - arrays, 4th rule - function pointers
    #ADD   
    
def p_variable_declaration2(p):
   '''
   variable_declaration2 : L_PAREN declarator R_PAREN
   '''
   #ADD
    
#def p_function_prototype(p):
#    '''
#    function_prototype : direct_declarator L_PAREN parameter_type_list R_PAREN
#    | direct_declarator L_PAREN identifier_list R_PAREN
#    | direct_declarator L_PAREN R_PAREN   
#    ''' 
    #2nd rule - paramter names without types are allowed
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
    p[0] = (NAME, LINE)
    #ADD   

def p_pointer(p):
    '''
    pointer : STAR
    | STAR type_qualifier_list
    | STAR pointer
    | STAR type_qualifier_list pointer
    '''
    pass

def p_type_qualifier_list(p):
    '''
    type_qualifier_list : type_qualifier
    | type_qualifier_list type_qualifier
    '''
    pass

def p_parameter_type_list(p):
    '''
    parameter_type_list : parameter_list
    | parameter_list COMMA ELLIPSIS
    '''
    #ADD

def p_parameter_list(p):
    '''
    parameter_list : parameter_declaration
    | parameter_list COMMA parameter_declaration
    '''
    pass

def p_parameter_declaration(p):
    '''
    parameter_declaration : declaration_specifiers declarator
    | declaration_specifiers abstract_declarator
    | declaration_specifiers
    '''
    #ADD
    pass

def p_identifier_list(p):
    '''
    identifier_list : IDENTIFIER
    | identifier_list COMMA IDENTIFIER
    '''
    pass

def p_type_name(p):
    '''
    type_name : specifier_qualifier_list
    | specifier_qualifier_list abstract_declarator
    '''
    pass

def p_abstract_declarator(p):
    '''
    abstract_declarator : pointer
    | direct_abstract_declarator
    | pointer direct_abstract_declarator
    '''
    pass

def p_direct_abstract_declarator(p):
    '''
    direct_abstract_declarator : L_PAREN abstract_declarator R_PAREN
    | L_SQUARE R_SQUARE
    | L_SQUARE constant_expression R_SQUARE
    | direct_abstract_declarator L_SQUARE R_SQUARE
    | direct_abstract_declarator L_SQUARE constant_expression R_SQUARE
    | L_PAREN R_PAREN
    | L_PAREN parameter_type_list R_PAREN
    | direct_abstract_declarator L_PAREN R_PAREN
    | direct_abstract_declarator L_PAREN parameter_type_list R_PAREN
    '''
    pass

def p_initializer(p):
    '''
    initializer : assignment_expression
    | L_BRACE initializer_list R_BRACE
    | L_BRACE initializer_list COMMA R_BRACE
    '''
    pass

def p_initializer_list(p):
    '''
    initializer_list : initializer
    | initializer_list COMMA initializer
    '''
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
    #ADD

def p_labeled_statement(p):
    '''
    labeled_statement : IDENTIFIER COLON statement
    | CASE constant_expression COLON statement
    | DEFAULT COLON statement
    '''
    pass

   
#C 89 allows variable declarations at the beginning of the block only. 
def p_compound_statement(p):
    '''
    compound_statement : L_BRACE R_BRACE
    | L_BRACE statement_list R_BRACE
    | L_BRACE declaration_list R_BRACE
    | L_BRACE declaration_list statement_list R_BRACE
    '''
    pass


#def p_compound_statement(p):
#    '''
#    compound_statement : L_BRACE R_BRACE
#    | L_BRACE dec_or_stmt_list R_BRACE
#    '''
#    pass
    
#def p_dec_or_stmt_list(p):
#    '''
#    dec_or_stmt_list : declaration_list
#    | statement_list
#    | declaration_list dec_or_stmt_list
#    | statement_list dec_or_stmt_list
#    '''
#    '''
#    dec_or_stmt_list : declaration_list dec_or_stmt_list
#    | statement_list dec_or_stmt_list
#    | empty
#    '''
#    pass

def p_declaration_list(p):
    '''
    declaration_list : declaration
    | declaration_list declaration
    '''
    pass

def p_statement_list(p):
    '''
    statement_list : statement
    | statement_list statement
    '''
    pass

def p_expression_statement(p):
    '''
    expression_statement : SEMI
    | expression SEMI
    '''
    pass

def p_selection_statement(p):
    '''
    selection_statement : IF L_PAREN expression R_PAREN statement
    | IF L_PAREN expression R_PAREN statement ELSE statement
    | SWITCH L_PAREN expression R_PAREN statement
    '''
    pass

def p_iteration_statement(p):
    '''iteration_statement : iteration_header iteration_body '''

def p_iteration_header(p):
    '''
    iteration_header : WHILE L_PAREN expression R_PAREN 
    | FOR L_PAREN expression_statement expression_statement R_PAREN 
    | FOR L_PAREN expression_statement expression_statement expression R_PAREN 
    '''
    LINE = p.lineno(1)
    #do while not supported
    #ADD
    pass


def p_iteration_body(p):
    '''iteration_body : statement '''
    LINE = p.lineno(1)
    #ADD





def p_jump_statement(p):
    '''
    jump_statement : GOTO IDENTIFIER SEMI
    | CONTINUE SEMI
    | BREAK SEMI
    | RETURN SEMI
    | RETURN expression SEMI
    '''
    pass

def p_translation_unit(p):
    '''
    translation_unit : external_declaration
    | translation_unit external_declaration
    '''
    pass

#def p_external_declaration(p):
#    '''
#    external_declaration : function_definition
#    | declaration
#    '''
#    pass

def p_external_declaration(p):
    '''
    external_declaration : function_definition
    | other_declarations
    '''
    pass
    
def p_other_declarations(p):
    '''
    other_declarations : declaration
    '''
    #Function prototypes and global variables
    #ADD

#def p_function_definition(p):
#    '''
#    function_definition : declaration_specifiers declarator declaration_list compound_statement
#    | declaration_specifiers declarator compound_statement
#    | declarator declaration_list compound_statement
#    | declarator compound_statement
#    '''
#    pass

#def p_function_header(p):
#    '''
#    function_header : declaration_specifiers declarator declaration_list
#    | declaration_specifiers declarator
#    | declarator declaration_list 
#    | declarator
#    '''
#    pass
    
#def p_function_definition(p):
#    '''
#    function_definition : function_header compound_statement
#    '''
#    #ADD
    
#def p_function_header(p):
#    '''
#    function_header : declaration_specifiers declarator 
#    | declarator  
#    '''
#    pass

def p_function_header(p):
    '''
    function_header : fheader_type1
    | fheader_type2
    '''
    NAME, LINE = p[1]
    p[0] = (NAME, LINE)
    #ADD
    
def p_fheader_type1(p):
    '''
    fheader_type1 : declaration_specifiers function_declaration
    '''
    NAME, LINE = p[2]
    p[0] = (NAME, LINE)
    #ADD
    
def p_fheader_type2(p):   
    '''
    fheader_type2 : function_declaration
    '''
    NAME, LINE = p[1]
    p[0] = (NAME, LINE)
    #ADD    
    
    
def p_function_definition(p):
    '''
    function_definition : function_header compound_statement
    | function_header declaration_list compound_statement
    '''
    NAME, LINE = p[1]
    #ADD    
    
    
    
#def p_empty(p):
#    'empty : '
#    pass    
    
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
   
