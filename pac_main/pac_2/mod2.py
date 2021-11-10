def something_to_do_mod_2(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        li = []
        for i in args:
            res = i*i
            li.append(res)
        return li
    return wrapper

