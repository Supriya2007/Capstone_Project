#Creates a dictionary of the form:
#filename:[(lineno, guideline_name, violation_msg)..]

import os
import platform

os_name = platform.system()
if 'Windows' in os_name:
    python="python"
    file_sep = '\\'

if 'Linux' in os_name:
    python="python3"
    file_sep = '/'

#cur_dir = os.getcwd()
#cur_dir = ".."
#print(cur_dir)
parser_creator = "Make_Parser.py"
parser="C_Parser_new.py"
err_msgs_file = "Violations.txt"
formal_struct_dir = "formal_structures"
#NOTE: Space not allowed in 'INPUT:<var_name>'
lib_rules = { 
'Check for global variables' : 'global_fs.txt', 
'Check for variable names less than INPUT:n characters long' : 'input_var_len_fs.txt',
'Check for functions having more than INPUT:max_size lines': 'input_func_size_fs.txt',
'Check for use of rewind() (use fseek instead)' : 'fseek_fs.txt',
'Check for use of strcmp() (use strncmp() instead)' : 'strcmp_fs.txt',
'Check for loops with depth more than INPUT:allowed_depth' : 'depth_of_looping_fs.txt', 
'Use SIZEOF to determine the size of a type in malloc() or calloc()':'sizeof_fs.txt',
'Specify void when function accepts no arguments':'void_fs.txt',
'Check for assignments in looping conditions':'assignment_in_loop_fs.txt',
'Check if strings have been allocated sufficient space':'explicit_size_str_fs.txt',
'Check for variables having length greater than 31':'var_len_less_than_31_fs.txt',
'Check for more than one variable per declaration':'one_variable_per_declaration_fs.txt',
'Do not use implicit typing': 'implicit_type_fs.txt',
'Check for expressions that depend on the order of evaluation of the operands' : 'side_effects_fs.txt',
'Do not use continue': 'no_continue_fs.txt',
'Check for functions with more than INPUT:max_count return statements' : 'return_fs.txt', 
'Check for more than one break or goto statements' : 'one_break_or_goto_fs.txt', 
'Always enclose control statement blocks in curly braces': 'control_statements_with_braces_fs.txt',
'Check for empty functions':'no_empty_function_fs.txt',
'Do not nest switch statements':'no_nested_switch_fs.txt',
'Check for recursive functions':'recursion_fs.txt',
'All switch statements must have a default clause':'switch_default_must.txt',
'Do not make a pointer to a variable with lower storage duration':'storage_class_fs.txt',
'Check if selection sort is used' : 'selection_sort_fs.txt',
'Check if merge sort is used' : 'mergesort_fs.txt',
'Check if iterative binary search is used' : 'binary_search_iterative_fs.txt',
'Check if recursive binary search is used' : 'binary_search_recursive_fs.txt',
'Check for self-referential structure': 'self_ref_struct_fs.txt',
'Check if linked list is used':'insert_to_list_fs.txt',
#'Check for deletion linked list':'delete_fs.txt',
'Check if linked list with header node concept is used' : 'list_header_fs.txt',
'Check if linked list with tailer node concept is used' : 'list_tailer_fs.txt',
'Check if tree data structure is used ' : 'tree_fs.txt',
'Check if list iterator is used': 'list_iterator_fs.txt',
'Check if bottom-up dynamic programming has been used' : 'dp_fs.txt',
'Check if heap is used' : 'heap_fs.txt',
'Check if top-down dynamic programming(Memoization) has been used' : 'memoization_fs.txt',
'Check if stack is used' : 'stack_fs.txt',
'Check if indirect recursion is used' : 'indirect_recursion_fs.txt',
'Check if graph is used' : 'graph_fs.txt',
'Check if recursive dfs has been used' : 'dfs_recursive_fs.txt',
'Check if queue is used': 'queue_fs.txt',
'Check if bfs has been used' : 'bfs_fs.txt'
}

#Even code files without errors inserted into violations. Will have an empty list as value
def insert_code_fnames(violations, code_files):
    for cf in code_files:
        violations[cf] = []

def get_err_msgs(msgs):
    err_msgs = []
    for i in range(0, len(msgs), 2):
        lineno = msgs[i].strip()
        msg_str = msgs[i+1].strip()
        err_msgs.append((lineno, msg_str))
    print("err_msgs: ", err_msgs, "\n")
    return err_msgs
        
        
