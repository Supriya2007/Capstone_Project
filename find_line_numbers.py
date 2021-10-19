#Stores mapping between user keywords and the states in the grammar with the line at which a newline can be added to the grammar

import re

states = {
    'before_parse':['before_parse_main', 7],
    'function_prototype' : ['p_function_declaration', 911],
    #Can not differentiate between function definitions and prototypes as of now
    'function_header' : ['p_function_declaration', 907],
    'function_parameters' : ['p_parameter_type_list', 907],
    'parameter_declaration' : ['p_parameter_declaration', 1004],
    'func_statements' : ['p_statement', 1131],
    'function_end' : ['p_function_definition', 1402],
    'var_declares' : ['p_variable_declaration1', 867],
    'variable_declaration' : ['p_variable_declaration', 852],
    'declarations' : ['p_other_declarations', 1358], 
    #Maps to declarations outside functions = global variables and function prototypes
    'declaration_stmt' : ['p_declaration', 486],
    #If many variables are declared in a single statement, declarations is matched once for each variable, while declaration_stmt is matched only once.
    'function_call' : ['p_function_call', 52],
    'loop_header':['p_iteration_header', 1276],
    'loop_body':['p_iteration_body', 1302],
    'loop_statement':['p_iteration_statement',1269],
    'after_parse':['after_parse_main', 1444],
    'switch_stmt': ['p_selection_statement', 1243],
    'if_stmt': ['p_selection_statement', 1243],
    'case_stmt':['p_labeled_statement', 1146],
    'equality_cond' : ['p_equality_expression', 279],
    'equality_cond_lhs' : ['p_equality_exp_lhs', 296],
    'variable_assignments' : ['p_assignment_expression', 404],
    'assignment_lhs' : ['p_assignment_lhs', 433],
    'postfix_expression' : ['p_postfix_expression', 78],
    'unary_expression' : ['p_unary_expression', 135],
    'identifier_list':['p_identifier_list', 1027],
    'unintialized_declaration':['p_uninitialized_declaration', 586],
    'initialized_declaration': ['p_initialized_declaration', 563],
    'expressions':['p_expression_statement', 1224],
    'functions_without_type_specifiers':['p_fheader_type2', 1392],
    'exp': ['p_expression', 462],
    'type_specifiers':['p_declaration_specifiers', 511],
    'jump_statement' : ['p_jump_statement',1310],
    'block_end':['p_compound_statement', 1162],
    'block_start':['p_compound_statement_begin', 1183],
    'declarator_name':['p_declarator', 823],
    'translation_unit':['p_translation_unit',1331],
    'structures_and_unions':['p_struct_or_union_specifier',640],
    'struct_declaration_list':['p_struct_declaration_list',686],
    'type_specifier':['p_type_specifier',627],
}

filename = "C_Parser.py"
for state in states:
    with open(filename) as myFile:
        for num, line in enumerate(myFile, 1):
            s = states[state][0]
            m = re.search(r'def(.*)\(p\):', line)
            if m:
                prodn_name = (m.groups()[0]).strip()
                if s == prodn_name:
                    states[state][1] = num
print(states)
