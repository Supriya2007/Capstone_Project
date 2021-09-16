import sys
#Stores mapping between user keywords and the states in the grammar with the line at which a newline can be added to the grammar

#Write prog to get initial line numbers, don't hard-code.
states = {
    'before_parse':['before_parse_main', 7],
    'function_prototype' : ['p_function_declaration', 862],
    #Can not differentiate between function definitions and prototypes as of now
    'function_header' : ['p_function_declaration', 862],
    'function_parameters' : ['p_parameter_type_list', 915],
    'parameter_declaration' : ['p_parameter_declaration', 943],
    'func_statements' : ['p_statement', 1062],
    #'function_end' : ['p_function_definition', 1246],
    'function_end' : ['p_function_definition', 1324],
    'var_declares' : ['p_variable_declaration1', 823],
    'variable_declaration' : ['p_variable_declaration', 808],
    'declarations' : ['p_other_declarations', 1280], 
    #Maps to declarations outside functions = global variables and function prototypes
    'declaration_stmt' : ['p_declaration', 470],
    'declaration_specifiers' : ['p_declaration_specifiers', 495],
    'type_qualifier' : ['p_type_qualifier', 772],
    #If many variables are declared in a single statement, declarations is matched once for each variable, while declaration_stmt is matched only once.
    'function_call' : ['p_function_call', 52],
    'loop_header':['p_iteration_header', 1202],
    'loop_body':['p_iteration_body', 1228],
    'after_parse':['after_parse_main', 1366],
    'switch_stmt': ['p_selection_statement', 1174],
    'if_stmt': ['p_selection_statement', 1174],
    'case_stmt':['p_labeled_statement', 1077],
    'equality_cond' : ['p_equality_expression', 267],
    'equality_cond_lhs' : ['p_equality_exp_lhs', 284],
    'variable_assignments' : ['p_assignment_expression', 392],
    'assignment_lhs' : ['p_assignment_lhs', 417],
    'postfix_expression' : ['p_postfix_expression', 75],
    'unary_expression' : ['p_unary_expression', 125],
    'identifier_list':['p_identifier_list', 958],
    'unintialized_declaration':['p_uninitialized_declaration', 561],
    'initialized_declaration': ['p_initialized_declaration', 540],
    'expressions':['p_expression_statement', 1155],
    'functions_without_type_specifiers':['p_fheader_type2', 1314],
    'exp': ['p_expression', 446],
    'type_specifiers':['p_declaration_specifiers', 492],
    'jump_statement' : ['p_jump_statement',1234],
    'block_end':['p_compound_statement', 1093],
    'block_start':['p_compound_statement_begin', 1114],
    'declarator_name':['p_declarator', 779],
    'translation_unit':['p_translation_unit',1255],
    'pointer':['p_pointer', 885],
    'declarator_and_initializer':['p_init_declarator', 535],
    
}
# #ADD in C_Parser.py marks place to add code

tab = '    ' #tab = 4 spaces
#cur_tab = '' 

def get_next_word():
    global i
    word = words[i]
    i+=1
    return word
    
def write_file_at(at_state, string):
    start_lno = states[at_state][1]
    func_name = states[at_state][0]
    #Checking if def and func name are there in the line. Number of arguments and spaces may vary.
    ind = start_lno-1
    while(not("def" in file_lines[ind] and func_name in file_lines[ind])):
        #print(file_lines[ind])
        ind+=1
    while(file_lines[ind].strip()!='#ADD'):
        ind+=1
    file_lines.insert(ind, string)
    #states[at_state][1]+=1
    
def read_input():
    global i
    try:
        line = input().lstrip()
    except EOFError:
        return ["eof"] #Signal for EOF
    words = line.split()
    i=0
    return words
    
def get_cmd_args_dict():
    vars_values = {}
    print("argv:", sys.argv)
    arg_count = len(sys.argv)-1 #Count other than prog name
    if(arg_count%2):
        print("Invalid Commandline Arguments: Number of args should be even. Format: <name> <var> <name> <var> ... ")
    for i in range(1, arg_count, 2):
        var_name = sys.argv[i]
        value = sys.argv[i+1]
        vars_values[var_name] = value
    return vars_values

var_values = get_cmd_args_dict()
print("var_values:", var_values)

#file_handle = open("C_Parser2.py", "rt")
file_handle = open("C_Parser.py", "rt")
file_lines = file_handle.readlines()
#print(file_lines)
file_handle.close() 

at_state="null"

