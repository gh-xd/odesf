import types
from process import __process_eq_str, __process_const_str


def eq_to_pyfunc(equations, constants=None, with_return=False):
    eqs_str = __process_eq_str(equations)

    if constants and not with_return:
        cons_str = __process_const_str(constants)
        return __func_from_string(f"def func(_x_, _y_, _f_): {cons_str} {eqs_str}")

    elif constants and with_return:
        cons_str = __process_const_str(constants)
        return __func_from_string(f"def func(_x_, _y_, _f_): {cons_str} {eqs_str} return _f_ ")

    elif constants is None and not with_return:
        return __func_from_string(f"def func(_x_, _y_, _f_): {eqs_str}")

    elif constants is None and with_return:
        return __func_from_string(f"def func(_x_, _y_, _f_): {eqs_str} return _f_ ")

def eq_to_pyfunc_string(equations, constants=None, with_return=False):
    eqs_str = __process_eq_str(equations)

    if constants and not with_return:
        cons_str = __process_const_str(constants)
        return f"def func(_x_, _y_, _f_): {cons_str} {eqs_str}"

    elif constants and with_return:
        cons_str = __process_const_str(constants)
        return f"def func(_x_, _y_, _f_): {cons_str} {eqs_str} return _f_ "

    elif constants is None and not with_return:
        return f"def func(_x_, _y_, _f_): {eqs_str}"

    elif constants is None and with_return:
        return f"def func(_x_, _y_, _f_): {eqs_str} return _f_ "

def __func_from_string(func_str):
    module_code = compile(func_str, '', 'exec')
    function_code = [c for c in module_code.co_consts if isinstance(c, types.CodeType)][0]
    func = types.FunctionType(function_code, globals())
    return func