
def my_var():
    int_var: int = 42
    str_var: str = '42'
    str_lit_var: str = 'quarante-deux'
    float_var: float = 42.0
    bool_var: bool = True
    list_var: list = [42]
    dict_var: dict = {42: 42}
    tuple_var: tuple = (42, )
    set_var: set = set()

    for var_type in (int_var, str_var, str_lit_var, float_var, bool_var, list_var, dict_var, tuple_var, set_var):
        print(f'{var_type} has a type {type(var_type)}')


if __name__ == '__main__':
    my_var()
