import function_type

def extract_function(function_node):
    name = function_node.children[0].children[0].value
    arity = len(function_node.children[0].children[1].children)
    result_type = function_type.make_type(
        function_node.children[0].children[2].children[0],
    )
    return name, function_type.FunctionType(arity, result_type)

def extract_assignment(assignment_node):
    name = assignment_node.children[0].children[0].value
    value_type = function_type.make_type(
        assignment_node.children[0].children[1],
    )
    return name, value_type
