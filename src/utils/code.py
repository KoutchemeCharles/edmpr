import ast 
from astor import to_source 
from python_minifier import minify


def clean_code(code, remove_docstring=True):
    """ Minify and clean a source code.
    
    Remove comments, initial docstrings, and empty blank lines. 
    Additionally, add a new docstring to the code.
    """

    code = minify(code, rename_locals=False, 
                  remove_literal_statements=remove_docstring)
    return to_source(ast.parse(code)).strip()


def get_code_identation(code):
    code = clean_code(code)
    lines = code.split("\n")
    if len(lines) == 1:
        raise ValueError(code)
        
    n_indents = len(lines[1]) - len(lines[1].lstrip())
    return lines[1][:n_indents] 


def ast_to_passen_repre(sc_ast):
    """ Transforms a Python AST into the representation
    used for computing the tree edit distance used in 
    the python-edit-distance library 
    """
    adj_list = []
    n_list = []
    i = 0
    
    def get_children(node):
        names = node._fields
        print("names", names)
        return [(f, getattr(node, f)) for f in names]
    
    def dfs(node, i):
        node_name = str(node.__class__.__name__)
        adj_list.append([])
        n_list.append(node_name)
        node_adj_list = []
        for j, c in enumerate(ast.iter_child_nodes(node)):
            dfs(c, i + 1 + j)
            node_adj_list.append(i + 1 + j)
        adj_list[i] = node_adj_list
        
    dfs(sc_ast, i)
    
    return n_list, adj_list