#Creates a dictionary of the form:
#filename:[(lineno, guideline_name, violation_msg)..]

import os

#When running on Windows
python="python"
file_sep = '\\'

#When running on Ubuntu
#python="python3"
#file_sep = '/'
#cur_dir = os.getcwd()
#cur_dir = ".."
#print(cur_dir)
parser_creator = "Make_Parser.py"
parser="C_Parser_new.py"
err_msgs_file = "Violations.txt"
formal_struct_dir = "fs"
#NOTE: Space not allowed in 'INPUT:<var_name>'
lib_rules = { 
#'Check for functions called before their declaration' : 'func_formal.txt', 
'Check for global variables' : 'global_formal.txt', 
#'Variable names must be at least 4 characters long' : 'var_len_formal.txt',
'Check for variable names less than INPUT:n characters long' : 'input_var_len.txt',
#'Functions should not have more than 10 lines': 'func_size_formal.txt',
'Check for functions having more than INPUT:max_size lines': 'input_func_size.txt',
'Check for use of rewind() (use fseek instead)' : 'fseek_formal.txt',
'Check for use of strcmp() (use strncmp() instead)' : 'strcmp_formal.txt',
'Check for loops with depth more than INPUT:allowed_depth' : 'while_formal_structure.txt', 
#'Always check if the return value of malloc() or calloc() is null':'null_formal.txt',
'Use SIZEOF to determine the size of a type in malloc() or calloc()':'sizeof_formal.txt',
'Specify void when function accepts no arguments':'void_formal.txt',
'Do not perform assignments in looping conditions':'assignment_in_loop.txt',
'Check if strings have been allocated sufficient space':'explicit_size_str_formal.txt',
'Do not use implicit typing': 'implicit_type_formal.txt',
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


