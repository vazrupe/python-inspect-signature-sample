from functools import wraps
from inspect import signature


def param_info(func):
    sig = signature(func)
    for param in sig.parameters.values():
        print(param.name)
        print(' -', param.default)
        print(' -', param.kind)


def safe_param(func):
    ok_args = False
    ok_kwargs = False

    list_params = []
    keyword_params = set()

    sig = signature(func)
    for param in sig.parameters.values():
        if param.kind == param.VAR_POSITIONAL:
            ok_args = True
        if param.kind == param.VAR_KEYWORD:
            ok_kwargs = True

        if param.kind in [param.POSITIONAL_OR_KEYWORD]:
            list_params.append(param.name)
        if param.kind in [param.POSITIONAL_OR_KEYWORD, param.KEYWORD_ONLY]:
            keyword_params.add(param.name)

    def get_default_value(param_name):
        original = sig.parameters[param_name]
        no_default = original.default is original.empty
        return None if original.default is original.empty else original.default

    @wraps(func)
    def wrap(*args, **kwargs):
        if not ok_args:
            args = args[:len(list_params)]

        if not ok_kwargs:
            temp = {k: v for k, v in kwargs.items() if k in keyword_params}
            kwargs = temp

        if len(args) < len(list_params):
            not_set_list_params = list_params[len(args):]
            for param in not_set_list_params:
                if param in kwargs:
                    continue

                kwargs[param] = get_default_value(param)

        not_set_keyword_params = keyword_params - set(list_params)
        not_set_keyword_params -= set(kwargs.keys())
        for param in not_set_keyword_params:
            kwargs[param] = get_default_value(param)

        return func(*args, **kwargs)
    return wrap


def safe_param2(default=None):
    def deco(func):
        ok_args = False
        ok_kwargs = False

        list_params = []
        keyword_params = set()

        sig = signature(func)
        for param in sig.parameters.values():
            if param.kind == param.VAR_POSITIONAL:
                ok_args = True
            if param.kind == param.VAR_KEYWORD:
                ok_kwargs = True

            if param.kind in [param.POSITIONAL_OR_KEYWORD]:
                list_params.append(param.name)
            if param.kind in [param.POSITIONAL_OR_KEYWORD, param.KEYWORD_ONLY]:
                keyword_params.add(param.name)

        def get_default_value(param_name):
            original = sig.parameters[param_name]
            no_default = original.default is original.empty
            return (
                default
                if original.default is original.empty
                else original.default
            )

        @wraps(func)
        def wrap(*args, **kwargs):
            if not ok_args:
                args = args[:len(list_params)]

            if not ok_kwargs:
                temp = {k: v for k, v in kwargs.items() if k in keyword_params}
                kwargs = temp

            if len(args) < len(list_params):
                not_set_list_params = list_params[len(args):]
                for param in not_set_list_params:
                    if param in kwargs:
                        continue

                    kwargs[param] = get_default_value(param)

            not_set_keyword_params = keyword_params - set(list_params)
            not_set_keyword_params -= set(kwargs.keys())
            for param in not_set_keyword_params:
                kwargs[param] = get_default_value(param)

            return func(*args, **kwargs)
        return wrap
    return deco