def print_dict(d):
    for key in d:
        print(key, ":")
        for l in d[key]:
            #print(key, ":", d[key])
            print(l)
    print()
    
def substitute_vars_in_rule(rule, selected_lib_dict, input_var_values):
    var_list = selected_lib_dict.get(rule, [])
    for var in var_list:
        key = "INPUT:"+var
        rule = rule.replace(key, str(input_var_values[var]))
    return rule    

#def main(selected_lib_list, fs_dict, code_files):
def main(selected_lib_dict, fs_dict, code_files, input_var_values):
    #print("EXECUTING Make_Parser.py in mysite/main")
    violations = {}
    insert_code_fnames(violations, code_files)
    #chosen_lib_rules = ['Declare Functions before Call',  'Set Max Depth of Looping']
    #chosen_lib_rules = ['Declare Functions before Call']

    #lib_struct_files = [lib_rules[key] for key in chosen_lib_rules]
    #print(lib_struct_files)
    
    #fs_files+=lib_struct_files
    #print(fs_files)

    #for struct_f in struct_files:
    #for struct_f in fs_files:
    lib_dict = { key : lib_rules[key] for key in selected_lib_dict }
    print("lib_dict :", lib_dict)
    chosen_rules = lib_dict
    chosen_rules.update(fs_dict)
    print("chosen_rules :", chosen_rules)
    
    #for rule in chosen_lib_rules:
    for rule in chosen_rules:
        #struct_f = lib_rules[rule]
        rule_args = ""
        print("selected_lib_dict", selected_lib_dict)
        var_list = selected_lib_dict.get(rule, [])
        for var in var_list:
            #rule_args = " ".join(selected_lib_dict[rule])
            rule_args +=" "+var+" "+str(input_var_values[var])
        struct_f = chosen_rules[rule]
        #create_parser_cmd = "%s %s < %s" % ( python, formal_struct_dir, file_sep, parser_creator, struct_f)
        create_parser_cmd = "%s %s %s < %s%s%s" % ( python, parser_creator, rule_args, formal_struct_dir, file_sep, struct_f)
        
        print(create_parser_cmd)
        os.system(create_parser_cmd)
        for code_f in code_files:
            run_parser_cmd = "%s %s < %s > %s"%(python, parser, code_f, err_msgs_file)
            #run_parser_cmd = "%s %s %s < %s > %s"%(python, parser, rule_args, code_f, err_msgs_file)
            #print(run_parser_cmd)
            os.system(run_parser_cmd)
            err_msgs_fh = open(err_msgs_file, "rt")
            parser_op = err_msgs_fh.readlines()
            err_msgs_fh.close()
            print("parser output: ", parser_op, "\n")
            err_msgs = get_err_msgs(parser_op)
            #violations[code_f] = [ (l, guidelines[struct_f], m) for l, m in err_msgs ]
            new_rule = substitute_vars_in_rule(rule, selected_lib_dict, input_var_values)
            violations[code_f] += [ (l, new_rule, m) for l, m in err_msgs ]
            #violations[code_f] += [ (l, rule, m) for l, m in err_msgs ]
    #print(violations)
    print("Violations in Run_Formal_Struct.py:")
    print_dict(violations)
    return violations
            

#main

#guidelines = {'Func_Proto_Formal_Struct.txt' : 'Declare functions before call'}
#fname : guideline_name
#struct_files = ['Func_Proto_Formal_Struct.txt']
#struct_files = list(guidelines.keys())
#print("struct files:", struct_files, "\n")

#code_files = ['test_func_declared.c']
#code_files = ['test_func_declared.c', 'func_proto_tests/test_new.txt', 'func_proto_tests/test_new2.txt', 'func_proto_tests/test_new3.txt', 'func_proto_tests/test_new4.txt', 'func_proto_tests/test_show.txt']

#Change to python when running on Windows
#python="python3"
#parser_creator = "Make_Parser.py"
#parser="C_Parser_new.py"

#err_msgs_file = "Violations.txt"

#err_msgs_fh = open(err_msgs_file, "rt")
#fh = file handle
#violations = {}
#insert_code_fnames(violations)
#print("Violations after inserting code files", violations, "\n")

#main(['Declare Functions before Call'], [], ['Code.c'])
#print("Violations:")
#print_dict(violations)
#print("final:", violations, "\n")
#err_msgs_fh.close()


