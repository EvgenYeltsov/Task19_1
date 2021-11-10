# Относительный импорт
from ..pac_2.mod2 import something_to_do_mod_2


@something_to_do_mod_2
def number_in_sqr(*args):
    return args


result = number_in_sqr(3, 4, 8, 9)

