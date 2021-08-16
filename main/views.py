from django.shortcuts import render, redirect
from . import Run_Formal_Structs
import os
import copy

def handle_uploaded_file(f, newfname):
    with open(newfname, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
def handle_uploaded_texarea(text, newfname):
    with open(newfname, 'wt+') as destination:
        destination.write(text)            
            
def process_guideline_variables(rule_names, guideline_vars):
    processed_guidelines = {}
    new_rule_names = {} #rule:rule with input tags
    print("GUIDELINE_VARS D:", guideline_vars)
    for i in range(len(rule_names)):
        cur_rule = rule_names[i]
        new_rule_names[cur_rule]=cur_rule
        print("CUR_RULE:", cur_rule)
        for word in cur_rule.split():
            if(word.startswith('INPUT')):
                var_name = word.split(':')[1]
                print("var_name =", var_name)
                print(guideline_vars.get(cur_rule, []))
                var_list = guideline_vars.get(cur_rule, [])
                var_list.append(var_name)
                guideline_vars[cur_rule] = var_list
                input_markup = "<input name='{}' size='3'>".format(var_name)
                print("input_markup =", input_markup)
                new_rule_names[cur_rule] = new_rule_names[cur_rule].replace(word, input_markup)
    print("Inside insert_input_tags after processing", rule_names)
    print("guideline_vars:", guideline_vars)
    print("new_rule_names:", new_rule_names)
    return new_rule_names, guideline_vars
        
def get_rule_vars(selected_lib_rules, guideline_vars):
    selected_rules_with_vars = {}
    for key in selected_lib_rules:
        selected_rules_with_vars[key] = guideline_vars.get(key, [])
    return selected_rules_with_vars
                   
def replace_var_vals(chosen_guideline_names, input_var_values, selected_lib_rules_with_vars):
    for i in range(len(chosen_guideline_names)):
        rule = chosen_guideline_names[i]
        var_list = selected_lib_rules_with_vars.get(rule, [])
        for var in var_list:
            key = "INPUT:"+var
            chosen_guideline_names[i] = chosen_guideline_names[i].replace(key, str(input_var_values[var]))
    return chosen_guideline_names
        
# Create your views here.

def home(request):
    request.session['code_file_count'] = 0
    request.session['file_count'] = 0
    request.session['fs_files'] = list()
    request.session['code_files'] = list()
    request.session['new_fs_rules'] = dict()
    request.session['chosen_guideline_names'] = list()
    request.session['lines'] = dict()
    request.session['v'] = dict()
    request.session['g'] = dict()
    request.session['file_contents'] = dict()
    request.session['input_var_values'] = dict()
    request.session['selected_lib_rules_with_vars'] = dict()
    guideline_vars = {}
    rule_names = dict()
    lib_rules = Run_Formal_Structs.lib_rules
    print("LIB RULES:", lib_rules)
    input_tagged_rules, guideline_vars = process_guideline_variables(list(lib_rules.keys()), guideline_vars)
    for rule in lib_rules:
        rule_names[rule]=input_tagged_rules[rule]
    request.session['rule_names'] = rule_names
    request.session['guideline_vars'] = guideline_vars
    return render(request, 'index_new.html', {"guideline_names":rule_names, "chosen_guideline_names":[]})


def home_reload(request):
    fh = open("Cmd_info.txt", "rt")
    text = fh.read()
    fh.close()
    chosen_guideline_names = request.session['chosen_guideline_names']
    input_var_values = request.session['input_var_values']
    selected_lib_rules_with_vars = request.session['selected_lib_rules_with_vars']
    replace_var_vals(chosen_guideline_names, input_var_values, selected_lib_rules_with_vars)
    print("After replace in chosen_guideline_names:", chosen_guideline_names)
    request.session['chosen_guideline_names'] = chosen_guideline_names
    rule_names = request.session['rule_names']
    print("After change RULE_NAMES :", rule_names)
    return render(request, 'index_new.html', {"cmd_info":text, "guideline_names":rule_names, "chosen_guideline_names":chosen_guideline_names})
    
def get_prog_files(request):
    code_files = request.session['code_files']
    code_file_count = request.session['code_file_count']
    print(request.FILES)
    uploaded_progs = request.FILES.getlist('code_file')
    print("uploaded_progs:", uploaded_progs)
    for prog_f in uploaded_progs:
        code_file_count+=1
        fname = "prog_%d.c"%code_file_count
        handle_uploaded_file(prog_f, fname)
        code_files.append(fname)
    print("code_files", code_files)
    print("code_file_count", code_file_count)
    request.session['code_file_count'] = code_file_count
    request.session['code_files'] = code_files
    response = redirect('home_reload')
    return response
        
'''
def get_selected_lib_rules(request):
    guideline_vars = request.session['guideline_vars']
    input_var_values = request.session['input_var_values']
    selected_lib_rules_with_vars = request.session['selected_lib_rules_with_vars']
    print("request.POST:", request.POST)
    selected_lib_rules = request.GET.getlist('lib_rule', [])
    print("selected_lib_rules:", selected_lib_rules)
    chosen_guideline_names = request.session['chosen_guideline_names']
    chosen_guideline_names.extend(selected_lib_rules)
    selected_lib_rules_with_vars = get_rule_vars(selected_lib_rules, guideline_vars)
    print("selected_lib_rules_with_vars:", selected_lib_rules)
    for selected_rule in selected_lib_rules_with_vars:
        var_list = selected_lib_rules_with_vars[selected_rule]
        for v in var_list:
            input_var_values[v] = request.GET[v]
    print("input_var_values",  input_var_values )
    print("selected_lib_rules_with_vars", selected_lib_rules_with_vars)
    request.session['selected_lib_rules'] = selected_lib_rules
    request.session['chosen_guideline_names'] = chosen_guideline_names
    request.session['input_var_values'] = input_var_values
    request.session['selected_lib_rules_with_vars'] = selected_lib_rules_with_vars
    response = redirect('home_reload')
    return response'''

def get_selected_lib_rules(request):
    guideline_vars = request.session['guideline_vars']
    input_var_values = request.session['input_var_values']
    selected_lib_rules_with_vars = request.session['selected_lib_rules_with_vars']
    print("request.POST:", request.POST)
    selected_lib_rules = request.GET.getlist('lib_rule', [])
    print("selected_lib_rules:", selected_lib_rules)
    chosen_guideline_names = request.session['chosen_guideline_names']
    chosen_guideline_names.extend(selected_lib_rules)
    selected_lib_rules_with_vars = get_rule_vars(selected_lib_rules, guideline_vars)
    print("selected_lib_rules_with_vars:", selected_lib_rules)
    for selected_rule in selected_lib_rules_with_vars:
        var_list = selected_lib_rules_with_vars[selected_rule]
        for v in var_list:
            input_var_values[v] = request.GET[v]
    print("input_var_values",  input_var_values )
    print("selected_lib_rules_with_vars", selected_lib_rules_with_vars)
    request.session['selected_lib_rules'] = selected_lib_rules
    request.session['chosen_guideline_names'] = chosen_guideline_names
    request.session['input_var_values'] = input_var_values
    request.session['selected_lib_rules_with_vars'] = selected_lib_rules_with_vars
    response = redirect('home_reload')
    return response
    
def get_formal_struct(request):
    fs_files = request.session['fs_files']
    new_fs_rules = request.session['new_fs_rules']
    chosen_guideline_names = request.session['chosen_guideline_names']
    file_sep = Run_Formal_Structs.file_sep
    fs_dir = Run_Formal_Structs.formal_struct_dir
    print(request.POST)
    print(request.FILES)
    gname = request.POST['Guideline_Name']
    file_count=request.session['file_count']
    file_count+=1
    fname = 'fs_%d.txt'%(file_count)
    fs_path = "%s%s%s"%(fs_dir, file_sep, fname)
    print('fname', fname)
    print('fs_path', fs_path)
    fs = request.FILES.get('Upload_file', [])
    if(fs):
        handle_uploaded_file(fs, fs_path)
    else:
        fs_text = request.POST['fs_textarea']
        handle_uploaded_texarea(fs_text, fs_path)
    
    new_fs_rules[gname] = fname
    fs_files.append(fname)
    print("fs_files", fs_files)
    chosen_guideline_names.append(gname)
    request.session['file_count'] = file_count
    response = redirect('home_reload')
    request.session['fs_files'] = fs_files
    request.session['new_fs_rules'] = new_fs_rules
    request.session['chosen_guideline_names'] = chosen_guideline_names
    return response
         
    
def get_data(request):
    new_fs_rules = request.session['new_fs_rules']
    code_files = request.session['code_files']
    input_var_values = request.session['input_var_values']
    selected_lib_rules_with_vars = request.session['selected_lib_rules_with_vars']
    print("new_fs_rules:", new_fs_rules)
    try:
        selected_lib_rules = request.session['selected_lib_rules']
    except:
        pass
    chosen_guideline_names = request.session['chosen_guideline_names']
    #print("selected_lib_rules", selected_lib_rules)
    print("selected_lib_rules_with_vars:", selected_lib_rules_with_vars)
    violations = Run_Formal_Structs.main(selected_lib_rules_with_vars, new_fs_rules, code_files, input_var_values)
    print("Violations in views.py:")
    print(violations)
    lines = request.session['lines']
    v = request.session['v']
    g = request.session['g']
    for i in violations:
        lines[i]=list()
        g[i]=list()
        v[i]=list()
        for j in violations[i]:
            lines[i].append(j[0])
            g[i].append(j[1])
            v[i].append(j[2])
    print("line", lines)
    print("g", g)
    print(v)
    file_contents = request.session['file_contents']
    for fname in code_files:    
        fh = open(fname, "rt")
        content=fh.read()
        file_contents[fname] = content
        fh.close()
    print("file_contents = ", file_contents)
    print(v)
    print("g=",g)
    print("v=",v)
    print("lines=",lines)
    #print(selected_lib_rules)
    request.session['lines'] = lines
    request.session['v'] = v
    request.session['g'] = g
    request.session['file_contents'] = file_contents
    return render(request, 'page2.html',{"content":file_contents,"line":lines,"v":v,"g":g,'rules':chosen_guideline_names})

def filter(request):
    rule=request.POST['rules']
    selected_lib_rules = request.session['selected_lib_rules']
    chosen_guideline_names = request.session['chosen_guideline_names']
    lines = request.session['lines']
    v = request.session['v']
    g = request.session['g']
    file_contents = request.session['file_contents']
    print(rule)
    print("In filter")
    print(selected_lib_rules)
    l1=dict()
    v1=dict()
    g1=dict()
    for i in g:
        l1[i]=list()
        g1[i]=list()
        v1[i]=list()
        for j in range(0,len(g[i])):
            if(g[i][j]==rule):
                l1[i].append(lines[i][j])
                v1[i].append(v[i][j])
                g1[i].append(g[i][j])
    return render(request, 'page2.html',{"content":file_contents,"line":l1,"v":v1,"g":g1,'rules':chosen_guideline_names})
    
def start_again(request):
    del request.session['code_file_count']
    del request.session['file_count']
    del request.session['new_fs_rules']
    del request.session['fs_files']
    del request.session['chosen_guideline_names']
    try:
        del request.session['selected_lib_rules']
    except:
        pass
    return redirect('home') 

def run_again(request):
    modified_code = request.POST['modified_code']
    print("Modified code=", modified_code)
    return redirect('home') 