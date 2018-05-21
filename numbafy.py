__version__ = '0.52'
import sympy as sym

def numbafy(expression, parameters=None, constants=None, use_cse=False, new_function_name='numbafy_func'):
    cse = sym.cse(expression)
    
    code_parameters = ''
    code_constants = ''
    code_cse = ''

    if parameters:
        code_parameters = ', '.join(f'{p}' for p in parameters)
    
    if constants:
        code_constants = []
        for k, v in constants.items():
            code_constants.append(f'{k} = {v}')
        code_constants = '\n    '.join(code_constants)
        
    if use_cse:
        expressions = sym.cse(expression)
        code_cse = []
        for e in expressions[0]:
            k, v = e
            code_cse.append(f'{k} = {v}')
        code_cse = '\n    '.join(code_cse)
        code_expression = f'{expressions[1][0]}'
    else:
        code_expression = f'{expression}'
        

    template = f"""@jit
def {new_function_name}({code_parameters}):
    {code_constants}
    {code_cse}

    return {code_expression}"""
       
    return template


if __name__ == '__main__':
    import sympy as sym
    from numba import jit

    # this is a very basic example; numbafy shines with huge expression
    a, b, c = sym.symbols('a, b, c')

    constants = {c: 1.4}

    expression = c * a**b
    parameters = (a, b)

    num = numbafy(expression=expression, parameters=parameters, constants=constants, use_cse=True)
    exec(num)
    result = numbafy_func(a=2.0, b=3.0)
    print(result)