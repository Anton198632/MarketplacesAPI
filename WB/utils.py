import inspect
import re


def build_parameters_for_url(url, function):
    frame = inspect.currentframe().f_back
    local_vars = frame.f_locals
    first_function_signature = inspect.signature(function)
    parameters = []
    for param_name, param in first_function_signature.parameters.items():
        if param_name != "body_request":
            param_value = local_vars[param_name]
            if param_value:
                parameters.append(f"{param_name}={param_value}")

    return f'{url}?{"&".join(parameters)}'


def is_xx_status(status_code, first_number):
    re_word = rf"^{first_number}\d\d$"
    return bool(re.match(re_word, str(status_code)))