#cur_tab = ""
while(True):
    words = read_input()
    if(len(words)==0):
        continue

    if(not words):
        continue #Skipping new lines
        
    if(words==["eof"]):
        print("Processing completed")
        break

    cmd = get_next_word()
    if(cmd!="STATE"):
        print("ERROR: Should specify a state")
        break
        
    cur_state = get_next_word()
    #if(cur_state!="main"):
    #    cur_tab = tab
    if(cur_state=="before_parse" or cur_state=="after_parse"):
        cur_tab = ""
    else:
        cur_tab = tab
        
    while(True):
        words = read_input() #input().lstrip()
        #print(words)
        if(len(words)==0):
            continue
        cmd = get_next_word()
        if(cmd=="END_STATE"):
            break
            
        py_cmd = ""
        if(cmd=="CREATE"):
            var_name = get_next_word()
            init_val = get_next_word()
            py_cmd = "%s%s = %s\n"%(cur_tab, var_name, init_val)
        elif(cmd=="APPEND"):
            list_name = get_next_word()
            value = get_next_word()
            py_cmd = "%s%s.append(%s)\n"%(cur_tab, list_name, value)
        elif(cmd == "REMOVE"):
            list_name = get_next_word()
            value = get_next_word()
            py_cmd = "%s%s.remove(%s)\n"%(cur_tab, list_name, value)
        elif(cmd == "POP"):
            list_name = get_next_word()
            index = get_next_word()
            py_cmd = "%s%s.pop(%s)\n"%(cur_tab, list_name, index)
        elif(cmd=="DICT_APPEND"):
            dict_name = get_next_word()
            key = get_next_word()
            value = get_next_word()
            py_cmd = "%s%s[%s] = %s\n"%(cur_tab, dict_name, key, value)
        elif(cmd == "DICT_REMOVE"):
            dict_name = get_next_word()
            key = get_next_word()
            py_cmd = "%s%s.pop(%s)\n"%(cur_tab, dict_name, key)    
        elif(cmd=="IF"):
            var_name = get_next_word()  
            cond = get_next_word() 
            if(cond == "IN"):
                list_name = get_next_word()
                py_cmd = "%sif (%s in %s) :\n"%(cur_tab, var_name, list_name) 
            if(cond == "NOTIN"):
                list_name = get_next_word()
                py_cmd = "%sif (%s not in %s) :\n"%(cur_tab, var_name, list_name) 
            elif(cond == "EQUALTO"):
                list_name = get_next_word()
                py_cmd = "%sif (%s == %s) :\n"%(cur_tab, var_name, list_name) 
            elif(cond == "NOTEQUALTO"):
                list_name = get_next_word()
                py_cmd = "%sif (%s != %s) :\n"%(cur_tab, var_name, list_name)
            elif(cond == "LESS_THAN"):
                var2_name = get_next_word()
                py_cmd = "%sif (%s < %s) :\n"%(cur_tab, var_name, var2_name)
            elif(cond == "GREATER_THAN"):
                var2_name = get_next_word()
                py_cmd = "%sif (%s > %s) :\n"%(cur_tab, var_name, var2_name)  
            elif(cond == "GREATER_EQUAL"):
                var2_name = get_next_word()
                py_cmd = "%sif (%s >= %s) :\n"%(cur_tab, var_name, var2_name)  
            elif(cond == "LESS_EQUAL"):
                var2_name = get_next_word()
                py_cmd = "%sif (%s <= %s) :\n"%(cur_tab, var_name, var2_name)    
            #Add LESS_EQUAL, GREATER_EQUAL later   
                
            cur_tab+=tab  
        elif(cmd=="ELSE"):
            #cur_tab-=tab
            cur_tab = " "*(len(cur_tab)-len(tab))
            py_cmd = "%selse :\n"%(cur_tab)
            cur_tab+=tab
        elif(cmd == "END_IF" or cmd=="END_FOR"):
            cur_tab = " "*(len(cur_tab)-len(tab))
        elif(cmd == "SET"):
            var_name = get_next_word()
            value = get_next_word()
            py_cmd = "%s%s = %s\n"%(cur_tab, var_name, value)   
        elif(cmd == "GLOBAL_SET"):
            list_name = get_next_word()
            value = get_next_word()
            py_cmd = "%sglobal %s;%s = %s\n"%(cur_tab, list_name, list_name, value)
        elif(cmd == "PRINT"):
            list_name = get_next_word()
            py_cmd = "%sprint(%s)\n"%(cur_tab, list_name)
        elif(cmd == "VIOLATION"):
            msg=""
            while(i<len(words)):
                msg = msg + " " + get_next_word()
            py_cmd = "%sprint('%s')\n"%(cur_tab, msg) 
        elif(cmd == "LENGTH"):
            var_name = get_next_word()
            py_cmd = "{tab}{var}_len = len({var})\n".format(tab=cur_tab, var=var_name)
            #print("len cmd:", py_cmd)
        elif(cmd == "USE_GLOBAL"):
            var_name = get_next_word()
            py_cmd = "{tab}global {var}\n".format(tab=cur_tab, var=var_name)
        elif(cmd == "INPUT"):
            var_name = get_next_word()
            init_val = var_values[var_name]
            py_cmd = "%s%s = %s\n"%(cur_tab, var_name, init_val)
        elif(cmd == "INDEX"):
            var_name = get_next_word()
            ind = get_next_word()
            py_cmd = "%s%s_%s = %s[%s]\n"%(cur_tab, var_name, ind, var_name, ind)
        elif(cmd == "FOR"):
            var_name = get_next_word()
            opt = get_next_word()
            print(var_name, opt)
            if(opt == "IN"):
                list_name = get_next_word()
                py_cmd = "%sfor %s in %s:\n"%(cur_tab, var_name, list_name)
                cur_tab+=tab
        elif(cmd == "BREAK"):
            py_cmd = "%sbreak\n"%(cur_tab)
        elif(cmd == "CONTINUE"):
            py_cmd = "%scontinue\n"%(cur_tab)
        write_file_at(cur_state, py_cmd)     
   
file_handle_new = open("C_Parser_new.py", "wt")
file_handle_new.writelines(file_lines)
file_handle_new.close()
